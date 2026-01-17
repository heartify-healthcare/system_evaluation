
# Report đánh giá Kịch bản 2 (A/B Testing RAG)

Ngày đánh giá: 2025-12-18  
Phạm vi: 36 mẫu × 2 pipeline = 72 outputs (`36_cases_norag` và `36_cases_rag`).

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

- **Văn bản** = ghép toàn bộ các trường trong `explanation`: `summary` + `details` + `recommendations` + `next_steps`.
- **Tổng số từ**: đếm thủ công xấp xỉ theo tách từ bằng dấu cách (sai số nhỏ có thể có do đếm thủ công; dùng cùng một cách đếm cho cả 2 pipeline để so sánh công bằng).
- **Từ chuyên ngành chưa giải thích**: các viết tắt/thuật ngữ y khoa/tiếng Anh xuất hiện **mà không có diễn giải ngay gần đó** (cùng câu hoặc ngay sau trong ngoặc/định nghĩa).
	- Ví dụ **được coi là đã giải thích**: "HRV (biến thiên nhịp tim)", "tâm nhĩ (buồng tim phía trên)".
	- Ví dụ **chưa giải thích**: chỉ nêu "RMSSD", LBBB", "RBBB",... mà không diễn giải cho người dùng phổ thông.

### Hallucination Rate (HR, %)

Theo kịch bản: "tỷ lệ thông tin bịa đặt", kiểm tra đặc biệt các **trích dẫn/nguồn y khoa** có thật trong cơ sở tri thức.

**Ràng buộc thực tế khi chấm thủ công trong workspace này:** không có file "corpus/KB" để đối chiếu từng trích dẫn có tồn tại hay không. Vì vậy, mình áp dụng đúng "Lưu ý #4" của bạn: **dựa vào dấu hiệu câu chữ** như "Theo hướng dẫn y khoa", "Theo LITFL", "theo litfl.com", "theo khuyến cáo ..." để ước lượng.

**Quy ước HR dùng trong report này:**

- Một **case** được tính là "có hallucination" nếu trong output của case đó **KHÔNG** có **gán nguồn/chuẩn** kiểu "theo ...", "guideline ...", "tài liệu ...", "litfl ...".
- $$ HR = \frac{\text{Số case hallucination}}{\text{Tổng số case}} \times 100\% $$

> Lưu ý: Đây là **ước lượng theo dấu hiệu trích dẫn**, không phải kiểm chứng "đúng/sai y khoa" của toàn bộ nội dung.

## Kết quả chi tiết theo từng case

### Bảng kết quả (No-RAG)

