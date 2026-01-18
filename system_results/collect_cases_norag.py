import os
import json
import numpy as np
import requests
from pathlib import Path
import time

# Configuration
API_ENDPOINT = "http://localhost:8080/api/v1/ecg-sessions"
JWT_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoidXNlciIsInVzZXJfaWQiOiI0MDA0YjgzNy1iODJkLTRkYzctOTQxYy1iNmYzOTA2NmUxOWIiLCJlbWFpbCI6InNvbmdva3Vwa2pAZ21haWwuY29tIiwidXNlcm5hbWUiOiJzb25nb2t1cGtqIiwic3ViIjoic29uZ29rdXBraiIsImlhdCI6MTc2NTk1Njc0OSwiZXhwIjoxNzY2MDQzMTQ5fQ.mC_bVrlEknQLzZZwwW1MDjjiZbo8xIb7p_ToxXyxMPxvMuZz6kVCy-daOBfYfBDJ9FoS0QixujpoeLyZrQ9Wug"  # Điền JWT token của bạn vào đây
DEVICE_ID = "05281231"
SAMPLING_RATE = 130
CASES_FOLDER = "36_cases_norag"
PROGRESS_FILE = "progress_norag.json"
ACCEPTED_FILES_LOG = "accepted_files_rag.json"  # Đọc từ file được tạo bởi collect_cases_rag.py

# Required successful cases per folder
REQUIRED_CASES_PER_FOLDER = 3


def load_progress():
    """Load progress from file if exists"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "current_file_index": 0,
        "total_cases_saved": 0
    }


def save_progress(progress):
    """Save current progress to file"""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)


def load_accepted_files():
    """Load accepted files list from RAG collection"""
    if not os.path.exists(ACCEPTED_FILES_LOG):
        print(f"⚠️  CẢNH BÁO: Không tìm thấy file {ACCEPTED_FILES_LOG}")
        print("Vui lòng chạy collect_cases_rag.py trước để tạo danh sách file.")
        return None
    
    with open(ACCEPTED_FILES_LOG, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_ecg_data(file_path):
    """Load ECG data from .npy file"""
    data = np.load(file_path)
    
    # Handle 2D array format [[1], [2], [3],...] -> [1, 2, 3,...]
    if isinstance(data, np.ndarray):
        # Check if it's a 2D array with shape (n, 1)
        if data.ndim == 2 and data.shape[1] == 1:
            data = data.flatten()
        # Convert numpy array to list for JSON serialization
        data = data.tolist()
    
    # Additional check for nested lists [[1], [2], [3],...]
    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], list):
        # Flatten nested list structure
        data = [item[0] if isinstance(item, list) and len(item) == 1 else item for item in data]
    
    return data


def create_request_body(ecg_signal):
    """Create request body according to example_request.json format"""
    return {
        "deviceId": DEVICE_ID,
        "rawData": {
            "signal": ecg_signal,
            "lead": "I",
            "duration": 10
        },
        "samplingRate": SAMPLING_RATE
    }


def send_ecg_request(ecg_signal):
    """Send ECG data to server and return response"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {JWT_TOKEN}"
    }
    
    request_body = create_request_body(ecg_signal)
    
    try:
        response = requests.post(API_ENDPOINT, json=request_body, headers=headers, timeout=30)
        
        if response.status_code == 201:
            return response.json(), None
        else:
            return None, f"HTTP Error {response.status_code}: {response.text}"
    
    except requests.exceptions.RequestException as e:
        return None, f"Request Error: {str(e)}"


