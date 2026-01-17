## Báo cáo chấm thủ công (Script 2, ChatGPT 5.1)

Dựa trên kịch bản trong [script2/script_content.tex](script2/script_content.tex) và mẫu báo cáo/chuẩn chấm trong [script2/report_template.md](script2/report_template.md). Phạm vi chấm: 36 case (từ case 1 đến case 36) trong [script2/36_cases_norag](script2/36_cases_norag) và [script2/36_cases_rag](script2/36_cases_rag).

### Quy ước sử dụng khi chấm
- **JD (%):** số thuật ngữ chuyên ngành chưa được giải thích / tổng số từ × 100%. Tổng số từ lấy theo bảng trong template.
- **HR (0/1):** 1 nếu output không có cụm trích dẫn/nguồn kiểu "theo ...", "guideline ...", "litfl ..."; 0 nếu có.
- **Câu "theo .../nguồn ...":** ghi "Có" nếu có ít nhất một trích dẫn nguồn; ngược lại "Không".
- **Ghi chú:** nêu ngắn gọn thuật ngữ chưa giải thích hoặc điểm đáng chú ý.


## Kết quả chi tiết (No-RAG, case 1–36)

| Case | Chẩn đoán (từ prompt) | Tổng từ | Jargon chưa giải thích | JD (%) | Câu "theo .../nguồn ..." | HR_case (0/1) | Ghi chú |
|---:|---|---:|---:|---:|---:|---:|---|
|1|Rung nhĩ (Atrial Fibrillation)|281|1| 0.36 |Không|1|"RMSSD" chưa giải thích rõ|
|2|Rung nhĩ (Atrial Fibrillation)|290|1| 0.34 |Không|1|"RMSSD" chưa giải thích rõ|
|3|Rung nhĩ (Atrial Fibrillation)|244|0| 0.0 |Không|1|Không thấy jargon chưa giải thích|
|4|Cuồng nhĩ (Atrial Flutter)|262|0| 0.0 |Không|1|Mô tả răng cưa đã giải thích khái niệm|
|5|Cuồng nhĩ (Atrial Flutter)|261|0| 0.0 |Không|1|"sóng F" được mô tả răng cưa, coi như đã giải thích|
|6|Cuồng nhĩ (Atrial Flutter)|229|1| 0.44 |Không|1|"flutter" (tiếng Anh) chưa dịch/giải thích|
|7|Nhịp chậm (Bradycardia)|227|0| 0.0 |Không|1|Không thấy jargon chưa giải thích|
|8|Nhịp chậm (Bradycardia)|241|0| 0.0 |Không|1|Không thấy jargon chưa giải thích|
|9|Nhịp chậm (Bradycardia)|194|0| 0.0 |Không|1|Không thấy jargon chưa giải thích|
|10|Block nhĩ thất độ I|263|0| 0.0 |Không|1|"khoảng PR" đã được giải thích|
|11|Block nhĩ thất độ I (First-degree Atrioventricular Block)|245|0| 0.0 |Không|1|PR, QRS đều được mô tả dễ hiểu|
|12|Block nhĩ thất độ I (First-degree Atrioventricular Block)|262|0| 0.0 |Không|1|Khoảng PR, QRS được giải thích bằng tiếng Việt|
|13|Block nhánh trái (Left Bundle Branch Block)|293|0| 0.0 |Không|1|Giải thích vì sao QRS hẹp, không thêm viết tắt khó|
|14|Block nhánh trái (Left Bundle Branch Block)|270|0| 0.0 |Không|1|Mô tả Block nhánh trái bằng ngôn ngữ phổ thông|
|15|Block nhánh trái (Left Bundle Branch Block)|212|0| 0.0 |Không|1|QRS rộng nhưng được giải thích rõ cho người đọc|
|16|Nhịp xoang bình thường (Normal Sinus Rhythm)|161|0| 0.0 |Không|1|Không thấy thuật ngữ chuyên môn khó|
|17|Nhịp xoang bình thường (Normal Sinus Rhythm)|192|0| 0.0 |Không|1|HRV được giải thích là "biến thiên nhịp tim"|
|18|Nhịp xoang bình thường (Normal Sinus Rhythm)|188|0| 0.0 |Không|1|Giải thích rõ nút xoang và QRS|
|19|Ngoại tâm thu nhĩ (Premature Atrial Contraction)|286|0| 0.0 |Không|1|Ngoại tâm thu nhĩ được mô tả dễ hiểu, không viết tắt|
|20|Ngoại tâm thu nhĩ (Premature Atrial Contraction)|254|0| 0.0 |Không|1|Mô tả các nhịp sớm theo thời điểm, không thêm jargon|
|21|Ngoại tâm thu nhĩ (Premature Atrial Contraction)|234|0| 0.0 |Không|1|Mô tả ngoại tâm thu nhĩ rõ ràng, không dùng viết tắt khó|
|22|Ngoại tâm thu thất (Premature Ventricular Contraction)|258|0| 0.0 |Không|1|Giải thích ngoại tâm thu thất bằng tiếng Việt, có ví dụ vị trí nhịp sớm|
|23|Ngoại tâm thu thất (Premature Ventricular Contraction)|240|0| 0.0 |Không|1|Mô tả nhịp sớm PVC bằng ngôn ngữ đời thường, dễ hiểu|
|24|Ngoại tâm thu thất (Premature Ventricular Contraction)|273|0| 0.0 |Không|1|Nhấn mạnh số lượng nhịp sớm và hình dạng rộng, không thêm jargon|
|25|Block nhánh phải (Right Bundle Branch Block)|261|0| 0.0 |Không|1|Giải thích rằng QRS hẹp nên chưa phù hợp chẩn đoán Block nhánh phải|
|26|Block nhánh phải (Right Bundle Branch Block)|224|0| 0.0 |Không|1|Trình bày tiêu chuẩn QRS rộng >0.12s và so sánh với QRS đo được|
|27|Block nhánh phải (Right Bundle Branch Block)|325|0| 0.0 |Không|1|Nhấn mạnh kết quả AI nhưng khẳng định QRS vẫn trong giới hạn bình thường|
|28|Chênh xuống đoạn ST (ST Depression)|238|0| 0.0 |Không|1|Mô tả đoạn ST chênh xuống và giải thích nguy cơ thiếu máu cơ tim|
|29|Chênh xuống đoạn ST (ST Depression)|227|0| 0.0 |Không|1|Giải thích cấu trúc đoạn ST và ý nghĩa thiếu máu cơ tim, không trích nguồn|
|30|Chênh xuống đoạn ST (ST Depression)|200|0| 0.0 |Không|1|Mô tả ST chênh xuống, khuyến cáo khám sớm, không có câu "theo ..."|
|31|Chênh lên đoạn ST (ST Elevation)|196|0| 0.0 |Không|1|Giải thích đoạn ST là phần sóng giữa co bóp và tái cực, không có viết tắt khó|
|32|Chênh lên đoạn ST (ST Elevation)|212|0| 0.0 |Không|1|Mô tả ST chênh lên và liên hệ nhồi máu cơ tim, không dùng thuật ngữ tiếng Anh khó|
|33|Chênh lên đoạn ST (ST Elevation)|243|0| 0.0 |Không|1|Giải thích đoạn ST và ý nghĩa thiếu máu cơ tim, không có viết tắt chưa giải thích|
|34|Nhịp nhanh (Tachycardia)|225|0| 0.0 |Không|1|"Chỉ số biến thiên nhịp tim (HRV)" được giải thích, không có RMSSD|
|35|Nhịp nhanh (Tachycardia)|186|0| 0.0 |Không|1|Mô tả nhịp nhanh và QRS bình thường bằng tiếng Việt, không có viết tắt khó|
|36|Nhịp nhanh (Tachycardia)|202|0| 0.0 |Không|1|"Chỉ số biến thiên nhịp tim (HRV)" được nêu kèm giải thích, không có RMSSD|


