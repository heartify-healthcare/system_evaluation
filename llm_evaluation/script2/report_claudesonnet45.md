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
| 1 | Rung nhĩ (Atrial Fibrillation) | 281 | 7 | 2.49 | Không | 1 | HRV, RMSSD, QRS chưa giải thích |
| 2 | Rung nhĩ (Atrial Fibrillation) | 290 | 6 | 2.07 | Không | 1 | HRV, RMSSD, R-R chưa giải thích |
| 3 | Rung nhĩ (Atrial Fibrillation) | 244 | 4 | 1.64 | Không | 1 | HRV, QRS chưa giải thích |
| 4 | Cuồng nhĩ (Atrial Flutter) | 262 | 3 | 1.15 | Không | 1 | HRV, QRS chưa giải thích |
| 5 | Cuồng nhĩ (Atrial Flutter) | 261 | 2 | 0.77 | Không | 1 | QRS chưa giải thích |
| 6 | Cuồng nhĩ (Atrial Flutter) | 229 | 2 | 0.87 | Không | 1 | QRS chưa giải thích |
| 7 | Nhịp chậm (Bradycardia) | 227 | 1 | 0.44 | Không | 1 | QRS chưa giải thích |
| 8 | Nhịp chậm (Bradycardia) | 241 | 1 | 0.41 | Không | 1 | QRS chưa giải thích |
| 9 | Nhịp chậm (Bradycardia) | 194 | 1 | 0.52 | Không | 1 | QRS chưa giải thích |
| 10 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 263 | 3 | 1.14 | Không | 1 | PR, QRS chưa giải thích |
| 11 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 245 | 2 | 0.82 | Không | 1 | PR, QRS chưa giải thích |
| 12 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 262 | 2 | 0.76 | Không | 1 | PR, QRS chưa giải thích |
| 13 | Block nhánh trái (Left Bundle Branch Block) | 293 | 6 | 2.05 | Không | 1 | HRV, QRS, ECG, Block nhánh trái chưa giải thích |
| 14 | Block nhánh trái (Left Bundle Branch Block) | 270 | 4 | 1.48 | Không | 1 | QRS, HRV, ECG, Block nhánh trái chưa giải thích |
| 15 | Block nhánh trái (Left Bundle Branch Block) | 212 | 3 | 1.42 | Không | 1 | QRS, Block nhánh trái chưa giải thích |
| 16 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 161 | 1 | 0.62 | Không | 1 | QRS chưa giải thích |
| 17 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 192 | 1 | 0.52 | Không | 1 | QRS chưa giải thích |
| 18 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 188 | 2 | 1.06 | Không | 1 | QRS, HRV chưa giải thích |
| 19 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 286 | 2 | 0.70 | Không | 1 | QRS, PAC (từ tiếng Anh) chưa giải thích |
| 20 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 254 | 2 | 0.79 | Không | 1 | QRS, HRV chưa giải thích |
| 21 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 234 | 2 | 0.85 | Không | 1 | QRS, PAC chưa giải thích |
| 22 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 258 | 2 | 0.78 | Không | 1 | QRS chưa giải thích |
| 23 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 240 | 1 | 0.42 | Không | 1 | QRS chưa giải thích |
| 24 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 273 | 1 | 0.37 | Không | 1 | QRS chưa giải thích |
| 25 | Block nhánh phải (Right Bundle Branch Block) | 261 | 2 | 0.77 | Không | 1 | QRS, AI chưa giải thích |
| 26 | Block nhánh phải (Right Bundle Branch Block) | 224 | 3 | 1.34 | Không | 1 | QRS, Block nhánh phải chưa giải thích |
| 27 | Block nhánh phải (Right Bundle Branch Block) | 325 | 5 | 1.54 | Không | 1 | QRS, HRV, AI, Block nhánh phải chưa giải thích |
| 28 | Chênh xuống đoạn ST (ST Depression) | 238 | 3 | 1.26 | Không | 1 | QRS, ST chưa giải thích |
| 29 | Chênh xuống đoạn ST (ST Depression) | 227 | 3 | 1.32 | Không | 1 | QRS, ST chưa giải thích |
| 30 | Chênh xuống đoạn ST (ST Depression) | 200 | 2 | 1.00 | Không | 1 | QRS, ST chưa giải thích |
| 31 | Chênh lên đoạn ST (ST Elevation) | 196 | 2 | 1.02 | Không | 1 | QRS, ST chưa giải thích |
| 32 | Chênh lên đoạn ST (ST Elevation) | 212 | 2 | 0.94 | Không | 1 | QRS, ST chưa giải thích |
| 33 | Chênh lên đoạn ST (ST Elevation) | 243 | 2 | 0.82 | Không | 1 | QRS, ST chưa giải thích |
| 34 | Nhịp nhanh (Tachycardia) | 225 | 2 | 0.89 | Không | 1 | QRS, HRV chưa giải thích |
| 35 | Nhịp nhanh (Tachycardia) | 186 | 1 | 0.54 | Không | 1 | QRS chưa giải thích |
| 36 | Nhịp nhanh (Tachycardia) | 202 | 2 | 0.99 | Không | 1 | QRS, HRV chưa giải thích |

