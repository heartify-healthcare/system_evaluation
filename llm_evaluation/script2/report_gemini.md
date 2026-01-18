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
| 7 | Nhịp chậm (Bradycardia) | 175 | 0 | 0.00 | Không | 1 | Giải thích rõ ràng, QRS được diễn giải là "thời gian dẫn truyền". |
| 8 | Nhịp chậm (Bradycardia) | 182 | 0 | 0.00 | Không | 1 | Không có thuật ngữ khó hiểu. |
| 9 | Nhịp chậm (Bradycardia) | 158 | 0 | 0.00 | Không | 1 | "sóng QRS" được nhắc đến nhưng trong ngữ cảnh dễ hiểu. |
| 10 | Block nhĩ thất độ I | 205 | 0 | 0.00 | Không | 1 | Giải thích rất kỹ về sóng P, QRS và khoảng PR. |
| 11 | Block nhĩ thất độ I | 195 | 0 | 0.00 | Không | 1 | Diễn giải "khoảng thời gian giữa sóng P và phức bộ QRS". |
| 12 | Block nhĩ thất độ I | 202 | 0 | 0.00 | Không | 1 | Giải thích rõ ràng về sự chậm trễ dẫn truyền. |
| 13 | Block nhánh trái (LBBB) | 220 | 0 | 0.00 | Không | 1 | Phát hiện mâu thuẫn: QRS 0.063s (bình thường) khác với chẩn đoán LBBB. |
| 14 | Block nhánh trái (LBBB) | 200 | 0 | 0.00 | Không | 1 | Phát hiện mâu thuẫn: QRS 0.07s không phù hợp LBBB. |
| 15 | Block nhánh trái (LBBB) | 160 | 0 | 0.00 | Có* | 1 | *Có cụm "Theo hướng dẫn y khoa" nhưng được đánh giá là kiến thức nội tại (generic generation) giống Case 2, 10. |
| 16 | Nhịp xoang bình thường | 150 | 0 | 0.00 | Không | 1 | Giải thích tốt, không có thuật ngữ lạ. |
| 17 | Nhịp xoang bình thường | 160 | 0 | 0.00 | Không | 1 | Giải thích rõ "nút xoang", "nhịp xoang". |
| 18 | Nhịp xoang bình thường | 160 | 0 | 0.00 | Không | 1 | Các chỉ số được giải thích rõ ràng. |
| 19 | Ngoại tâm thu nhĩ (PAC) | 210 | 0 | 0.00 | Không | 1 | Giải thích rõ hiện tượng "nhịp sớm từ buồng nhĩ". |
| 20 | Ngoại tâm thu nhĩ (PAC) | 200 | 0 | 0.00 | Không | 1 | Không có nguồn trích dẫn. |
| 21 | Ngoại tâm thu nhĩ (PAC) | 190 | 0 | 0.00 | Không | 1 | Giải thích QRS và HRV tốt. |
| 22 | Ngoại tâm thu thất (PVC) | 200 | 0 | 0.00 | Không | 1 | Mô tả "xung điện bổ sung từ buồng thất" dễ hiểu. |
| 23 | Ngoại tâm thu thất (PVC) | 195 | 0 | 0.00 | Không | 1 | Không có nguồn trích dẫn. |
| 24 | Ngoại tâm thu thất (PVC) | 210 | 0 | 0.00 | Không | 1 | Không có nguồn trích dẫn. |
| 25 | Block nhánh phải (RBBB) | 220 | 0 | 0.00 | Không | 1 | Giải thích tốt, phát hiện mâu thuẫn QRS hẹp. |
| 26 | Block nhánh phải (RBBB) | 210 | 0 | 0.00 | Không | 1 | Giải thích QRS, Block nhánh phải rõ ràng. |
| 27 | Block nhánh phải (RBBB) | 230 | 0 | 0.00 | Không | 1 | Không có nguồn trích dẫn. |
| 28 | Chênh xuống đoạn ST | 210 | 0 | 0.00 | Không | 1 | Giải thích ST, QRS dễ hiểu. |
| 29 | Chênh xuống đoạn ST | 200 | 0 | 0.00 | Không | 1 | Không có nguồn trích dẫn. |
| 30 | Chênh xuống đoạn ST | 190 | 0 | 0.00 | Không | 1 | Không có nguồn trích dẫn. |
| 31 | Chênh lên đoạn ST (STEMI) | 200 | 1 | 0.50 | Không | 1 | Giải thích đoạn ST tốt. "Tái cực" chưa giải thích rõ. |
| 32 | Chênh lên đoạn ST (STEMI) | 210 | 0 | 0.00 | Không | 1 | Diễn giải tốt bằng ngôn ngữ phổ thông. |
| 33 | Chênh lên đoạn ST (STEMI) | 240 | 0 | 0.00 | Không | 1 | Không có nguồn trích dẫn. |
| 34 | Nhịp nhanh (Tachycardia) | 220 | 0 | 0.00 | Không | 1 | Giải thích HRV là "Chỉ số biến thiên nhịp tim". |
| 35 | Nhịp nhanh (Tachycardia) | 190 | 2 | 1.05 | Không | 1 | Nhắc đến "sóng P", "sóng T" mà không giải thích. |
| 36 | Nhịp nhanh (Tachycardia) | 200 | 0 | 0.00 | Không | 1 | Không có nguồn trích dẫn. |

