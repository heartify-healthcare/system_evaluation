import pandas as pd
import numpy as np
import shutil
from pathlib import Path
import random

# Đọc file labels.csv
df = pd.read_csv('labels.csv')


# Lọc chỉ lấy các mẫu train
train_df = df[df['split'] == 'train'].copy()

# Danh sách 12 loại bệnh
disease_labels = ['AFIB', 'AFL', 'Brady', 'IAVB', 'LBBB', 'Normal', 'PAC', 'PVC', 'RBBB', 'STD', 'STE', 'Tachy']


print("Bắt đầu copy các mẫu test ngẫu nhiên...\n")


for disease in disease_labels:
    print(f"Xử lý loại bệnh: {disease}")
    # Lấy tất cả các mẫu train có liên quan tới STD (labels chứa STD, có thể có dấu chấm phẩy)
    disease_samples = train_df[train_df['labels'].str.contains(disease)]
    if len(disease_samples) == 0:
        print(f"  ⚠ Không tìm thấy mẫu train nào cho {disease}")
        continue
    print(f"  Tìm thấy {len(disease_samples)} mẫu train liên quan tới {disease}")
    # Chọn ngẫu nhiên tối đa 10 mẫu
    n_samples = min(10, len(disease_samples))
    selected_samples = disease_samples.sample(n=n_samples)
    print(f"  Chọn ngẫu nhiên {n_samples} mẫu để copy")
    # Xóa sạch folder đích trước khi copy
    target_folder = Path(disease)
    if target_folder.exists() and target_folder.is_dir():
        for f in target_folder.iterdir():
            if f.is_file():
                f.unlink()
            elif f.is_dir():
                shutil.rmtree(f)
    else:
        target_folder.mkdir(exist_ok=True)

    # Copy các file
    for idx, row in selected_samples.iterrows():
        filename = row['filename']
        source_file = Path('data') / filename
        target_file = target_folder / filename
        if source_file.exists():
            shutil.copy2(source_file, target_file)
            print(f"  ✓ Copied: {filename}")
        else:
            print(f"  ✗ File không tồn tại: {filename}")
    print()

print("Hoàn tất!")
