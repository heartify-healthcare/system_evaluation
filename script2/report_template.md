## Mục tiêu & thiết kế thí nghiệm

- **Mục tiêu:** kiểm chứng bằng số liệu rằng **RAG** giúp câu trả lời **cụ thể/giàu thông tin hơn** và **giảm rủi ro** (đặc biệt là trích dẫn/nguồn không chắc chắn) so với LLM thuần.
- **Thiết kế:** cùng một đầu vào (từ mô hình Deep Learning trong trường `prompt`) chạy qua:
	- **Pipeline A (No-RAG):** chỉ LLM.
	- **Pipeline B (With-RAG):** LLM + truy xuất kiến thức.

## Chỉ số & quy ước chấm thủ công

### Jargon Density (JD, %)

Theo kịch bản:

$$ JD = \frac{\text{Số từ chuyên ngành chưa giải thích}}{\text{Tổng số từ trong văn bản}} \times 100\% $$

**Quy ước đếm thủ công (để nhất quán):**

- **Tổng số từ**: Đã đếm sẵn và được điền vào bảng.
- **Từ chuyên ngành chưa giải thích**: các viết tắt/thuật ngữ y khoa/tiếng Anh xuất hiện **mà không có diễn giải ngay gần đó** (cùng câu hoặc ngay sau trong ngoặc/định nghĩa).
	- Ví dụ **được coi là đã giải thích**: "HRV (biến thiên nhịp tim)", "tâm nhĩ (buồng tim phía trên)".
	- Ví dụ **chưa giải thích**: chỉ nêu "RMSSD", LBBB", "RBBB",... mà không diễn giải cho người dùng phổ thông.

### Hallucination Rate (HR, %)

Theo kịch bản: "tỷ lệ thông tin bịa đặt", kiểm tra đặc biệt các **trích dẫn/nguồn y khoa** có thật trong cơ sở tri thức RAG.

**Ràng buộc thực tế khi chấm thủ công trong workspace này:** Dựa vào dấu hiệu câu chữ như "Theo hướng dẫn y khoa", "Theo LITFL", "theo litfl.com", "theo khuyến cáo ..." để ước lượng.

**Quy ước HR dùng trong report này:**

- Một **case** được tính là "có hallucination" nếu trong output của case đó **KHÔNG** có **gán nguồn/chuẩn** kiểu "theo ...", "guideline ...", "tài liệu ...", "litfl ...".
- $$ HR = \frac{\text{Số case hallucination}}{\text{Tổng số case}} \times 100\% $$

> Lưu ý: Đây là **ước lượng theo dấu hiệu trích dẫn**, không phải kiểm chứng "đúng/sai y khoa" của toàn bộ nội dung.

## Kết quả chi tiết theo từng case

### Bảng kết quả (No-RAG)

| Case | Chẩn đoán (từ prompt) | Tổng từ | Jargon chưa giải thích | JD (%) | Câu "theo .../nguồn ..." | HR_case (0/1) | Ghi chú |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | Rung nhĩ (Atrial Fibrillation) | 281 | ... | ... | ... | ... | ... |
| 2 | Rung nhĩ (Atrial Fibrillation) | 290 | ... | ... | ... | ... | ... |
| 3 | Rung nhĩ (Atrial Fibrillation) | 244 | ... | ... | ... | ... | ... |
| 4 | Cuồng nhĩ (Atrial Flutter) | 262 | ... | ... | ... | ... | ... |
| 5 | Cuồng nhĩ (Atrial Flutter) | 261 | ... | ... | ... | ... | ... |
| 6 | Cuồng nhĩ (Atrial Flutter) | 229 | ... | ... | ... | ... | ... |
| 7 | Nhịp chậm (Bradycardia) | 227 | ... | ... | ... | ... | ... |
| 8 | Nhịp chậm (Bradycardia) | 241 | ... | ... | ... | ... | ... |
| 9 | Nhịp chậm (Bradycardia) | 194 | ... | ... | ... | ... | ... |
| 10 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 263 | ... | ... | ... | ... | ... |
| 11 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 245 | ... | ... | ... | ... | ... |
| 12 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 262 | ... | ... | ... | ... | ... |
| 13 | Block nhánh trái (Left Bundle Branch Block) | 293 | ... | ... | ... | ... | ... |
| 14 | Block nhánh trái (Left Bundle Branch Block) | 270 | ... | ... | ... | ... | ... |
| 15 | Block nhánh trái (Left Bundle Branch Block) | 212 | ... | ... | ... | ... | ... |
| 16 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 161 | ... | ... | ... | ... | ... |
| 17 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 192 | ... | ... | ... | ... | ... |
| 18 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 188 | ... | ... | ... | ... | ... |
| 19 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 286 | ... | ... | ... | ... | ... |
| 20 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 254 | ... | ... | ... | ... | ... |
| 21 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 234 | ... | ... | ... | ... | ... |
| 22 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 258 | ... | ... | ... | ... | ... |
| 23 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 240 | ... | ... | ... | ... | ... |
| 24 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 273 | ... | ... | ... | ... | ... |
| 25 | Block nhánh phải (Right Bundle Branch Block) | 261 | ... | ... | ... | ... | ... |
| 26 | Block nhánh phải (Right Bundle Branch Block) | 224 | ... | ... | ... | ... | ... |
| 27 | Block nhánh phải (Right Bundle Branch Block) | 325 | ... | ... | ... | ... | ... |
| 28 | Chênh xuống đoạn ST (ST Depression) | 238 | ... | ... | ... | ... | ... |
| 29 | Chênh xuống đoạn ST (ST Depression) | 227 | ... | ... | ... | ... | ... |
| 30 | Chênh xuống đoạn ST (ST Depression) | 200 | ... | ... | ... | ... | ... |
| 31 | Chênh lên đoạn ST (ST Elevation) | 196 | ... | ... | ... | ... | ... |
| 32 | Chênh lên đoạn ST (ST Elevation) | 212 | ... | ... | ... | ... | ... |
| 33 | Chênh lên đoạn ST (ST Elevation) | 243 | ... | ... | ... | ... | ... |
| 34 | Nhịp nhanh (Tachycardia) | 225 | ... | ... | ... | ... | ... |
| 35 | Nhịp nhanh (Tachycardia) | 186 | ... | ... | ... | ... | ... |
| 36 | Nhịp nhanh (Tachycardia) | 202 | ... | ... | ... | ... | ... |