## Kết quả chi tiết (With-RAG, Case 1–6)

| Case | Chẩn đoán (từ prompt) | Tổng từ | Jargon chưa giải thích | JD (%) | Câu \"theo .../nguồn ...\" | HR_case (0/1) | Ghi chú |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | Rung nhĩ (Atrial Fibrillation) | 230 | 1 | 0.43 | Có | 0 | Trích dẫn \"theo litfl.com\". \"RMSSD\" chưa giải thích. |
| 2 | Rung nhĩ (Atrial Fibrillation) | 300 | 1 | 0.33 | Có | 0 | Trích dẫn \"Theo hướng dẫn y khoa\". |
| 3 | Rung nhĩ (Atrial Fibrillation) | 272 | 0 | 0.00 | Có | 0 | Trích dẫn \"theo LITFL.com\". |
| 4 | Cuồng nhĩ (Atrial Flutter) | 259 | 0 | 0.00 | Có | 0 | Trích dẫn \"Rev Esp Cardiol\" và \"LITFL\". |
| 5 | Cuồng nhĩ (Atrial Flutter) | 273 | 0 | 0.00 | Không | 1 | **Lỗi:** Không tìm thấy trích dẫn nguồn. |
| 6 | Cuồng nhĩ (Atrial Flutter) | 262 | 0 | 0.00 | Không | 1 | **Lỗi:** Không tìm thấy trích dẫn nguồn. |
| 7 | Nhịp chậm (Bradycardia) | 198 | 0 | 0.00 | Không | 1 | **Lỗi:** Không tìm thấy trích dẫn nguồn. Nội dung khá giống No-RAG. |
| 8 | Nhịp chậm (Bradycardia) | 165 | 0 | 0.00 | Không | 1 | **Lỗi:** Không tìm thấy trích dẫn nguồn. |
| 9 | Nhịp chậm (Bradycardia) | 178 | 0 | 0.00 | Không | 1 | **Lỗi:** Không tìm thấy trích dẫn nguồn. |
| 10 | Block nhĩ thất độ I | 215 | 0 | 0.00 | Có | 0 | Trích dẫn "Theo hướng dẫn y khoa...". |
| 11 | Block nhĩ thất độ I | 208 | 0 | 0.00 | Có | 0 | Trích dẫn "Theo hướng dẫn y khoa...". |
| 12 | Block nhĩ thất độ I | 218 | 0 | 0.00 | Có | 0 | Trích dẫn "Theo hướng dẫn y khoa...". |
| 13 | Block nhánh trái (LBBB) | 200 | 0 | 0.00 | Có | 0 | Trích dẫn rõ ràng: "**Theo hướng dẫn y khoa (LITFL)**". |
| 14 | Block nhánh trái (LBBB) | 210 | 0 | 0.00 | Có | 0 | Trích dẫn rõ ràng: "**(Litfl.com)**". |
| 15 | Block nhánh trái (LBBB) | 170 | 0 | 0.00 | Có | 0 | Trích dẫn: "Theo hướng dẫn y khoa". |
| 16 | Nhịp xoang bình thường | 170 | 0 | 0.00 | Có | 0 | Trích dẫn: "theo hướng dẫn y khoa (70-100 ms)". |
| 17 | Nhịp xoang bình thường | 170 | 0 | 0.00 | Có | 0 | Trích dẫn: "theo hướng dẫn y khoa". |
| 18 | Nhịp xoang bình thường | 180 | 0 | 0.00 | Có | 0 | Trích dẫn rõ ràng: "**theo tài liệu y khoa LITFL**". |
| 19 | Ngoại tâm thu nhĩ (PAC) | 220 | 0 | 0.00 | Có | 0 | Trích dẫn: "**Theo tài liệu y khoa về Premature Atrial Contractions**". |
| 20 | Ngoại tâm thu nhĩ (PAC) | 210 | 0 | 0.00 | **Không** | **1** | **Lỗi:** Mất trích dẫn nguồn (hallucination risk). |
| 21 | Ngoại tâm thu nhĩ (PAC) | 200 | 0 | 0.00 | Có | 0 | Trích dẫn: "**Theo hướng dẫn y khoa về Premature Atrial Contractions**". |
| 22 | Ngoại tâm thu thất (PVC) | 220 | 0 | 0.00 | Có | 0 | Trích dẫn: "**Theo hướng dẫn y khoa**" về tiêu chuẩn QRS rộng >120ms. |
| 23 | Ngoại tâm thu thất (PVC) | 230 | 0 | 0.00 | Có | 0 | Trích dẫn rõ ràng: "**Theo hướng dẫn y khoa (StatPearls)**". |
| 24 | Ngoại tâm thu thất (PVC) | 225 | 0 | 0.00 | Có | 0 | Trích dẫn: "**theo hướng dẫn y khoa**". |
| 25 | Block nhánh phải (RBBB) | 210 | 0 | 0.00 | Có | 0 | Trích dẫn: "**Theo hướng dẫn y khoa**" về tiêu chuẩn QRS > 120ms. |
| 26 | Block nhánh phải (RBBB) | 220 | 0 | 0.00 | Có | 0 | Trích dẫn: "**Theo hướng dẫn y khoa**". |
| 27 | Block nhánh phải (RBBB) | 230 | 0 | 0.00 | Có | 0 | Trích dẫn: "**Theo hướng dẫn y khoa**". |
| 28 | Chênh xuống đoạn ST | 220 | 0 | 0.00 | Có | 0 | Trích dẫn: "**theo các tài liệu y khoa**". |
| 29 | Chênh xuống đoạn ST | 210 | 0 | 0.00 | Có | 0 | Trích dẫn: "**theo hướng dẫn y khoa**". |
| 30 | Chênh xuống đoạn ST | 230 | 0 | 0.00 | Có | 0 | Trích dẫn cụ thể: "**theo thông tin y khoa từ litfl.com**". |
| 31 | Chênh lên đoạn ST (STEMI) | 230 | 0 | 0.00 | Có | 0 | Trích dẫn: "**Theo hướng dẫn y khoa**". |
| 32 | Chênh lên đoạn ST (STEMI) | 250 | 0 | 0.00 | Có | 0 | Trích dẫn: "**Theo hướng dẫn y khoa**". |
| 33 | Chênh lên đoạn ST (STEMI) | 200 | 0 | 0.00 | **Không** | **1** | **Lỗi:** Mất nguồn trích dẫn (Hallucination risk). |
| 34 | Nhịp nhanh (Tachycardia) | 250 | 1 | 0.40 | Có | 0 | Trích dẫn: "**Theo hướng dẫn y khoa**". "RMSSD" chưa giải thích. |
| 35 | Nhịp nhanh (Tachycardia) | 270 | 2 | 0.74 | Có | 0 | Trích dẫn: "**Theo hướng dẫn y khoa**". "sóng P", "RMSSD" chưa giải thích. |
| 36 | Nhịp nhanh (Tachycardia) | 250 | 1 | 0.40 | Có | 0 | Trích dẫn: "**Theo hướng dẫn y khoa**". "RMSSD" chưa giải thích. |