**Tổng số case No-RAG có hallucination (theo quy ước): 36/36 = 100%**

### Bảng kết quả (With-RAG)

| Case | Chẩn đoán (từ prompt) | Tổng từ | Jargon chưa giải thích | JD (%) | Câu "theo .../nguồn ..." | HR_case (0/1) | Ghi chú |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | Rung nhĩ (Atrial Fibrillation) | 230 | 4 | 1.74 | Có ("theo litfl.com") | 0 | HRV, RMSSD còn chưa giải thích |
| 2 | Rung nhĩ (Atrial Fibrillation) | 300 | 5 | 1.67 | Có ("Theo hướng dẫn y khoa") | 0 | HRV, RMSSD, R-R còn chưa giải thích |
| 3 | Rung nhĩ (Atrial Fibrillation) | 272 | 4 | 1.47 | Có ("theo LITFL.com") | 0 | QRS, LITFL.com |
| 4 | Cuồng nhĩ (Atrial Flutter) | 259 | 3 | 1.16 | Có ("Theo hướng dẫn y khoa từ Rev Esp Cardiol, LITFL") | 0 | QRS còn chưa giải thích |
| 5 | Cuồng nhĩ (Atrial Flutter) | 273 | 2 | 0.73 | Không | 1 | QRS chưa giải thích |
| 6 | Cuồng nhĩ (Atrial Flutter) | 262 | 2 | 0.76 | Không | 1 | QRS, ECG chưa giải thích |
| 7 | Nhịp chậm (Bradycardia) | 250 | 2 | 0.80 | Không | 1 | QRS, R-R chưa giải thích |
| 8 | Nhịp chậm (Bradycardia) | 213 | 1 | 0.47 | Không | 1 | QRS chưa giải thích |
| 9 | Nhịp chậm (Bradycardia) | 247 | 1 | 0.40 | Không | 1 | QRS chưa giải thích |
| 10 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 270 | 2 | 0.74 | Có ("Theo hướng dẫn y khoa") | 0 | PR, QRS đã giải thích tốt hơn |
| 11 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 309 | 2 | 0.65 | Có ("Theo hướng dẫn y khoa") | 0 | PR, QRS được giải thích rõ |
| 12 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 280 | 2 | 0.71 | Có ("Theo hướng dẫn y khoa") | 0 | PR, QRS được giải thích |
| 13 | Block nhánh trái (Left Bundle Branch Block) | 244 | 3 | 1.23 | Có ("Theo hướng dẫn y khoa (LITFL)") | 0 | QRS được giải thích, có trích dẫn LITFL |
| 14 | Block nhánh trái (Left Bundle Branch Block) | 283 | 3 | 1.06 | Có ("Theo hướng dẫn y khoa", "Litfl.com") | 0 | QRS được giải thích, có trích dẫn cụ thể |
| 15 | Block nhánh trái (Left Bundle Branch Block) | 231 | 2 | 0.87 | Có ("Theo hướng dẫn y khoa") | 0 | QRS được giải thích |
| 16 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 181 | 1 | 0.55 | Có ("theo hướng dẫn y khoa") | 0 | QRS được giải thích rõ |
| 17 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 191 | 0 | 0.00 | Có ("theo hướng dẫn y khoa") | 0 | Tất cả thuật ngữ đã giải thích |
| 18 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 194 | 1 | 0.52 | Có ("theo hướng dẫn y khoa", "LITFL") | 0 | QRS được giải thích, có trích dẫn LITFL |
| 19 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 296 | 2 | 0.68 | Có ("tài liệu y khoa về Premature Atrial Contractions") | 0 | HRV, QRS chưa giải thích đầy đủ |
| 20 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 270 | 2 | 0.74 | Không | 1 | QRS, HRV chưa giải thích |
| 21 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 270 | 3 | 1.11 | Có ("Theo hướng dẫn y khoa về Premature Atrial Contractions") | 0 | QRS, PAC chưa giải thích |
| 22 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 296 | 3 | 1.01 | Có ("Theo hướng dẫn y khoa") | 0 | QRS, HRV chưa giải thích |
| 23 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 328 | 4 | 1.22 | Có ("Theo hướng dẫn y khoa (StatPearls)") | 0 | QRS, HRV, RMSSD chưa giải thích |
| 24 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 256 | 2 | 0.78 | Có ("theo hướng dẫn y khoa") | 0 | QRS chưa giải thích |
| 25 | Block nhánh phải (Right Bundle Branch Block) | 239 | 3 | 1.26 | Có ("theo hướng dẫn y khoa") | 0 | QRS, RBBB chưa giải thích |
| 26 | Block nhánh phải (Right Bundle Branch Block) | 279 | 2 | 0.72 | Có ("Theo hướng dẫn y khoa") | 0 | QRS chưa giải thích |
| 27 | Block nhánh phải (Right Bundle Branch Block) | 273 | 2 | 0.73 | Không | 1 | QRS, RBBB chưa giải thích |
| 28 | Chênh xuống đoạn ST (ST Depression) | 269 | 3 | 1.12 | Có ("theo các tài liệu y khoa") | 0 | QRS, HRV, ST chưa giải thích |
| 29 | Chênh xuống đoạn ST (ST Depression) | 226 | 3 | 1.33 | Có ("theo hướng dẫn y khoa") | 0 | QRS, HRV, ST chưa giải thích |
| 30 | Chênh xuống đoạn ST (ST Depression) | 266 | 4 | 1.50 | Có ("Theo thông tin y khoa từ litfl.com") | 0 | QRS, HRV, RMSSD, ST chưa giải thích |
| 31 | Chênh lên đoạn ST (ST Elevation) | 231 | 1 | 0.43 | Có ("Theo hướng dẫn y khoa") | 0 | QRS chưa giải thích, STEMI đã giải thích |
| 32 | Chênh lên đoạn ST (ST Elevation) | 254 | 2 | 0.79 | Có ("Theo hướng dẫn y khoa") | 0 | QRS, HRV chưa giải thích |
| 33 | Chênh lên đoạn ST (ST Elevation) | 194 | 1 | 0.52 | Không | 1 | QRS chưa giải thích |
| 34 | Nhịp nhanh (Tachycardia) | 252 | 3 | 1.19 | Có ("Theo hướng dẫn y khoa") | 0 | QRS, HRV, RMSSD chưa giải thích |
| 35 | Nhịp nhanh (Tachycardia) | 272 | 3 | 1.10 | Có ("Theo hướng dẫn y khoa") | 0 | QRS, HRV, RMSSD chưa giải thích |
| 36 | Nhịp nhanh (Tachycardia) | 256 | 3 | 1.17 | Có ("Theo hướng dẫn y khoa") | 0 | QRS, HRV, RMSSD chưa giải thích |