### Bảng kết quả (With-RAG)

| Case | Chẩn đoán (từ prompt) | Tổng từ | Jargon chưa giải thích | JD (%) | Câu "theo .../nguồn ..." | HR_case (0/1) | Ghi chú |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | Rung nhĩ (Atrial Fibrillation) | 230 | ... | ... | ... | ... | ... |
| 2 | Rung nhĩ (Atrial Fibrillation) | 300 | ... | ... | ... | ... | ... |
| 3 | Rung nhĩ (Atrial Fibrillation) | 272 | ... | ... | ... | ... | ... |
| 4 | Cuồng nhĩ (Atrial Flutter) | 259 | ... | ... | ... | ... | ... |
| 5 | Cuồng nhĩ (Atrial Flutter) | 273 | ... | ... | ... | ... | ... |
| 6 | Cuồng nhĩ (Atrial Flutter) | 262 | ... | ... | ... | ... | ... |
| 7 | Nhịp chậm (Bradycardia) | 250 | ... | ... | ... | ... | ... |
| 8 | Nhịp chậm (Bradycardia) | 213 | ... | ... | ... | ... | ... |
| 9 | Nhịp chậm (Bradycardia) | 247 | ... | ... | ... | ... | ... |
| 10 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 270 | ... | ... | ... | ... | ... |
| 11 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 309 | ... | ... | ... | ... | ... |
| 12 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 280 | ... | ... | ... | ... | ... |
| 13 | Block nhánh trái (Left Bundle Branch Block) | 244 | ... | ... | ... | ... | ... |
| 14 | Block nhánh trái (Left Bundle Branch Block) | 283 | ... | ... | ... | ... | ... |
| 15 | Block nhánh trái (Left Bundle Branch Block) | 231 | ... | ... | ... | ... | ... |
| 16 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 181 | ... | ... | ... | ... | ... |
| 17 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 191 | ... | ... | ... | ... | ... |
| 18 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 194 | ... | ... | ... | ... | ... |
| 19 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 296 | ... | ... | ... | ... | ... |
| 20 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 270 | ... | ... | ... | ... | ... |
| 21 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 270 | ... | ... | ... | ... | ... |
| 22 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 296 | ... | ... | ... | ... | ... |
| 23 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 328 | ... | ... | ... | ... | ... |
| 24 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 256 | ... | ... | ... | ... | ... |
| 25 | Block nhánh phải (Right Bundle Branch Block) | 239 | ... | ... | ... | ... | ... |
| 26 | Block nhánh phải (Right Bundle Branch Block) | 279 | ... | ... | ... | ... | ... |
| 27 | Block nhánh phải (Right Bundle Branch Block) | 273 | ... | ... | ... | ... | ... |
| 28 | Chênh xuống đoạn ST (ST Depression) | 269 | ... | ... | ... | ... | ... |
| 29 | Chênh xuống đoạn ST (ST Depression) | 226 | ... | ... | ... | ... | ... |
| 30 | Chênh xuống đoạn ST (ST Depression) | 266 | ... | ... | ... | ... | ... |
| 31 | Chênh lên đoạn ST (ST Elevation) | 231 | ... | ... | ... | ... | ... |
| 32 | Chênh lên đoạn ST (ST Elevation) | 254 | ... | ... | ... | ... | ... |
| 33 | Chênh lên đoạn ST (ST Elevation) | 194 | ... | ... | ... | ... | ... |
| 34 | Nhịp nhanh (Tachycardia) | 252 | ... | ... | ... | ... | ... |
| 35 | Nhịp nhanh (Tachycardia) | 272 | ... | ... | ... | ... | ... |
| 36 | Nhịp nhanh (Tachycardia) | 256 | ... | ... | ... | ... | ... |

## Tổng hợp (sẽ cập nhật sau khi chấm đủ 72 outputs)

- **JD (No-RAG):** mean ...%, median ...%
- **JD (RAG):** mean ...%, median ...%
- **HR (No-RAG, theo case):** .../36 = ...%
- **HR (RAG, theo case):** .../36 = ...%

## Nhận xét & khuyến nghị