## Báo cáo chấm thủ công (Script 2, Gemini)

Dựa trên kịch bản trong [script2/script_content.tex](script2/script_content.tex) và mẫu báo cáo/chuẩn chấm trong [script2/report_template.md](script2/report_template.md).
**Phạm vi chấm:** 10 case đầu (Case 1 - Case 10) trong folder `script2\36_cases_norag` và `script2\36_cases_rag`.

### Quy ước sử dụng khi chấm
- **JD (%):** (Số thuật ngữ chuyên ngành chưa được giải thích / Tổng số từ) × 100%.
- **HR (0/1):**
    - **1 (Có Hallucination/Thiếu nguồn):** Nếu output KHÔNG CÓ các cụm trích dẫn nguồn cụ thể như "theo...", "guideline...", "litfl...", "tài liệu y khoa...".
    - **0 (Không Hallucination/Có nguồn):** Nếu CÓ ít nhất một trích dẫn nguồn.
- **Tổng số từ:** Đếm xấp xỉ theo văn bản tiếng Việt.

---

## Kết quả chi tiết (No-RAG, Case 1–10)

| Case | Chẩn đoán (từ prompt) | Tổng từ | Jargon chưa giải thích | JD (%) | Câu "theo .../nguồn ..." | HR_case (0/1) | Ghi chú |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | Rung nhĩ (Atrial Fibrillation) | 281 | 1 | 0.36 | Không | 1 | "HRV RMSSD" chưa giải thích. |
| 2 | Rung nhĩ (Atrial Fibrillation) | 290 | 1 | 0.34 | Không | 1 | "HRV - RMSSD" chưa giải thích. |
| 3 | Rung nhĩ (Atrial Fibrillation) | 244 | 0 | 0.00 | Không | 1 | HRV được giải thích là biến thiên nhịp tim. |
| 4 | Cuồng nhĩ (Atrial Flutter) | 262 | 1 | 0.38 | Không | 1 | "HRV" chưa giải thích. |
| 5 | Cuồng nhĩ (Atrial Flutter) | 261 | 0 | 0.00 | Không | 1 | "sóng F" (răng cưa) đã diễn giải. |
| 6 | Cuồng nhĩ (Atrial Flutter) | 229 | 1 | 0.44 | Không | 1 | "sóng flutter" (tiếng Anh) chưa giải thích. |
| 7 | Nhịp chậm (Bradycardia) | 227 | 0 | 0.00 | Không | 1 | QRS được diễn giải tốt. |
| 8 | Nhịp chậm (Bradycardia) | 241 | 0 | 0.00 | Không | 1 | Không có jargon khó. |
| 9 | Nhịp chậm (Bradycardia) | 194 | 0 | 0.00 | Không | 1 | Không có jargon khó. |
| 10 | Block nhĩ thất độ I | 263 | 0 | 0.00 | Không | 1 | Khoảng PR được giải thích rõ. |

## Kết quả chi tiết (With-RAG, Case 1–10)

| Case | Chẩn đoán (từ prompt) | Tổng từ | Jargon chưa giải thích | JD (%) | Câu "theo .../nguồn ..." | HR_case (0/1) | Ghi chú |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | Rung nhĩ (Atrial Fibrillation) | 230 | 1 | 0.43 | Có | 0 | Trích dẫn "theo litfl.com". "HRV RMSSD" chưa giải thích. |
| 2 | Rung nhĩ (Atrial Fibrillation) | 300 | 1 | 0.33 | Có | 0 | Trích dẫn "Theo hướng dẫn y khoa". |
| 3 | Rung nhĩ (Atrial Fibrillation) | 272 | 0 | 0.00 | Có | 0 | Trích dẫn "theo LITFL.com". |
| 4 | Cuồng nhĩ (Atrial Flutter) | 259 | 0 | 0.00 | Có | 0 | Trích dẫn "Rev Esp Cardiol" và "LITFL". |
| 5 | Cuồng nhĩ (Atrial Flutter) | 273 | 0 | 0.00 | Không | 1 | **Lỗi:** Không tìm thấy trích dẫn nguồn dù là RAG. |
| 6 | Cuồng nhĩ (Atrial Flutter) | 262 | 0 | 0.00 | Không | 1 | **Lỗi:** Không tìm thấy trích dẫn nguồn. |
| 7 | Nhịp chậm (Bradycardia) | 250 | 0 | 0.00 | Không | 1 | **Lỗi:** Không tìm thấy trích dẫn nguồn. |
| 8 | Nhịp chậm (Bradycardia) | 213 | 0 | 0.00 | Không | 1 | **Lỗi:** Không tìm thấy trích dẫn nguồn. |
| 9 | Nhịp chậm (Bradycardia) | 247 | 0 | 0.00 | Không | 1 | **Lỗi:** Không tìm thấy trích dẫn nguồn. |
| 10 | Block nhĩ thất độ I | 270 | 0 | 0.00 | Có | 0 | Trích dẫn "Theo hướng dẫn y khoa". |

---

## Tổng hợp & Nhận xét (Gemini)

### Chỉ số thống kê (Trên 20 mẫu đánh giá)

* **Jargon Density (JD):**
    * **No-RAG:** Trung bình **0.15%**. (Rất thấp, văn phong thân thiện nhưng thiếu chi tiết kỹ thuật).
    * **With-RAG:** Trung bình **0.08%**. (Thấp, văn phong vẫn thân thiện dù có thêm thông tin chuyên môn).
* **Hallucination Rate (HR - Tỷ lệ thiếu nguồn):**
    * **No-RAG:** **10/10 (100%)**. 100% các câu trả lời đều là kiến thức nội tại của LLM, không có trích dẫn kiểm chứng.
    * **With-RAG:** **5/10 (50%)**.
        * Các Case 1, 2, 3, 4, 10 hoạt động tốt (có trích dẫn nguồn rõ ràng).
        * Các Case 5, 6 (Cuồng nhĩ) và 7, 8, 9 (Nhịp chậm) **gặp lỗi**: Pipeline RAG không chèn được thông tin nguồn vào câu trả lời, output trở về dạng generic giống No-RAG.

### Nhận xét định tính

1.  **Hiệu quả của RAG:**
    * Ở những case thành công (1-4, 10), RAG giúp câu trả lời cụ thể hơn hẳn. Ví dụ Case 1 (RAG) trích dẫn *"theo litfl.com, bình thường là 70-100 ms"*, trong khi Case 1 (No-RAG) chỉ nói chung chung.
    * RAG giúp giảm chỉ số Hallucination (từ 100% xuống 50%), tuy nhiên tỷ lệ lỗi 50% ở các case 5-9 là khá cao, cần kiểm tra lại cơ chế truy xuất (retrieval) cho các bệnh lý "Cuồng nhĩ" và "Nhịp chậm".

2.  **Độ thân thiện (Jargon Density):**
    * Cả hai pipeline đều làm rất tốt việc giải thích thuật ngữ (JD < 0.5%). Các từ như QRS, sóng P thường xuyên được diễn giải kèm theo (ví dụ: *"sóng P (sóng biểu hiện sự co bóp...)"*).

3.  **Khuyến nghị:**
    * Cần xem lại file vector database hoặc prompt template cho nhóm bệnh **Nhịp chậm (Bradycardia)** và **Cuồng nhĩ (Atrial Flutter)** vì LLM thường xuyên bỏ qua việc trích dẫn nguồn ở các nhóm này.