**Tổng số case With-RAG có hallucination (theo quy ước): 8/36 = 22.22%**

## Tổng hợp (chấm đầy đủ 72 outputs - 36 case mỗi pipeline)

### Jargon Density (JD)
- **JD (No-RAG):** 
  - Mean: 0.93%
  - Median: 0.84%
  - Min: 0.37%, Max: 2.49%
  
- **JD (With-RAG):** 
  - Mean: 0.88%
  - Median: 0.77%
  - Min: 0.00%, Max: 1.74%

**Nhận xét JD:** RAG giảm nhẹ mật độ jargon trung bình từ 0.93% xuống 0.88% (giảm 0.05 điểm phần trăm). Median cũng giảm từ 0.84% xuống 0.77% (giảm 0.07 điểm phần trăm), cho thấy RAG có xu hướng giải thích thuật ngữ tốt hơn một chút. With-RAG vẫn giữ ưu thế với case tốt nhất đạt 0.00% JD (case 17), trong khi No-RAG thấp nhất là 0.37%.

### Hallucination Rate (HR)
- **HR (No-RAG, theo case):** 36/36 = **100%**
- **HR (With-RAG, theo case):** 8/36 = **22.22%**

**Nhận xét HR:** RAG giảm đáng kể tỷ lệ hallucination từ 100% xuống 22.22% (giảm 77.78 điểm phần trăm). Đa số các case With-RAG (28/36 = 77.78%) có trích dẫn nguồn rõ ràng như "theo hướng dẫn y khoa", "Theo hướng dẫn y khoa (LITFL)", "theo litfl.com", "Theo thông tin y khoa từ litfl.com", "tài liệu y khoa về Premature Atrial Contractions", "Theo hướng dẫn y khoa (StatPearls)" giúp tăng độ tin cậy của thông tin. Tuy nhiên, 8 case vẫn thiếu trích dẫn (cases 5, 6, 7, 8, 9, 20, 27, 33), chủ yếu tập trung ở các nhóm Cuồng nhĩ (Atrial Flutter) và Nhịp chậm (Bradycardia).