| Case | Chẩn đoán (từ prompt) | Tổng từ | Jargon chưa giải thích | JD (%) | Câu "theo .../nguồn ..." | HR_case (0/1) | Ghi chú |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | Rung nhĩ (Atrial Fibrillation) | 281 | 1 (RMSSD) | 0.356 | 0 | 0 | Không gán nguồn; JD thấp. |
| 2 | Rung nhĩ (Atrial Fibrillation) | 290 | 1 (RMSSD) | 0.345 | 0 | 0 | Không gán nguồn; JD thấp. |
| 3 | Rung nhĩ (Atrial Fibrillation) | 244 | 0 | 0.000 | 0 | 0 | Không gán nguồn; có giải thích các thuật ngữ qua diễn giải tiếng Việt. |
| 4 | Cuồng nhĩ (Atrial Flutter) | 262 | 1 (HRV) | 0.382 | 0 | 0 | Có "HRV" nhưng không mở rộng viết tắt (dù có diễn giải ý nghĩa). |
| 5 | Cuồng nhĩ (Atrial Flutter) | 261 | 0 | 0.000 | 0 | 0 | Thuật ngữ được diễn giải; không gán nguồn. |
| 6 | Cuồng nhĩ (Atrial Flutter) | 229 | 1 (flutter) | 0.437 | 0 | 0 | Có "sóng flutter" tiếng Anh (mô tả răng cưa nhưng không giải thích thuật ngữ). |
| 7 | Nhịp chậm (Bradycardia) | 227 | 0 | 0.000 | 0 | 0 | Không gán nguồn; JD thấp. |
| 8 | Nhịp chậm (Bradycardia) | 241 | 0 | 0.000 | 0 | 0 | Không gán nguồn; JD thấp. |
| 9 | Nhịp chậm (Bradycardia) | 194 | 0 | 0.000 | 0 | 0 | Không gán nguồn; JD thấp. |
| 10 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 263 | 0 | 0.000 | 0 | 0 | Giải thích rõ sóng P/QRS/khoảng PR. |
| 11 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 245 | 0 | 0.000 | 0 | 0 | Không gán nguồn; diễn giải dễ hiểu. |
| 12 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 262 | 0 | 0.000 | 0 | 0 | Không gán nguồn; diễn giải dễ hiểu. |
| 13 | Block nhánh trái (Left Bundle Branch Block) | 293 | 1 (12 chuyển đạo) | 0.341 | 0 | 0 | Có cảnh báo "không nhất quán" với LBBB; khuyến nghị kiểm tra 12 chuyển đạo. |
| 14 | Block nhánh trái (Left Bundle Branch Block) | 270 | 0 | 0.000 | 0 | 0 | Nêu định nghĩa LBBB và so sánh với QRS 0.07s; không gán nguồn. |
| 15 | Block nhánh trái (Left Bundle Branch Block) | 212 | 0 | 0.000 | 0 | 0 | Ủng hộ LBBB dù QRS=0.112s (gần ngưỡng); không gán nguồn. |
| 16 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 161 | 0 | 0.000 | 0 | 0 | Diễn giải "nút xoang" cho người dùng; không gán nguồn. |
| 17 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 192 | 0 | 0.000 | 0 | 0 | Không gán nguồn; văn phong dễ hiểu. |
| 18 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 188 | 1 (HRV) | 0.532 | 0 | 0 | Có "HRV" không mở rộng viết tắt. |
| 19 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 286 | 0 | 0.000 | 0 | 0 | Không gán nguồn; giải thích "ngoại tâm thu nhĩ" rõ. |
| 20 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 254 | 0 | 0.000 | 0 | 0 | Nêu thời điểm nhịp sớm; không gán nguồn. |
| 21 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 234 | 0 | 0.000 | 0 | 0 | Không gán nguồn; mô tả PAC rõ ràng. |
| 22 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 258 | 0 | 0.000 | 0 | 0 | Không gán nguồn; nêu "hình dạng rộng hơn" + thời điểm quan sát. |
| 23 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 240 | 0 | 0.000 | 0 | 0 | Không gán nguồn; diễn giải "nhịp đập thừa" dễ hiểu. |
| 24 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 273 | 1 (điện giải) | 0.366 | 0 | 0 | Có nêu "mất cân bằng điện giải" nhưng không giải thích thêm. |
| 25 | Block nhánh phải (Right Bundle Branch Block) | 261 | 0 | 0.000 | 0 | 0 | Nêu "không nhất quán" vì QRS hẹp; không gán nguồn. |
| 26 | Block nhánh phải (Right Bundle Branch Block) | 224 | 0 | 0.000 | 0 | 0 | Không gán nguồn; kết luận RBBB không được xác nhận (QRS 0.076s). |
| 27 | Block nhánh phải (Right Bundle Branch Block) | 325 | 0 | 0.000 | 0 | 0 | Không gán nguồn; giải thích rõ RBBB và đối chiếu QRS bình thường. |
| 28 | Chênh xuống đoạn ST (ST Depression) | 238 | 0 | 0.000 | 0 | 0 | Giải thích ST và "thiếu máu" bằng ngôn ngữ phổ thông. |
| 29 | Chênh xuống đoạn ST (ST Depression) | 227 | 0 | 0.000 | 0 | 0 | Có liệt kê xét nghiệm gợi ý (gắng sức...); không gán nguồn. |
| 30 | Chênh xuống đoạn ST (ST Depression) | 200 | 0 | 0.000 | 0 | 0 | Không gán nguồn; diễn giải tương đối ngắn. |
| 31 | Chênh lên đoạn ST (ST Elevation) | 196 | 0 | 0.000 | 0 | 0 | Cảnh báo xử trí khẩn cấp; không gán nguồn. |
| 32 | Chênh lên đoạn ST (ST Elevation) | 212 | 0 | 0.000 | 0 | 0 | Cảnh báo khẩn cấp; không gán nguồn. |
| 33 | Chênh lên đoạn ST (ST Elevation) | 243 | 0 | 0.000 | 0 | 0 | Có giải thích ST/QRS; cảnh báo khẩn cấp; không gán nguồn. |
| 34 | Nhịp nhanh (Tachycardia) | 225 | 0 | 0.000 | 0 | 0 | Có giải thích HRV; không gán nguồn. |
| 35 | Nhịp nhanh (Tachycardia) | 186 | 2 (P, T) | 1.075 | 0 | 0 | Nhắc P/T nhưng không diễn giải; không gán nguồn. |
| 36 | Nhịp nhanh (Tachycardia) | 202 | 0 | 0.000 | 0 | 0 | Có giải thích HRV; không gán nguồn. |

### Bảng kết quả (With-RAG)

