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
CASES_FOLDER = "36_cases"
PROGRESS_FILE = "progress.json"
DIAGNOSIS_MAP_FILE = "diagnosis_map.json"

# Folders to process
FOLDERS = ["AFIB", "AFL", "Brady", "IAVB", "LBBB", "Normal", "PAC", "PVC", "RBBB", "STD", "STE", "Tachy"]

# Required successful cases per folder
REQUIRED_CASES_PER_FOLDER = 3


def load_diagnosis_map():
    """Load diagnosis mapping from JSON file"""
    with open(DIAGNOSIS_MAP_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_progress():
    """Load progress from file if exists"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "current_folder_index": 0,
        "current_file_index": 0,
        "total_cases_saved": 0,
        "folder_stats": {folder: 0 for folder in FOLDERS}
    }


def save_progress(progress):
    """Save current progress to file"""
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)


def get_npy_files(folder_path):
    """Get all .npy files in a folder"""
    return sorted([f for f in os.listdir(folder_path) if f.endswith('.npy')])


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


def check_diagnosis_match(response, expected_diagnosis):
    """Check if response diagnosis matches expected diagnosis"""
    try:
        actual_diagnosis = response.get("prediction", {}).get("diagnosis", "")
        return actual_diagnosis == expected_diagnosis
    except Exception as e:
        print(f"Error checking diagnosis: {e}")
        return False


def save_case(response, case_index):
    """Save response as case file"""
    os.makedirs(CASES_FOLDER, exist_ok=True)
    case_filename = os.path.join(CASES_FOLDER, f"case_{case_index}.json")
    
    with open(case_filename, 'w', encoding='utf-8') as f:
        json.dump(response, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Đã lưu case_{case_index}.json")


def process_folders():
    """Main processing function"""
    # Check JWT token
    if not JWT_TOKEN:
        print("⚠️  CẢNH BÁO: JWT_TOKEN chưa được cấu hình!")
        print("Vui lòng cập nhật JWT_TOKEN trong file collect_cases.py")
        return
    
    # Load necessary data
    diagnosis_map = load_diagnosis_map()
    progress = load_progress()
    
    # Ensure 36_cases folder exists
    os.makedirs(CASES_FOLDER, exist_ok=True)
    
    print("=" * 80)
    print("BẮT ĐẦU THU THẬP DỮ LIỆU ECG")
    print("=" * 80)
    print(f"Tiến trình hiện tại: {progress['total_cases_saved']}/36 cases")
    print()
    
    # Start from saved progress
    for folder_idx in range(progress['current_folder_index'], len(FOLDERS)):
        folder_name = FOLDERS[folder_idx]
        folder_path = folder_name
        
        # Check if folder exists
        if not os.path.exists(folder_path):
            print(f"⚠️  Folder '{folder_name}' không tồn tại. Bỏ qua...")
            progress['current_folder_index'] = folder_idx + 1
            progress['current_file_index'] = 0
            save_progress(progress)
            continue
        
        expected_diagnosis = diagnosis_map.get(folder_name, "")
        successful_cases = progress['folder_stats'][folder_name]
        
        print(f"\n{'=' * 80}")
        print(f"Đang xử lý folder: {folder_name} ({successful_cases}/{REQUIRED_CASES_PER_FOLDER} cases)")
        print(f"Chẩn đoán mong đợi: {expected_diagnosis}")
        print(f"{'=' * 80}\n")
        
        # Get all .npy files
        npy_files = get_npy_files(folder_path)
        
        if not npy_files:
            print(f"⚠️  Không tìm thấy file .npy trong folder '{folder_name}'")
            progress['current_folder_index'] = folder_idx + 1
            progress['current_file_index'] = 0
            save_progress(progress)
            continue
        
        # Process files starting from saved file index
        start_file_idx = progress['current_file_index'] if folder_idx == progress['current_folder_index'] else 0
        
        for file_idx in range(start_file_idx, len(npy_files)):
            # Check if we already have enough successful cases for this folder
            if successful_cases >= REQUIRED_CASES_PER_FOLDER:
                print(f"✓ Đã đủ {REQUIRED_CASES_PER_FOLDER} cases cho folder {folder_name}")
                break
            
            npy_file = npy_files[file_idx]
            file_path = os.path.join(folder_path, npy_file)
            
            print(f"  [{file_idx + 1}/{len(npy_files)}] Đang xử lý: {npy_file}")
            
            try:
                # Load ECG data
                ecg_signal = load_ecg_data(file_path)
                
                # Send request
                print(f"    → Gửi request đến server...")
                response, error = send_ecg_request(ecg_signal)
                
                if error:
                    print(f"    ✗ Lỗi: {error}")
                    
                    # Check if it's a quota error (you may need to adjust this check)
                    if "quota" in error.lower() or "429" in error or "401" in error:
                        print("\n" + "=" * 80)
                        print("⚠️  PHÁT HIỆN LỖI QUOTA/AUTHENTICATION!")
                        print("=" * 80)
                        print("Vui lòng:")
                        print("1. Cập nhật JWT_TOKEN mới trong file collect_cases.py")
                        print("2. Chạy lại script để tiếp tục từ vị trí hiện tại")
                        print(f"\nTiến trình đã được lưu: {progress['total_cases_saved']}/36 cases")
                        print("=" * 80)
                        return
                    
                    # Update progress and continue
                    progress['current_file_index'] = file_idx + 1
                    save_progress(progress)
                    time.sleep(1)  # Wait a bit before next request
                    continue
                
                # Check diagnosis match
                if check_diagnosis_match(response, expected_diagnosis):
                    actual_diagnosis = response.get("prediction", {}).get("diagnosis", "")
                    print(f"    ✓ Chẩn đoán đúng: {actual_diagnosis}")
                    
                    # Save case
                    progress['total_cases_saved'] += 1
                    save_case(response, progress['total_cases_saved'])
                    
                    # Update stats
                    successful_cases += 1
                    progress['folder_stats'][folder_name] = successful_cases
                    
                    print(f"    → Tiến trình: {progress['total_cases_saved']}/36 cases tổng | {successful_cases}/{REQUIRED_CASES_PER_FOLDER} cases cho {folder_name}")
                else:
                    actual_diagnosis = response.get("prediction", {}).get("diagnosis", "Không xác định")
                    print(f"    ✗ Chẩn đoán không khớp: {actual_diagnosis}")
                
                # Update progress
                progress['current_file_index'] = file_idx + 1
                save_progress(progress)
                
                # Small delay to avoid overwhelming the server
                time.sleep(0.5)
            
            except Exception as e:
                print(f"    ✗ Lỗi khi xử lý file: {e}")
                progress['current_file_index'] = file_idx + 1
                save_progress(progress)
                continue
        
        # Move to next folder
        progress['current_folder_index'] = folder_idx + 1
        progress['current_file_index'] = 0
        save_progress(progress)
    
    # Final summary
    print("\n" + "=" * 80)
    print("HOÀN THÀNH!")
    print("=" * 80)
    print(f"Tổng số cases đã thu thập: {progress['total_cases_saved']}/36")
    print("\nChi tiết theo folder:")
    for folder in FOLDERS:
        count = progress['folder_stats'][folder]
        status = "✓" if count >= REQUIRED_CASES_PER_FOLDER else "✗"
        print(f"  {status} {folder}: {count}/{REQUIRED_CASES_PER_FOLDER} cases")
    print("=" * 80)


if __name__ == "__main__":
    try:
        process_folders()
    except KeyboardInterrupt:
        print("\n\n⚠️  Chương trình bị ngắt bởi người dùng")
        print("Tiến trình đã được lưu. Chạy lại script để tiếp tục.")
    except Exception as e:
        print(f"\n\n✗ Lỗi không mong đợi: {e}")
        print("Tiến trình đã được lưu. Chạy lại script để tiếp tục.")