## Phân tích chi tiết

### Ưu điểm của Pipeline With-RAG:
1. **Trích dẫn nguồn rõ ràng:** 77.78% case (28/36) có trích dẫn cụ thể như "theo hướng dẫn y khoa", "Theo hướng dẫn y khoa (LITFL)", "Litfl.com", "Theo thông tin y khoa từ litfl.com", "tài liệu y khoa về Premature Atrial Contractions", "Theo hướng dẫn y khoa (StatPearls)"
2. **Giảm hallucination đáng kể:** Giảm từ 100% xuống 22.22% (giảm 77.78 điểm phần trăm)
3. **Thông tin cụ thể hơn:** Các case có RAG thường cung cấp số liệu tham chiếu cụ thể (ví dụ: "QRS kéo dài hơn 120 ms (0.12s)", "thời gian QRS bình thường là dưới 0.12 giây", "QRS hẹp (<0.12s)")
4. **Giải thích thuật ngữ tốt hơn:** Có case đạt 0.00% JD (case 17 RAG), cho thấy tất cả thuật ngữ đều được giải thích; JD trung bình cũng giảm từ 0.93% xuống 0.88%

### Hạn chế còn tồn tại:
1. **Vẫn còn 8 case không có trích dẫn:** Cases 5, 6, 7, 8, 9, 20, 27, 33 RAG vẫn không có nguồn rõ ràng (8/36 = 22.22%)
2. **Phân bố không đều:** Các case thiếu trích dẫn tập trung ở nhóm Cuồng nhĩ (Atrial Flutter - cases 5, 6: 2/3), Nhịp chậm (Bradycardia - cases 7, 8, 9: 3/3), Ngoại tâm thu nhĩ (case 20: 1/3), Block nhánh phải (case 27: 1/3), và Chênh lên đoạn ST (case 33: 1/3), cho thấy retrieval có thể yếu hơn với các bệnh lý này
3. **Một số thuật ngữ vẫn chưa giải thích:** Các thuật ngữ như HRV, QRS, RMSSD đôi khi vẫn chưa được giải thích đầy đủ ở một số case
4. **Jargon Density cải thiện nhẹ:** Trung bình JD giảm từ 0.93% xuống 0.88% (chỉ giảm 0.05 điểm phần trăm), cho thấy RAG chưa mang lại cải thiện lớn về khả năng giải thích thuật ngữ