def save_case(response, case_index):
    """Save response as case file"""
    os.makedirs(CASES_FOLDER, exist_ok=True)
    case_filename = os.path.join(CASES_FOLDER, f"case_{case_index}.json")
    
    with open(case_filename, 'w', encoding='utf-8') as f:
        json.dump(response, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Đã lưu case_{case_index}.json")


def process_accepted_files():
    """Main processing function - reprocess accepted files from RAG collection"""
    # Check JWT token
    if not JWT_TOKEN:
        print("⚠️  CẢNH BÁO: JWT_TOKEN chưa được cấu hình!")
        print("Vui lòng cập nhật JWT_TOKEN trong file collect_cases_norag.py")
        return
    
    # Load accepted files list
    accepted_files = load_accepted_files()
    if accepted_files is None:
        return
    
    # Load progress
    progress = load_progress()
    
    # Ensure 36_cases_norag folder exists
    os.makedirs(CASES_FOLDER, exist_ok=True)
    
    print("=" * 80)
    print("BẮT ĐẦU THU THẬP DỮ LIỆU ECG (NO RAG)")
    print("=" * 80)
    print(f"Tổng số file cần xử lý: {len(accepted_files)}")
    print(f"Tiến trình hiện tại: {progress['total_cases_saved']}/{len(accepted_files)} cases")
    print()
    
    # Start from saved progress
    start_idx = progress['current_file_index']
    
    for file_idx in range(start_idx, len(accepted_files)):
        file_info = accepted_files[file_idx]
        
        folder_name = file_info['folder']
        npy_file = file_info['filename']
        file_path = file_info['file_path']
        expected_diagnosis = file_info['diagnosis']
        
        print(f"\n[{file_idx + 1}/{len(accepted_files)}] Đang xử lý: {file_path}")
        print(f"  Folder: {folder_name}")
        print(f"  Chẩn đoán mong đợi: {expected_diagnosis}")
        
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"  ⚠️  File không tồn tại, bỏ qua...")
            progress['current_file_index'] = file_idx + 1
            save_progress(progress)
            continue
        
        try:
            # Load ECG data
            ecg_signal = load_ecg_data(file_path)
            
            # Send request
            print(f"  → Gửi request đến server...")
            response, error = send_ecg_request(ecg_signal)
            
            if error:
                print(f"  ✗ Lỗi: {error}")
                
                # Check if it's a quota error
                if "quota" in error.lower() or "429" in error or "401" in error:
                    print("\n" + "=" * 80)
                    print("⚠️  PHÁT HIỆN LỖI QUOTA/AUTHENTICATION!")
                    print("=" * 80)
                    print("Vui lòng:")
                    print("1. Cập nhật JWT_TOKEN mới trong file collect_cases_norag.py")
                    print("2. Chạy lại script để tiếp tục từ vị trí hiện tại")
                    print(f"\nTiến trình đã được lưu: {progress['total_cases_saved']}/{len(accepted_files)} cases")
                    print("=" * 80)
                    return
                
                # Update progress and continue
                progress['current_file_index'] = file_idx + 1
                save_progress(progress)
                time.sleep(1)  # Wait a bit before next request
                continue
            
            # Save case (regardless of diagnosis match, since we're reprocessing)
            progress['total_cases_saved'] += 1
            save_case(response, progress['total_cases_saved'])
            
            actual_diagnosis = response.get("prediction", {}).get("diagnosis", "Không xác định")
            print(f"  ✓ Đã lưu case | Chẩn đoán: {actual_diagnosis}")
            
            # Check if diagnosis still matches
            if actual_diagnosis == expected_diagnosis:
                print(f"  ✓ Chẩn đoán vẫn khớp")
            else:
                print(f"  ⚠️  Chẩn đoán khác: mong đợi '{expected_diagnosis}', nhận '{actual_diagnosis}'")
            
            print(f"  → Tiến trình: {progress['total_cases_saved']}/{len(accepted_files)} cases")
            
            # Update progress
            progress['current_file_index'] = file_idx + 1
            save_progress(progress)
            
            # Small delay to avoid overwhelming the server
            time.sleep(0.5)
        
        except Exception as e:
            print(f"  ✗ Lỗi khi xử lý file: {e}")
            progress['current_file_index'] = file_idx + 1
            save_progress(progress)
            continue
    
    # Final summary
    print("\n" + "=" * 80)
    print("HOÀN THÀNH!")
    print("=" * 80)
    print(f"Tổng số cases đã thu thập: {progress['total_cases_saved']}/{len(accepted_files)}")
    print(f"Folder lưu trữ: {CASES_FOLDER}")
    print("=" * 80)


if __name__ == "__main__":
    try:
        process_accepted_files()
    except KeyboardInterrupt:
        print("\n\n⚠️  Chương trình bị ngắt bởi người dùng")
        print("Tiến trình đã được lưu. Chạy lại script để tiếp tục.")
    except Exception as e:
        print(f"\n\n✗ Lỗi không mong đợi: {e}")
        print("Tiến trình đã được lưu. Chạy lại script để tiếp tục.")
