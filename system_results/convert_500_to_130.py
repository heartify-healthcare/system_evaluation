import numpy as np
from scipy import signal
import os
import math

# --- CẤU HÌNH ---
ORIGIN_FS = 500   # Tần số gốc hiện tại
TARGET_FS = 130   # Tần số mục tiêu
CHUNK_SEC = 10    # Độ dài mỗi đoạn (giây)

# Số mẫu cho mỗi đoạn
SAMPLES_ORIGIN = ORIGIN_FS * CHUNK_SEC  # 500 * 10 = 5000
SAMPLES_TARGET = TARGET_FS * CHUNK_SEC  # 130 * 10 = 1300

# Các folder bệnh tim cần chuyển đổi (trừ 'data')
DISEASE_FOLDERS = ['AFIB', 'AFL', 'Brady', 'IAVB', 'LBBB', 'Normal', 'PAC', 'PVC', 'RBBB', 'STD', 'STE', 'Tachy']

def downsample_ecg_file(file_path):
    """
    Chuyển đổi một file ECG từ 500Hz xuống 130Hz
    
    Args:
        file_path: Đường dẫn đến file .npy cần chuyển đổi
    
    Returns:
        True nếu thành công, False nếu có lỗi
    """
    try:
        # Đọc dữ liệu 500Hz
        data_500 = np.load(file_path)
        
        # Kiểm tra độ dài
        if len(data_500) != SAMPLES_ORIGIN:
            print(f"  ⚠️  Bỏ qua {os.path.basename(file_path)}: Độ dài không đúng ({len(data_500)} != {SAMPLES_ORIGIN})")
            return False
        
        # --- QUÁ TRÌNH CHUYỂN ĐỔI NGƯỢC ---
        # Bước 1: Denormalize nếu cần (tùy chọn - có thể bỏ qua vì ta sẽ normalize lại)
        # Vì dữ liệu đã được Z-score normalize, ta có thể làm việc trực tiếp
        
        # Bước 2: Tính toán tỷ lệ Resample (Polyphase)
        # GCD(130, 500) = 10 -> Up=13, Down=50
        g = math.gcd(TARGET_FS, ORIGIN_FS)
        up = TARGET_FS // g      # 13
        down = ORIGIN_FS // g    # 50
        
        # Bước 3: Polyphase Resample (downsample)
        data_130 = signal.resample_poly(data_500, up, down)
        
        # Bước 4: Fix độ dài chính xác (nếu cần)
        if len(data_130) != SAMPLES_TARGET:
            data_130 = signal.resample(data_130, SAMPLES_TARGET)
        
        # Bước 5: Normalize lại (Z-score)
        if np.std(data_130) > 1e-6:
            data_final = (data_130 - np.mean(data_130)) / np.std(data_130)
        else:
            data_final = np.zeros_like(data_130)
        
        # Bước 6: Ghi đè lên file gốc
        np.save(file_path, data_final.astype(np.float32))
        
        return True
        
    except Exception as e:
        print(f"  ❌ Lỗi khi xử lý {os.path.basename(file_path)}: {str(e)}")
        return False

def process_all_folders():
    """
    Duyệt qua tất cả các folder bệnh tim và chuyển đổi các file .npy
    """
    # Tính toán tỷ lệ để hiển thị thông tin
    g = math.gcd(TARGET_FS, ORIGIN_FS)
    up = TARGET_FS // g
    down = ORIGIN_FS // g
    
    print("=" * 70)
    print("🔄 CHUYỂN ĐỔI ECG TỪ 500Hz XUỐNG 130Hz")
    print("=" * 70)
    print(f"📊 Tần số gốc:     {ORIGIN_FS} Hz ({SAMPLES_ORIGIN} mẫu / {CHUNK_SEC}s)")
    print(f"📊 Tần số mục tiêu: {TARGET_FS} Hz ({SAMPLES_TARGET} mẫu / {CHUNK_SEC}s)")
    print(f"⚙️  Thuật toán:     Polyphase (Up {up} / Down {down})")
    print("=" * 70)
    
    total_files = 0
    total_success = 0
    total_failed = 0
    
    # Lấy thư mục làm việc hiện tại
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    for folder_name in DISEASE_FOLDERS:
        folder_path = os.path.join(base_dir, folder_name)
        
        # Kiểm tra folder có tồn tại không
        if not os.path.exists(folder_path):
            print(f"\n⚠️  Folder '{folder_name}' không tồn tại, bỏ qua...")
            continue
        
        # Lấy danh sách file .npy
        npy_files = [f for f in os.listdir(folder_path) if f.endswith('.npy')]
        
        if len(npy_files) == 0:
            print(f"\n📁 {folder_name}: Không có file .npy")
            continue
        
        print(f"\n📁 {folder_name}: Tìm thấy {len(npy_files)} file(s)")
        
        # Xử lý từng file
        folder_success = 0
        folder_failed = 0
        
        for npy_file in npy_files:
            file_path = os.path.join(folder_path, npy_file)
            total_files += 1
            
            if downsample_ecg_file(file_path):
                folder_success += 1
                total_success += 1
            else:
                folder_failed += 1
                total_failed += 1
        
        # Hiển thị kết quả cho folder
        if folder_success > 0:
            print(f"  ✅ Đã chuyển đổi: {folder_success} file(s)")
        if folder_failed > 0:
            print(f"  ❌ Thất bại: {folder_failed} file(s)")
    
    # Tổng kết
    print("\n" + "=" * 70)
    print("📊 TỔNG KẾT")
    print("=" * 70)
    print(f"Tổng số file đã xử lý: {total_files}")
    print(f"✅ Thành công:         {total_success}")
    print(f"❌ Thất bại:           {total_failed}")
    print("=" * 70)
    
    if total_success > 0:
        print("\n🎉 Hoàn tất! Tất cả file đã được ghi đè với dữ liệu 130Hz.")
    else:
        print("\n⚠️  Không có file nào được chuyển đổi thành công.")

if __name__ == "__main__":
    # Xác nhận với người dùng trước khi thực hiện
    print("⚠️  CẢNH BÁO: Script này sẽ GHI ĐÈ lên tất cả file .npy trong các folder bệnh tim!")
    print("⚠️  Dữ liệu gốc sẽ bị thay thế bằng dữ liệu 130Hz.")
    print()
    
    response = input("Bạn có chắc chắn muốn tiếp tục? (yes/no): ").strip().lower()
    
    if response in ['yes', 'y']:
        print("\n🚀 Bắt đầu chuyển đổi...\n")
        process_all_folders()
    else:
        print("\n❌ Đã hủy bỏ.")