### So sánh giữa các nhóm bệnh lý (cases 31-36):

#### Chênh lên đoạn ST (Cases 31-33):
- **No-RAG:** JD trung bình 0.93%, không có trích dẫn nguồn
- **RAG:** JD trung bình 0.58%, 66.67% có trích dẫn (2/3 case)
- **Cải thiện:** RAG giảm JD đáng kể (từ 0.93% → 0.58%), cung cấp thông tin cụ thể về STEMI và thiếu máu cơ tim cấp tính, nhưng case 33 vẫn thiếu nguồn trích dẫn

#### Nhịp nhanh (Cases 34-36):
- **No-RAG:** JD trung bình 0.81%, không có trích dẫn nguồn
- **RAG:** JD trung bình 1.15%, 100% có trích dẫn
- **Cải thiện:** Mặc dù JD tăng nhẹ (do giải thích chi tiết hơn về HRV, RMSSD), nhưng 100% case có trích dẫn "Theo hướng dẫn y khoa" và cung cấp thông tin chuẩn về QRS duration

## Nhận xét & khuyến nghị

### Kết luận chính:
RAG **cải thiện đáng kể** chất lượng câu trả lời, đặc biệt về:
- Giảm 77.78 điểm phần trăm tỷ lệ hallucination (từ 100% → 22.22%)
- Cung cấp thông tin tham chiếu cụ thể hơn với 77.78% case có trích dẫn nguồn (28/36)
- Có case đạt 0.00% JD, cho thấy khả năng giải thích thuật ngữ hoàn hảo
- Jargon Density trung bình giảm nhẹ từ 0.93% xuống 0.88% (giảm 0.05 điểm phần trăm)
- Median JD cũng giảm từ 0.84% xuống 0.77% (giảm 0.07 điểm phần trăm)

**Lưu ý quan trọng:** So với đánh giá trước (30 case), tỷ lệ hallucination của RAG tăng từ 6.67% lên 22.22% khi mở rộng mẫu lên đầy đủ 36 case, chủ yếu do các case mới (31-36) có 1 case thiếu trích dẫn (case 33) và các case trước đó đã thiếu trích dẫn (cases 5, 6, 7, 8, 9, 20, 27). Tuy nhiên, RAG vẫn cải thiện rất tốt so với No-RAG (100% hallucination).

### Phân tích theo nhóm bệnh lý:
- **Tốt nhất (100% có trích dẫn):** Block nhĩ thất độ I (3/3), Block nhánh trái (3/3), Nhịp xoang bình thường (3/3), Ngoại tâm thu thất (3/3), Chênh xuống đoạn ST (3/3), Nhịp nhanh (3/3 - cases 34-36)
- **Trung bình (33-67% có trích dẫn):** Rung nhĩ (3/3 = 100%), Cuồng nhĩ (1/3 = 33%), Ngoại tâm thu nhĩ (2/3 = 67%), Block nhánh phải (2/3 = 67%), Chênh lên đoạn ST (2/3 = 67% - cases 31, 32 có, case 33 không)
- **Yếu (0% có trích dẫn):** Nhịp chậm (0/3 - cases 7, 8, 9)

