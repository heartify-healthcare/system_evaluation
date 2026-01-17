## Báo cáo chấm thủ công 20 mẫu (Script 2)

Dựa trên kịch bản trong [script2/script_content.tex](script2/script_content.tex) và mẫu báo cáo/chuẩn chấm trong [script2/report_template.md](script2/report_template.md). Phạm vi chấm: 10 case đầu trong [script2/36_cases_norag](script2/36_cases_norag) và 10 case đầu trong [script2/36_cases_rag](script2/36_cases_rag).

### Quy ước sử dụng khi chấm
- **JD (%):** số thuật ngữ chuyên ngành chưa được giải thích / tổng số từ x 100%. Tổng số từ lấy theo bảng trong template.
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
|11|Block nhĩ thất độ I (First-degree Atrioventricular Block)|245|0| 0.0 |Không|1|P/QRS đã được diễn giải trong ngữ cảnh|
|12|Block nhĩ thất độ I (First-degree Atrioventricular Block)|262|1| 0.38 |Không|1|"khoảng PR" nêu nhưng chưa giải thích|
|13|Block nhánh trái (Left Bundle Branch Block)|293|0| 0.0 |Không|1|Mâu thuẫn chẩn đoán (QRS hẹp, không phù hợp LBBB)|
|14|Block nhánh trái (Left Bundle Branch Block)|270|0| 0.0 |Không|1|QRS hẹp, khuyến nghị đi khám xác nhận|
|15|Block nhánh trái (Left Bundle Branch Block)|212|0| 0.0 |Không|1|QRS rộng 0.112s phù hợp LBBB|
|16|Nhịp xoang bình thường (Normal Sinus Rhythm)|161|0| 0.0 |Không|1|Nhịp xoang, QRS bình thường|
|17|Nhịp xoang bình thường (Normal Sinus Rhythm)|192|0| 0.0 |Không|1|Nhịp xoang, QRS bình thường|
|18|Nhịp xoang bình thường (Normal Sinus Rhythm)|188|0| 0.0 |Không|1|Có diễn giải HRV trong câu|
|19|Ngoại tâm thu nhĩ (Premature Atrial Contraction)|286|0| 0.0 |Không|1|Mô tả PAC lành tính, các chỉ số ổn|
|20|Ngoại tâm thu nhĩ (Premature Atrial Contraction)|254|0| 0.0 |Không|1|PAC, QRS bình thường|
|21|Ngoại tâm thu nhĩ (Premature Atrial Contraction)|234|1| 0.43 |Không|1|"QRS" dùng ký hiệu, không mở rộng|
|22|Ngoại tâm thu thất (Premature Ventricular Contraction)|258|2| 0.78 |Không|1|"nút xoang chủ nhịp", "QRS" chưa giải thích|
|23|Ngoại tâm thu thất (Premature Ventricular Contraction)|240|2| 0.83 |Không|1|"RMSSD", "QRS" chưa giải thích|
|24|Ngoại tâm thu thất (Premature Ventricular Contraction)|273|1| 0.37 |Không|1|"QRS" chưa giải thích|
|25|Block nhánh phải (Right Bundle Branch Block)|261|1| 0.38 |Không|1|"QRS" chưa giải thích; QRS hẹp, không điển hình RBBB|
|26|Block nhánh phải (Right Bundle Branch Block)|224|1| 0.45 |Không|1|"QRS" chưa giải thích|
|27|Block nhánh phải (Right Bundle Branch Block)|325|2| 0.62 |Không|1|"HRV RMSSD", "QRS" chưa giải thích|
|28|Chênh xuống đoạn ST (ST Depression)|238|1| 0.42 |Không|1|"QRS" chưa giải thích; ST đã được mô tả|
|29|Chênh xuống đoạn ST (ST Depression)|227|1| 0.44 |Không|1|"QRS" chưa giải thích|
|30|Chênh xuống đoạn ST (ST Depression)|200|1| 0.5 |Không|1|"QRS" chưa giải thích|
|31|Chênh lên đoạn ST (ST Elevation)|196|1| 0.51 |Không|1|"QRS" chưa giải thích; ST đã được mô tả trong ngoặc|
|32|Chênh lên đoạn ST (ST Elevation)|212|1| 0.47 |Không|1|"QRS" chưa giải thích; ST và "nhồi máu cơ tim" có diễn giải|
|33|Chênh lên đoạn ST (ST Elevation)|243|1| 0.41 |Không|1|"QRS" chưa giải thích; ST đã được diễn giải|
|34|Nhịp nhanh (Tachycardia)|225|1| 0.44 |Không|1|"QRS" chưa giải thích; HRV đã được diễn giải|
|35|Nhịp nhanh (Tachycardia)|186|1| 0.54 |Không|1|"QRS" chưa giải thích|
|36|Nhịp nhanh (Tachycardia)|202|1| 0.5 |Không|1|"QRS" chưa giải thích; HRV đã được diễn giải|

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
|11|Block nhĩ thất độ I (First-degree Atrioventricular Block)|309|2| 0.65 |Có|0|Có cụm "Theo hướng dẫn y khoa"; PR, QRS chưa giải thích|
|12|Block nhĩ thất độ I (First-degree Atrioventricular Block)|280|2| 0.71 |Có|0|Có cụm "Theo hướng dẫn y khoa"; PR, QRS chưa giải thích|
|13|Block nhánh trái (Left Bundle Branch Block)|244|1| 0.41 |Có|0|Có trích dẫn LITFL; QRS chưa giải thích|
|14|Block nhánh trái (Left Bundle Branch Block)|283|1| 0.35 |Có|0|Có trích dẫn Litfl.com; QRS chưa giải thích|
|15|Block nhánh trái (Left Bundle Branch Block)|231|1| 0.43 |Có|0|Có cụm "Theo hướng dẫn y khoa"; QRS chưa giải thích|
|16|Nhịp xoang bình thường (Normal Sinus Rhythm)|181|1| 0.55 |Có|0|Có cụm "theo hướng dẫn y khoa" về QRS; QRS chưa giải thích|
|17|Nhịp xoang bình thường (Normal Sinus Rhythm)|191|1| 0.52 |Có|0|Có cụm "theo hướng dẫn y khoa"; QRS chưa giải thích|
|18|Nhịp xoang bình thường (Normal Sinus Rhythm)|194|1| 0.52 |Có|0|Có trích dẫn LITFL; QRS chưa giải thích|
|19|Ngoại tâm thu nhĩ (Premature Atrial Contraction)|296|1| 0.34 |Có|0|Có cụm "Theo tài liệu y khoa" về PAC; QRS chưa giải thích|
|20|Ngoại tâm thu nhĩ (Premature Atrial Contraction)|270|2| 0.74 |Không|1|Không thấy nguồn/citation; QRS, HRV chưa giải thích rõ|
|21|Ngoại tâm thu nhĩ (Premature Atrial Contraction)|270|1| 0.37 |Có|0|Có cụm "Theo hướng dẫn y khoa"; "QRS" chưa giải thích|
|22|Ngoại tâm thu thất (Premature Ventricular Contraction)|296|1| 0.34 |Có|0|Có cụm "Theo hướng dẫn y khoa"; "QRS" chưa giải thích|
|23|Ngoại tâm thu thất (Premature Ventricular Contraction)|328|2| 0.61 |Có|0|Có trích dẫn (StatPearls); "RMSSD", "QRS" chưa giải thích|
|24|Ngoại tâm thu thất (Premature Ventricular Contraction)|256|1| 0.39 |Có|0|Có cụm "Theo hướng dẫn y khoa"; "QRS" chưa giải thích|
|25|Block nhánh phải (Right Bundle Branch Block)|239|1| 0.42 |Có|0|Có cụm "Theo hướng dẫn y khoa"; "QRS" chưa giải thích|
|26|Block nhánh phải (Right Bundle Branch Block)|279|1| 0.36 |Có|0|Có cụm "Theo hướng dẫn y khoa"; "QRS" chưa giải thích|
|27|Block nhánh phải (Right Bundle Branch Block)|273|1| 0.37 |Có|0|Có cụm "Theo hướng dẫn y khoa"; "QRS" chưa giải thích|
|28|Chênh xuống đoạn ST (ST Depression)|269|2| 0.74 |Có|0|Có trích dẫn litfl.com; "myocardial ischaemia" chưa dịch; "QRS" chưa giải thích|
|29|Chênh xuống đoạn ST (ST Depression)|226|1| 0.44 |Có|0|Có cụm "Theo hướng dẫn y khoa"; "QRS" chưa giải thích|
|30|Chênh xuống đoạn ST (ST Depression)|266|2| 0.75 |Có|0|Có trích dẫn litfl.com; "myocardial ischaemia" chưa dịch; "QRS" chưa giải thích|
|31|Chênh lên đoạn ST (ST Elevation)|231|1| 0.43 |Có|0|Có cụm "Theo hướng dẫn y khoa"; "QRS" chưa giải thích; STEMI đã mở rộng|
|32|Chênh lên đoạn ST (ST Elevation)|254|1| 0.39 |Có|0|Có cụm "Theo hướng dẫn y khoa"; "QRS" chưa giải thích; HRV đã giải thích|
|33|Chênh lên đoạn ST (ST Elevation)|194|0| 0.0 |Không|1|Không thấy nguồn/citation; ST đã được diễn giải, không thấy acronym chưa giải thích|
|34|Nhịp nhanh (Tachycardia)|252|2| 0.79 |Có|0|Có cụm "Theo hướng dẫn y khoa"; "QRS" và "RMSSD" chưa giải thích|
|35|Nhịp nhanh (Tachycardia)|272|2| 0.74 |Có|0|Có cụm "Theo hướng dẫn y khoa"; "QRS" và "RMSSD" chưa giải thích|
|36|Nhịp nhanh (Tachycardia)|256|2| 0.78 |Có|0|Có cụm "Theo hướng dẫn y khoa"; "QRS" và "RMSSD" chưa giải thích|

---

## Tổng hợp (sẽ cập nhật sau khi chấm đủ 72 outputs)

- **JD (No-RAG):** mean 0.27%, median 0.36%
- **JD (RAG):** mean 0.39%, median 0.4%
- **HR (No-RAG, theo case):** 36/36 = 100.0%
- **HR (RAG, theo case):** 29/36 = 80.56% (có trích dẫn nguồn)