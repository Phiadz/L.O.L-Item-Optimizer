# Kế Hoạch Thực Hiện — Huỳnh Gia Huy (MSSV: 079206018609)

**Vai trò:** Xây dựng dữ liệu test, Viết các phần báo cáo tổng của dự án (trừ phân tích 3 thuật toán), Thực hiện slide 1-12, Hỗ trợ kiểm thử UI

---

## 1. Tổng Quan Nhiệm Vụ

Huỳnh Gia Huy chịu trách nhiệm phần dữ liệu và phần tài liệu/slide tổng hợp của nhóm:

1. Chuẩn bị toàn bộ dữ liệu test dùng cho code và demo.
2. Viết các phần báo cáo chung của dự án (không viết 3 mục phân tích DP/Greedy/B&B).
3. Làm 12 slide mở đầu (slide 1-12).
4. Hỗ trợ test UI cùng Nguyễn Văn Vũ.

---

## 2. Nội Dung Công Việc Chi Tiết

### 2.1 Xây dựng dữ liệu test (cụ thể)

**File dữ liệu cần bàn giao:**

- `items_data.json`: bộ dữ liệu chính 50+ item.
- `test_small.json`: 5-10 item để đối chiếu bằng tay.
- `test_greedy_fail.json`: bộ dữ liệu phản ví dụ cho Greedy.
- `test_large.json`: bộ dữ liệu 100+ item để đo hiệu năng.

**Ràng buộc dữ liệu bắt buộc:**

- Không trùng tên item.
- `gold` là số nguyên dương.
- `power` là số thực dương.
- File JSON hợp lệ, mở được bằng `json.load`.

### 2.2 Viết phần báo cáo tổng của dự án

**Các mục bắt buộc do Huy viết:**

1. Giới thiệu đề tài và mục tiêu nghiên cứu.
2. Phạm vi bài toán và ánh xạ sang ngữ cảnh game LOL.
3. Kiến trúc chương trình và luồng dữ liệu.
4. Thiết kế thực nghiệm và mô tả môi trường chạy.
5. Bảng kết quả tổng hợp và nhận xét xu hướng chung.
6. Kết luận, hạn chế, hướng phát triển.

**Không viết:** phân tích chuyên sâu từng thuật toán (do Lộc, Chiến, Hưng phụ trách).

### 2.3 Thực hiện slide 1-12 (chi tiết từng slide)

**Slide 1-12 bắt buộc gồm:**

1. Slide 1: Trang bìa.
2. Slide 2: Mục lục.
3. Slide 3: Lý do chọn đề tài.
4. Slide 4: Phát biểu bài toán 0/1 Knapsack.
5. Slide 5: Ánh xạ bài toán sang LOL.
6. Slide 6: Mục tiêu và tiêu chí đánh giá.
7. Slide 7: Kiến trúc hệ thống.
8. Slide 8: Luồng dữ liệu chương trình.
9. Slide 9: Dữ liệu đầu vào và cách xây dựng dataset.
10. Slide 10: Thiết kế thực nghiệm (N, W, số lần chạy).
11. Slide 11: Phân công thành viên mới nhất.
12. Slide 12: Chuyển tiếp sang phần demo và kết quả (slide 13-24).

**Chuẩn định dạng slide:**

- Mỗi slide 1 ý chính.
- Có hình minh họa hoặc sơ đồ, hạn chế chữ dày đặc.
- Dùng cùng theme với slide 13-24.

### 2.4 Hỗ trợ kiểm thử UI

**Checklist test cần chạy:**

1. Load file dữ liệu thành công.
2. Thêm/Sửa/Xóa item không lỗi.
3. Nhập sai `max_gold` có thông báo rõ ràng.
4. Chạy đủ 3 thuật toán và hiển thị đúng kết quả.
5. Biểu đồ mở được, số liệu trùng dữ liệu kết quả.

---

## 3. Timeline

| Tuần | Công việc | Đầu ra cụ thể |
|---|---|---|
| Tuần 1 | Hoàn thiện dataset chính và dataset test chuyên biệt | Bộ dữ liệu JSON đầy đủ và hợp lệ |
| Tuần 2 | Viết phần mở đầu, phạm vi, kiến trúc trong báo cáo | Draft báo cáo phần tổng quan |
| Tuần 3 | Viết phần thực nghiệm, kết luận và làm slide 1-12 | File slide 1-12 + báo cáo gần hoàn thiện |
| Tuần 4 | Kiểm thử UI, rà soát và chốt báo cáo tổng | Bản báo cáo hoàn chỉnh để nộp |

---

## 4. Phối hợp

- Với Lê Thiên Lộc, Đỗ Đình Chiến, Hoàng Văn Hưng: nhận 3 mục phân tích thuật toán để ghép vào báo cáo tổng.
- Với Nguyễn Văn Vũ: test giao diện và đồng bộ style slide 1-12 với 13-24.
- Với cả nhóm: chốt dữ liệu thực nghiệm cuối cùng trước hạn nộp.