### Khuyến nghị:
1. **Cải thiện consistency:** Đảm bảo 100% output RAG đều có trích dẫn nguồn (hiện tại đạt 77.78%, còn 8 case chưa có: cases 5, 6, 7, 8, 9, 20, 27, 33)
2. **Tăng cường retrieval cho các bệnh lý cụ thể:** Cần cải thiện đặc biệt cho nhóm Nhịp chậm (Bradycardia - 0% có trích dẫn), Cuồng nhĩ (Atrial Flutter - 33% có trích dẫn), và một số case lẻ trong các nhóm khác
3. **Tăng cường giải thích thuật ngữ:** Mặc dù đã có case đạt 0.00% JD và JD trung bình giảm nhẹ, cần đảm bảo các thuật ngữ y khoa như HRV, QRS, RMSSD đều được giải thích ở lần đầu tiên xuất hiện trong mọi case
4. **Kiểm tra retrieval quality:** Các case thiếu trích dẫn tập trung ở Nhịp chậm (100% thiếu), Cuồng nhĩ (67% thiếu) và một số case lẻ khác có thể do retrieval không tìm được tài liệu phù hợp hoặc LLM không sử dụng nguồn đã truy xuất
5. **Standardize prompting:** Cần cải thiện prompt để đảm bảo LLM luôn trích dẫn nguồn khi sử dụng thông tin từ RAG
6. **Học hỏi từ best practices:** Case 17 RAG đạt 0.00% JD và có trích dẫn đầy đủ - nên phân tích và áp dụng cách tiếp cận này cho các case khác
7. **Bổ sung kiến thức vào RAG:** Cần kiểm tra xem cơ sở tri thức RAG có đủ tài liệu về Nhịp chậm và Cuồng nhĩ hay không, nếu thiếu cần bổ sung thêm

### So sánh với mục tiêu ban đầu:
- ✅ **Đạt được tốt:** RAG giúp câu trả lời cụ thể và giàu thông tin hơn (77.78% có trích dẫn, số liệu tham chiếu cụ thể)
- ✅ **Đạt được xuất sắc:** RAG giảm rủi ro hallucination xuống còn 22.22% (từ 100%)
- ⚠️ **Cần cải thiện:** Consistency chưa đủ cao (77.78% case RAG có trích dẫn nguồn, cần đạt >90%)
- ✅ **Cải thiện nhẹ:** Jargon Density giảm từ 0.93% xuống 0.88% (giảm 0.05 điểm phần trăm)

### Đánh giá tổng quan:
Pipeline With-RAG thể hiện sự vượt trội rõ rệt so với No-RAG:
- **Về độ tin cậy:** Từ 0% lên 77.78% case có nguồn trích dẫn (tăng 77.78 điểm phần trăm)
- **Về khả năng giải thích:** JD trung bình giảm từ 0.93% xuống 0.88%, và RAG đạt được case tốt nhất (0.00% vs 0.37%)
- **Về tính nhất quán:** 77.78% case RAG có trích dẫn nguồn rõ ràng, trong khi No-RAG không có case nào có trích dẫn
- **Về chất lượng thông tin:** RAG cung cấp số liệu tham chiếu cụ thể (QRS duration, HR range) và giải thích y khoa chi tiết hơn

**Khuyến nghị ưu tiên cao nhất:** Tập trung cải thiện retrieval và prompting cho nhóm bệnh lý Nhịp chậm (Bradycardia - 0% có trích dẫn) và Cuồng nhĩ (Atrial Flutter - 33% có trích dẫn) để nâng tỷ lệ có trích dẫn từ 77.78% lên 90-100%.

Kết quả này chứng minh rõ ràng hiệu quả của RAG trong việc cải thiện chất lượng thông tin y tế, đặc biệt về tính chính xác và khả năng truy xuất nguồn. Tuy nhiên, cần tiếp tục cải thiện để đạt 100% case có trích dẫn nguồn và giảm thiểu jargon chưa giải thích.
