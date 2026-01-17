Dựa trên kịch bản trong [script2/script_content.tex](script2/script_content.tex) và mẫu báo cáo/chuẩn chấm trong [script2/report_template.md](script2/report_template.md).
**Phạm vi chấm:** 12 mẫu (Case 1 - Case 6) cho mỗi pipeline trong folder `script2\36_cases_norag` và `script2\36_cases_rag`.

### Quy ước sử dụng khi chấm
- **JD (%):** (Số thuật ngữ chuyên ngành chưa được giải thích / Tổng số từ) × 100%.
- **HR (0/1):**
    - **1 (Có Hallucination/Thiếu nguồn):** Nếu output KHÔNG CÓ các cụm trích dẫn nguồn cụ thể như \"theo...\", \"guideline...\", \"litfl...\", \"tài liệu y khoa...\".
    - **0 (Không Hallucination/Có nguồn):** Nếu CÓ ít nhất một trích dẫn nguồn.
- **Tổng số từ:** Đếm xấp xỉ theo văn bản tiếng Việt.

---

## Kết quả chi tiết (No-RAG, Case 1–6)

| Case | Chẩn đoán (từ prompt) | Tổng từ | Jargon chưa giải thích | JD (%) | Câu \"theo .../nguồn ...\" | HR_case (0/1) | Ghi chú |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | Rung nhĩ (Atrial Fibrillation) | 281 | 1 | 0.36 | Không | 1 | \"RMSSD\" chưa giải thích. |
| 2 | Rung nhĩ (Atrial Fibrillation) | 290 | 1 | 0.34 | Không | 1 | \"RMSSD\" chưa giải thích. |
| 3 | Rung nhĩ (Atrial Fibrillation) | 244 | 0 | 0.00 | Không | 1 | HRV được giải thích là \"biến thiên nhịp tim\". |
| 4 | Cuồng nhĩ (Atrial Flutter) | 262 | 1 | 0.38 | Không | 1 | \"HRV\" (chỉ số HRV cao) chưa giải thích. |
| 5 | Cuồng nhĩ (Atrial Flutter) | 261 | 0 | 0.00 | Không | 1 | \"sóng F\" (răng cưa) đã diễn giải. |
| 6 | Cuồng nhĩ (Atrial Flutter) | 229 | 1 | 0.44 | Không | 1 | \"sóng flutter\" (tiếng Anh) chưa giải thích rõ. |

## Kết quả chi tiết (With-RAG, Case 1–6)

| Case | Chẩn đoán (từ prompt) | Tổng từ | Jargon chưa giải thích | JD (%) | Câu \"theo .../nguồn ...\" | HR_case (0/1) | Ghi chú |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | Rung nhĩ (Atrial Fibrillation) | 230 | 1 | 0.43 | Có | 0 | Trích dẫn \"theo litfl.com\". \"RMSSD\" chưa giải thích. |
| 2 | Rung nhĩ (Atrial Fibrillation) | 300 | 1 | 0.33 | Có | 0 | Trích dẫn \"Theo hướng dẫn y khoa\". |
| 3 | Rung nhĩ (Atrial Fibrillation) | 272 | 0 | 0.00 | Có | 0 | Trích dẫn \"theo LITFL.com\". |
| 4 | Cuồng nhĩ (Atrial Flutter) | 259 | 0 | 0.00 | Có | 0 | Trích dẫn \"Rev Esp Cardiol\" và \"LITFL\". |
| 5 | Cuồng nhĩ (Atrial Flutter) | 273 | 0 | 0.00 | Không | 1 | **Lỗi:** Không tìm thấy trích dẫn nguồn. |
| 6 | Cuồng nhĩ (Atrial Flutter) | 262 | 0 | 0.00 | Không | 1 | **Lỗi:** Không tìm thấy trích dẫn nguồn. |

---

## Tổng hợp & Nhận xét (Gemini)

### Chỉ số thống kê (Trên 12 mẫu đánh giá: 6 No-RAG, 6 RAG)

* **Jargon Density (JD):**
    * **No-RAG:** Trung bình **0.25%**.
    * **With-RAG:** Trung bình **0.13%**.
    * *Nhận xét:* Pipeline RAG có xu hướng giải thích thuật ngữ tốt hơn một chút hoặc dùng từ ngữ chuẩn xác hơn, mặc dù sự khác biệt về mật độ jargon là không quá lớn.

* **Hallucination Rate (HR - Tỷ lệ thiếu nguồn):**
    * **No-RAG:** **6/6 (100%)**. 100% các câu trả lời đều là kiến thức nội tại của LLM, hoàn toàn không có trích dẫn kiểm chứng.
    * **With-RAG:** **2/6 (33.3%)**.
        * Các Case 1, 2, 3, 4 (Rung nhĩ và 1 case Cuồng nhĩ) hoạt động tốt, có trích dẫn nguồn cụ thể (LITFL, Rev Esp Cardiol).
        * Các Case 5, 6 (Cuồng nhĩ) **gặp lỗi**: Output không chứa thông tin nguồn, nội dung quay về dạng generic như No-RAG.

### Nhận xét định tính

1.  **Hiệu quả của RAG:**
    * Ở nhóm **Rung nhĩ (Cases 1-3)**, RAG hoạt động rất hiệu quả. Câu trả lời trở nên giàu thông tin hơn nhờ các con số tham chiếu cụ thể (ví dụ: \"QRS bình thường là 70-100 ms\" từ LITFL) thay vì chỉ nói \"trong giới hạn bình thường\".
    * Ở nhóm **Cuồng nhĩ (Cases 4-6)**, hiệu quả không ổn định. Case 4 trích dẫn rất tốt (thậm chí trích dẫn cả tạp chí Rev Esp Cardiol), nhưng Case 5 và 6 lại thất bại trong việc đưa nguồn vào câu trả lời. Điều này gợi ý rằng context được retrieve về cho 2 case này có thể chưa đủ tốt hoặc LLM đã bỏ qua context.

2.  **Độ tin cậy:**
    * Pipeline No-RAG hoàn toàn dựa vào \"trí nhớ\" của mô hình (HR 100%), rủi ro cao về ảo giác nếu gặp các case hiếm.
    * Pipeline RAG giảm tỷ lệ này xuống đáng kể, nhưng cần khắc phục tính không ổn định ở các case Cuồng nhĩ."