import json
import matplotlib.pyplot as plt
import os

# Đọc dữ liệu từ file JSON
with open('latency_results.json', 'r') as f:
    data = json.load(f)

# Tạo folder graphs nếu chưa có
os.makedirs('graphs', exist_ok=True)

# Lấy dữ liệu cho mỗi trường
t_upload = [item['T_upload'] for item in data]
t_denoise = [item['T_denoise'] for item in data]
t_classify = [item['T_classify'] for item in data]
t_llm = [item['T_LLM'] for item in data]
t_total = [item['T_total'] for item in data]

# Tạo trục x (request number)
x = list(range(1, len(data) + 1))

# 1. Biểu đồ T_upload
plt.figure(figsize=(12, 6))
plt.plot(x, t_upload, marker='o', linewidth=2, markersize=4, color='#2E86AB')
plt.title('T_upload: Thời gian chuyển dữ liệu từ Frontend đến Server', fontsize=14, fontweight='bold')
plt.xlabel('Request Number', fontsize=12)
plt.ylabel('Time (ms)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('graphs/t_upload.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Biểu đồ T_denoise
plt.figure(figsize=(12, 6))
plt.plot(x, t_denoise, marker='o', linewidth=2, markersize=4, color='#A23B72')
plt.title('T_denoise: Thời gian xử lý mô hình AI lọc nhiễu', fontsize=14, fontweight='bold')
plt.xlabel('Request Number', fontsize=12)
plt.ylabel('Time (ms)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('graphs/t_denoise.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Biểu đồ T_classify
plt.figure(figsize=(12, 6))
plt.plot(x, t_classify, marker='o', linewidth=2, markersize=4, color='#F18F01')
plt.title('T_classify: Thời gian xử lý mô hình Deep Learning dự đoán bệnh tim', fontsize=14, fontweight='bold')
plt.xlabel('Request Number', fontsize=12)
plt.ylabel('Time (ms)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('graphs/t_classify.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Biểu đồ T_LLM
plt.figure(figsize=(12, 6))
plt.plot(x, t_llm, marker='o', linewidth=2, markersize=4, color='#C73E1D')
plt.title('T_LLM: Thời gian xử lý mô hình LLM đưa ra giải thích', fontsize=14, fontweight='bold')
plt.xlabel('Request Number', fontsize=12)
plt.ylabel('Time (ms)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('graphs/t_llm.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. Biểu đồ T_total
plt.figure(figsize=(12, 6))
plt.plot(x, t_total, marker='o', linewidth=2, markersize=4, color='#6A994E')
plt.title('T_total: Tổng thời gian xử lý một request', fontsize=14, fontweight='bold')
plt.xlabel('Request Number', fontsize=12)
plt.ylabel('Time (ms)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('graphs/t_total.png', dpi=300, bbox_inches='tight')
plt.close()

print("✓ Đã tạo thành công 5 biểu đồ trong folder 'graphs':")
print("  - graphs/t_upload.png")
print("  - graphs/t_denoise.png")
print("  - graphs/t_classify.png")
print("  - graphs/t_llm.png")
print("  - graphs/t_total.png")

# Tính thời gian trung bình
avg_t_upload = sum(t_upload) / len(t_upload)
avg_t_denoise = sum(t_denoise) / len(t_denoise)
avg_t_classify = sum(t_classify) / len(t_classify)
avg_t_llm = sum(t_llm) / len(t_llm)
avg_t_total = sum(t_total) / len(t_total)

# Tạo dictionary chứa kết quả trung bình
average_results = {
    "T_upload_avg": round(avg_t_upload, 2),
    "T_denoise_avg": round(avg_t_denoise, 2),
    "T_classify_avg": round(avg_t_classify, 2),
    "T_LLM_avg": round(avg_t_llm, 2),
    "T_total_avg": round(avg_t_total, 2),
    "total_requests": len(data)
}

# Xuất ra file JSON
with open('average_latency_results.json', 'w', encoding='utf-8') as f:
    json.dump(average_results, f, indent=2, ensure_ascii=False)

print("\n✓ Đã tính và xuất thời gian trung bình ra file 'average_latency_results.json':")
print(f"  - T_upload trung bình: {avg_t_upload:.2f} ms")
print(f"  - T_denoise trung bình: {avg_t_denoise:.2f} ms")
print(f"  - T_classify trung bình: {avg_t_classify:.2f} ms")
print(f"  - T_LLM trung bình: {avg_t_llm:.2f} ms")
print(f"  - T_total trung bình: {avg_t_total:.2f} ms")
print(f"  - Tổng số requests: {len(data)}")
