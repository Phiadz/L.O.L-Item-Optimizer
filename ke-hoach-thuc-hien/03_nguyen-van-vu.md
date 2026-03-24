# Kế Hoạch Thực Hiện — Nguyễn Văn Vũ (MSSV: 077206001635)

**Vai trò:** Thiết kế giao diện UI/UX (Tkinter), Thực hiện slide thuyết trình phần 13-24

---

## 1. Tổng Quan Nhiệm Vụ

Nguyễn Văn Vũ phụ trách phần trải nghiệm người dùng và thuyết trình nửa sau:

1. Viết code giao diện chạy được end-to-end với 3 thuật toán.
2. Chuẩn bị bộ slide 13-24 bám theo dữ liệu chạy thực tế của chương trình.

---

## 2. Nội Dung Công Việc Chi Tiết

### 2.1 Viết code UI chính trong `ui/main_window.py`

**Bố cục bắt buộc có:**

- Panel trái: danh sách item (`TreeView` cột Name, Gold, Power, Ratio).
- Panel phải trên: nhập `max_gold`, chọn thuật toán (DP/Greedy/B&B), nút chạy.
- Panel phải dưới: hiển thị kết quả theo tab từng thuật toán.

**Chức năng bắt buộc phải code:**

1. Load dữ liệu từ JSON.
2. Thêm/Sửa/Xóa item trên UI.
3. Chạy thuật toán theo checkbox đã chọn.
4. Hiển thị `selected_items`, `total_power`, `gold_used`, `gold_remaining`, `exec_time_ms`.

### 2.2 Kết nối thuật toán với UI (mức code)

**Khung gọi hàm bắt buộc:**

```python
if run_dp:
	results["DP"] = dp_solve(items, max_gold)
if run_greedy:
	results["Greedy"] = greedy_solve(items, max_gold)
if run_bnb:
	results["B&B"] = bnb_solve(items, max_gold)
```

**Validation bắt buộc:**

- Không cho chạy khi chưa có dữ liệu item.
- `max_gold` phải là số nguyên dương.
- Bắt và hiển thị lỗi bằng `messagebox.showerror`.

### 2.3 Hiển thị biểu đồ so sánh

**Yêu cầu:**

- Dùng `matplotlib` vẽ 2 biểu đồ cột:
  1. Thời gian chạy theo thuật toán.
  2. Tổng sức mạnh theo thuật toán.
- Có nhãn giá trị trên cột.
- Có nút mở biểu đồ từ giao diện chính.

### 2.4 Thực hiện slide 13-24 (cụ thể từng slide)

**Slide 13-24 đề xuất bắt buộc:**

1. Slide 13: Tổng quan kiến trúc giao diện.
2. Slide 14: Luồng thao tác người dùng (Load -> Nhập vàng -> Chạy).
3. Slide 15: Màn hình quản lý item.
4. Slide 16: Màn hình kết quả theo tab thuật toán.
5. Slide 17: Biểu đồ so sánh runtime.
6. Slide 18: Biểu đồ so sánh total power.
7. Slide 19: Demo case 1 (dữ liệu nhỏ, dễ hiểu).
8. Slide 20: Demo case 2 (dữ liệu lớn, thấy khác biệt tốc độ).
9. Slide 21: So sánh kết quả DP vs Greedy vs B&B.
10. Slide 22: Vấn đề gặp phải khi tích hợp và cách xử lý.
11. Slide 23: Tổng kết phần triển khai sản phẩm.
12. Slide 24: Chuyển tiếp sang phần hỏi đáp/kết luận nhóm.

**Chuẩn slide cần tuân thủ:**

- Mỗi slide không quá 6 gạch đầu dòng.
- Có ảnh chụp màn hình thật từ chương trình.
- Thống nhất template với slide 1-12 do Huỳnh Gia Huy làm.

---

## 3. Timeline

| Tuần | Công việc | Đầu ra cụ thể |
|---|---|---|
| Tuần 1 | Chốt wireframe và luồng UI | Sơ đồ màn hình + danh sách widget |
| Tuần 2 | Code các chức năng chính của giao diện | UI thao tác được với dữ liệu thật |
| Tuần 3 | Tích hợp 3 thuật toán và biểu đồ | Kết quả và chart hiển thị đúng |
| Tuần 4 | Hoàn thiện slide 13-24 và dọn giao diện | File slide hoàn chỉnh + UI demo ổn định |

---

## 4. Phối hợp

- Với Lê Thiên Lộc: chuẩn hóa API hàm `solve` để UI gọi thống nhất.
- Với Đỗ Đình Chiến và Hoàng Văn Hưng: xác nhận ý nghĩa kết quả hiển thị cho Greedy và B&B.
- Với Huỳnh Gia Huy: test giao diện bằng dataset thật và đồng bộ template slide.