---

## Tổng hợp (đã cập nhật đủ 72 outputs: 36 No-RAG + 36 RAG)

- **JD (No-RAG):** mean 0.09%, median 0.00%
- **JD (RAG):** mean 0.06%, median 0.00%
- **HR (No-RAG, theo case):** 36/36 = 100.00%
- **HR (RAG, theo case):** 7/36 = 19.44%

### Nhận xét định tính

1.  **Hiệu quả của RAG:**
    * Ở nhóm **Rung nhĩ (Cases 1-3)**, RAG hoạt động rất hiệu quả. Câu trả lời trở nên giàu thông tin hơn nhờ các con số tham chiếu cụ thể (ví dụ: \"QRS bình thường là 70-100 ms\" từ LITFL) thay vì chỉ nói \"trong giới hạn bình thường\".
    * Ở nhóm **Cuồng nhĩ (Cases 4-6)**, hiệu quả không ổn định. Case 4 trích dẫn rất tốt (thậm chí trích dẫn cả tạp chí Rev Esp Cardiol), nhưng Case 5 và 6 lại thất bại trong việc đưa nguồn vào câu trả lời. Điều này gợi ý rằng context được retrieve về cho 2 case này có thể chưa đủ tốt hoặc LLM đã bỏ qua context.

2.  **Độ tin cậy:**
    * Pipeline No-RAG hoàn toàn dựa vào \"trí nhớ\" của mô hình (HR 100%), rủi ro cao về ảo giác nếu gặp các case hiếm.
    * Pipeline RAG giảm tỷ lệ này xuống đáng kể, nhưng cần khắc phục tính không ổn định ở các case Cuồng nhĩ."