| Case | Chẩn đoán (từ prompt) | Tổng từ | Jargon chưa giải thích | JD (%) | Câu "theo .../nguồn ..." | HR_case (0/1) | Ghi chú |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | Rung nhĩ (Atrial Fibrillation) | 230 | 1 (RMSSD) | 0.435 | 1 | 1 | Có gán nguồn litfl.com cho "QRS bình thường". |
| 2 | Rung nhĩ (Atrial Fibrillation) | 300 | 1 (RMSSD) | 0.333 | 1 | 1 | Có câu "Theo hướng dẫn y khoa...". |
| 3 | Rung nhĩ (Atrial Fibrillation) | 272 | 0 | 0.000 | 1 | 1 | Có gán nguồn LITFL.com cho chuẩn QRS. |
| 4 | Cuồng nhĩ (Atrial Flutter) | 259 | 1 (Rev Esp Cardiol ref) | 0.386 | 1 | 1 | Có nêu nguồn (Rev Esp Cardiol + LITFL) nhưng không trích đoạn KB. |
| 5 | Cuồng nhĩ (Atrial Flutter) | 273 | 0 | 0.000 | 0 | 0 | Không gán nguồn; JD thấp. |
| 6 | Cuồng nhĩ (Atrial Flutter) | 262 | 0 | 0.000 | 0 | 0 | Không gán nguồn; JD thấp. |
| 7 | Nhịp chậm (Bradycardia) | 250 | 0 | 0.000 | 0 | 0 | Viết tắt "R-R" được diễn giải ngay trong câu. |
| 8 | Nhịp chậm (Bradycardia) | 213 | 0 | 0.000 | 0 | 0 | Không gán nguồn; JD thấp. |
| 9 | Nhịp chậm (Bradycardia) | 247 | 0 | 0.000 | 0 | 0 | Không gán nguồn; chi tiết dài hơn No-RAG. |
| 10 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 270 | 0 | 0.000 | 1 | 1 | Có câu "Theo hướng dẫn y khoa...". |
| 11 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 309 | 0 | 0.000 | 1 | 1 | Có câu "Theo hướng dẫn y khoa...". |
| 12 | Block nhĩ thất độ I (First-degree Atrioventricular Block) | 280 | 0 | 0.000 | 1 | 1 | Có câu "Theo hướng dẫn y khoa...". |
| 13 | Block nhánh trái (Left Bundle Branch Block) | 244 | 0 | 0.000 | 1 | 1 | Có gán "Theo hướng dẫn y khoa (LITFL) ...". |
| 14 | Block nhánh trái (Left Bundle Branch Block) | 283 | 0 | 0.000 | 1 | 1 | Có câu "Theo hướng dẫn y khoa ... (Litfl.com)". |
| 15 | Block nhánh trái (Left Bundle Branch Block) | 231 | 0 | 0.000 | 1 | 1 | Có câu "Theo hướng dẫn y khoa ...". |
| 16 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 181 | 0 | 0.000 | 1 | 1 | Có câu "theo hướng dẫn y khoa (70-100 ms)". |
| 17 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 191 | 0 | 0.000 | 1 | 1 | Có câu "theo hướng dẫn y khoa ...". |
| 18 | Nhịp xoang bình thường (Normal Sinus Rhythm) | 194 | 0 | 0.000 | 1 | 1 | Có "theo tài liệu y khoa LITFL ...". |
| 19 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 296 | 0 | 0.000 | 1 | 1 | Có câu "Theo tài liệu y khoa ...". |
| 20 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 270 | 1 (HRV) | 0.370 | 0 | 0 | Có "HRV" (không mở rộng), không gán nguồn. |
| 21 | Ngoại tâm thu nhĩ (Premature Atrial Contraction) | 270 | 1 (Premature Atrial Contractions) | 0.370 | 1 | 1 | Có câu "Theo hướng dẫn y khoa ...". |
| 22 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 296 | 0 | 0.000 | 1 | 1 | Có câu "Theo hướng dẫn y khoa ...". |
| 23 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 328 | 1 (RMSSD) | 0.305 | 1 | 1 | Có câu "Theo hướng dẫn y khoa (StatPearls) ...". |
| 24 | Ngoại tâm thu thất (Premature Ventricular Contraction) | 256 | 0 | 0.000 | 1 | 1 | Có câu "theo hướng dẫn y khoa ...". |
| 25 | Block nhánh phải (Right Bundle Branch Block) | 239 | 0 | 0.000 | 1 | 1 | Có câu "theo hướng dẫn y khoa ...". |
| 26 | Block nhánh phải (Right Bundle Branch Block) | 279 | 0 | 0.000 | 1 | 1 | Có câu "Theo hướng dẫn y khoa ...". |
| 27 | Block nhánh phải (Right Bundle Branch Block) | 273 | 1 (RBBB) | 0.366 | 1 | 1 | Có "Theo hướng dẫn y khoa ..."; có viết tắt RBBB. |
| 28 | Chênh xuống đoạn ST (ST Depression) | 269 | 0 | 0.000 | 1 | 1 | Có câu "theo các tài liệu y khoa ...". |
| 29 | Chênh xuống đoạn ST (ST Depression) | 226 | 0 | 0.000 | 1 | 1 | Có câu "theo hướng dẫn y khoa ...". |
| 30 | Chênh xuống đoạn ST (ST Depression) | 266 | 0 | 0.000 | 1 | 1 | Có nêu "litfl.com" và thuật ngữ tiếng Anh (đã kèm diễn giải). |
| 31 | Chênh lên đoạn ST (ST Elevation) | 231 | 0 | 0.000 | 1 | 1 | Có câu "Theo hướng dẫn y khoa ..."; có nhắc STEMI (đã diễn giải). |
| 32 | Chênh lên đoạn ST (ST Elevation) | 254 | 0 | 0.000 | 1 | 1 | Có câu "Theo hướng dẫn y khoa ..."; nhiều diễn giải chi tiết. |
| 33 | Chênh lên đoạn ST (ST Elevation) | 194 | 0 | 0.000 | 0 | 0 | Nội dung gần No-RAG; không gán nguồn. |
| 34 | Nhịp nhanh (Tachycardia) | 252 | 1 (RMSSD) | 0.397 | 1 | 1 | Có câu "Theo hướng dẫn y khoa ..."; nhắc HRV RMSSD không giải thích RMSSD. |
| 35 | Nhịp nhanh (Tachycardia) | 272 | 2 (P, RMSSD) | 0.735 | 1 | 1 | Có câu "Theo hướng dẫn y khoa ..."; thêm chuẩn tham chiếu QRS 70–100 ms. |
| 36 | Nhịp nhanh (Tachycardia) | 256 | 1 (RMSSD) | 0.391 | 1 | 1 | Có câu "Theo hướng dẫn y khoa ..."; nhắc HRV RMSSD không giải thích RMSSD. |