## Kết quả chi tiết (With-RAG, case 1–36)

| Case | Chẩn đoán (từ prompt) | Tổng từ | Jargon chưa giải thích | JD (%) | Câu "theo .../nguồn ..." | HR_case (0/1) | Ghi chú |
|---:|---|---:|---:|---:|---:|---:|---|
|1|Rung nhĩ (Atrial Fibrillation)|230|1| 0.43 |Có|0|Có trích dẫn phạm vi QRS theo LITFL; "RMSSD" chưa giải thích|
|2|Rung nhĩ (Atrial Fibrillation)|300|1| 0.33 |Có|0|Có cụm "Theo hướng dẫn y khoa"; "RMSSD" chưa giải thích|
|3|Rung nhĩ (Atrial Fibrillation)|272|0| 0.0 |Có|0|Có trích dẫn LITFL; không thấy jargon chưa giải thích|
|4|Cuồng nhĩ (Atrial Flutter)|259|0| 0.0 |Có|0|Có trích dẫn Rev Esp Cardiol và LITFL|
|5|Cuồng nhĩ (Atrial Flutter)|273|0| 0.0 |Không|1|Không thấy nguồn/citation|
|6|Cuồng nhĩ (Atrial Flutter)|262|0| 0.0 |Không|1|"ECG" đã được giải thích trong ngoặc|
|7|Nhịp chậm (Bradycardia)|250|0| 0.0 |Không|1|Không thấy nguồn/citation|
|8|Nhịp chậm (Bradycardia)|213|0| 0.0 |Không|1|Không thấy nguồn/citation|
|9|Nhịp chậm (Bradycardia)|247|0| 0.0 |Không|1|Không thấy nguồn/citation|
|10|Block nhĩ thất độ I|270|0| 0.0 |Có|0|Có cụm "Theo hướng dẫn y khoa"|
|11|Block nhĩ thất độ I (First-degree Atrioventricular Block)|309|0| 0.0 |Có|0|Có cụm "Theo hướng dẫn y khoa", không thêm viết tắt khó|
|12|Block nhĩ thất độ I (First-degree Atrioventricular Block)|280|0| 0.0 |Có|0|Nhắc "Theo hướng dẫn y khoa", PR/QRS được giải thích|
|13|Block nhánh trái (Left Bundle Branch Block)|244|0| 0.0 |Có|0|Trích dẫn LITFL, giải thích tiêu chuẩn QRS rộng|
|14|Block nhánh trái (Left Bundle Branch Block)|283|0| 0.0 |Có|0|Có câu "theo hướng dẫn y khoa" trong phần details|
|15|Block nhánh trái (Left Bundle Branch Block)|231|0| 0.0 |Có|0|Mô tả Block nhánh trái kèm dẫn chiếu hướng dẫn|
|16|Nhịp xoang bình thường (Normal Sinus Rhythm)|181|0| 0.0 |Có|0|Nêu QRS bình thường "theo hướng dẫn y khoa"|
|17|Nhịp xoang bình thường (Normal Sinus Rhythm)|191|0| 0.0 |Có|0|Có cụm "theo tài liệu y khoa LITFL"|
|18|Nhịp xoang bình thường (Normal Sinus Rhythm)|194|0| 0.0 |Có|0|Có câu "Theo tài liệu y khoa về Premature Atrial Contractions"|
|19|Ngoại tâm thu nhĩ (Premature Atrial Contraction)|296|0| 0.0 |Không|1|Không có cụm "theo ...", HRV được giải thích|
|20|Ngoại tâm thu nhĩ (Premature Atrial Contraction)|270|0| 0.0 |Không|1|Mô tả nhịp đập sớm, không nhắc nguồn|
|21|Ngoại tâm thu nhĩ (Premature Atrial Contraction)|270|0| 0.0 |Có|0|Có câu "Theo hướng dẫn y khoa về Premature Atrial Contractions", nội dung chi tiết dễ hiểu|
|22|Ngoại tâm thu thất (Premature Ventricular Contraction)|296|0| 0.0 |Có|0|Trích StatPearls khi mô tả tiêu chuẩn QRS rộng của ngoại tâm thu thất|
|23|Ngoại tâm thu thất (Premature Ventricular Contraction)|328|0| 0.0 |Có|0|Giải thích tiêu chuẩn QRS >0.12s "theo hướng dẫn y khoa", vẫn dùng lời văn dễ hiểu|
|24|Ngoại tâm thu thất (Premature Ventricular Contraction)|256|0| 0.0 |Có|0|Mô tả PVC và so sánh QRS đo được với tiêu chuẩn trong hướng dẫn y khoa|
|25|Block nhánh phải (Right Bundle Branch Block)|239|0| 0.0 |Có|0|Nêu Block nhánh phải nhưng nhấn mạnh QRS bình thường theo guideline y khoa|
|26|Block nhánh phải (Right Bundle Branch Block)|279|0| 0.0 |Có|0|Nhắc RBBB và tiêu chuẩn QRS rộng >0.12s theo hướng dẫn, không thêm viết tắt khó khác|
|27|Block nhánh phải (Right Bundle Branch Block)|273|0| 0.0 |Có|0|Có câu "theo hướng dẫn y khoa", khuyến nghị khám chuyên khoa tim mạch để xác nhận|
|28|Chênh xuống đoạn ST (ST Depression)|269|0| 0.0 |Có|0|Giải thích ST chênh xuống theo tài liệu y khoa, liên hệ đến thiếu máu cơ tim|
|29|Chênh xuống đoạn ST (ST Depression)|226|0| 0.0 |Có|0|Mô tả ST chênh xuống "theo hướng dẫn y khoa", gợi ý thiếu máu cơ tim|
|30|Chênh xuống đoạn ST (ST Depression)|266|0| 0.0 |Có|0|Trích litfl.com và giải thích "thiếu máu cơ tim cục bộ (myocardial ischaemia)" cho người đọc|
|31|Chênh lên đoạn ST (ST Elevation)|231|0| 0.0 |Có|0|Có câu "Theo hướng dẫn y khoa", giải thích STEMI bằng tiếng Việt kèm thuật ngữ tiếng Anh|
|32|Chênh lên đoạn ST (ST Elevation)|254|0| 0.0 |Có|0|Có cụm "Theo hướng dẫn y khoa", diễn giải rõ ST và thiếu máu cơ tim|
|33|Chênh lên đoạn ST (ST Elevation)|194|0| 0.0 |Không|1|Mô tả ST chênh lên và nhồi máu cơ tim, không có câu trích nguồn "theo ..."|
|34|Nhịp nhanh (Tachycardia)|252|1| 0.40 |Có|0|"RMSSD" xuất hiện trong cụm HRV RMSSD nhưng không được giải thích cụ thể|
|35|Nhịp nhanh (Tachycardia)|272|1| 0.37 |Có|0|"RMSSD" được nêu cùng HRV nhưng không có diễn giải cho người đọc phổ thông|
|36|Nhịp nhanh (Tachycardia)|256|1| 0.39 |Có|0|"RMSSD" xuất hiện như một chỉ số kỹ thuật, không được giải thích thêm|

## Tổng hợp (sẽ cập nhật sau khi chấm đủ 72 outputs)

- **JD (No-RAG):** mean 0.03%, median 0.0%
- **JD (RAG):** mean 0.05%, median 0.0%
- **HR (No-RAG, theo case):** 36/36 = 100.0%
- **HR (RAG, theo case):** 8/36 = 22.22%