## Tổng hợp (sẽ cập nhật sau khi chấm đủ 72 outputs)

- **JD (No-RAG):** mean 0.107%, median 0.0%
- **JD (RAG):** mean 0.114%, median 0.0%
- **HR (No-RAG, theo case):** 36/36 = 100.0%
- **HR (RAG, theo case):** 29/36 = 80.56%

## Nhận xét & khuyến nghị

### Nhận xét tổng quan (Bản hiệu chỉnh)

- **Về chỉ số Jargon Density (JD):**
  - Kết quả cho thấy JD gần như không thay đổi (No-RAG: 0.107% vs. RAG: 0.114%), duy trì ở mức rất thấp.
  - **Lý giải:** Việc chỉ số này "giậm chân tại chỗ" là hợp lý vì cả hai pipeline đều sử dụng chung một cấu trúc Prompt hệ thống định hướng người dùng phổ thông. Mức tăng nhẹ ở Pipeline RAG thực chất là dấu hiệu tích cực của việc cung cấp thông tin **cụ thể hơn**, khi mô hình đưa vào các thông số kỹ thuật chính xác từ cơ sở tri thức (như "RMSSD", "ngưỡng QRS 70-100ms") thay vì chỉ nói chung chung.


- **Về Hallucination Rate (HR) – Cải thiện vượt trội:**
  - Có sự thay đổi mang tính bước ngoặt khi HR giảm mạnh từ **100% (No-RAG)** xuống chỉ còn **19.4% (RAG)**.
  - Trong Pipeline No-RAG, 100% câu trả lời đều không có nguồn dẫn, đồng nghĩa với việc mọi thông tin y khoa đều là "kiến thức đóng" của LLM và không thể kiểm chứng.
  - Trong Pipeline RAG, khoảng **80.6%** các trường hợp đã được gán nguồn cụ thể (LITFL, StatPearls, v.v.), giúp giảm thiểu tối đa rủi ro "ảo giác" và tăng độ tin cậy cho các khuyến cáo lâm sàng.


- **Về chất lượng nội dung chuyên môn:**
  - RAG đã hoàn thành mục tiêu giúp câu trả lời **giàu thông tin hơn**. Thay vì chỉ đưa ra kết luận cảm tính, Pipeline B đã cung cấp được các **chuẩn tham chiếu y khoa** cụ thể để đối chiếu với chỉ số của người dùng.
  - Việc xuất hiện các tên nguồn như "litfl.com" hay "Theo hướng dẫn y khoa" là minh chứng cho việc mô hình đang thực sự "đọc" và "trích xuất" từ cơ sở dữ liệu thay vì tự bịa đặt câu chữ.