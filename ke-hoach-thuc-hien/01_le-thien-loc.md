# Kế Hoạch Thực Hiện — Lê Thiên Lộc (MSSV: 079306040024)

**Vai trò:** Thiết kế kiến trúc phần mềm, Cài đặt thuật toán Quy hoạch động (DP), Quản lý Git, Viết tài liệu phân tích thuật toán DP

---

## 1. Tổng Quan Nhiệm Vụ

Lê Thiên Lộc là đầu mối kỹ thuật của nhóm, chịu trách nhiệm 4 mảng:

1. Chốt kiến trúc code và giao diện API chung để 3 thuật toán tích hợp đồng nhất.
2. Viết code hoàn chỉnh thuật toán DP trong `algorithms/dp.py`.
3. Quản lý nhánh Git, review PR, kiểm soát merge.
4. Viết phần báo cáo phân tích thuật toán DP (lý thuyết + thực nghiệm).

---

## 2. Nội Dung Công Việc Chi Tiết

### 2.1 Kiến trúc và chuẩn giao tiếp giữa các module

**File cần chốt:**

- `models/item.py`: model dữ liệu `Item`.
- `algorithms/dp.py`, `algorithms/greedy.py`, `algorithms/branch_and_bound.py`: chuẩn hàm `solve`.
- `utils/data_loader.py`: đọc/ghi dữ liệu item.
- `ui/main_window.py`: gọi các thuật toán và hiển thị.

**Chuẩn API bắt buộc cho mọi thuật toán:**

```python
def solve(items: list[Item], max_gold: int) -> dict:
	return {
		"selected_items": list[Item],
		"total_power": float,
		"gold_used": int,
		"gold_remaining": int,
		"exec_time_ms": float,
	}
```

**Checklist phải làm xong:**

- Thống nhất kiểu dữ liệu trước khi mọi người code thuật toán.
- Chốt cách đặt tên key trong dict kết quả.
- Chốt quy ước import package để tránh lỗi vòng lặp import.

### 2.2 Cài đặt thuật toán DP (cụ thể mức code)

**Mục tiêu code:** triển khai đầy đủ 4 bước trong `algorithms/dp.py`.

1. Khởi tạo bảng `dp` kích thước `(n+1) x (W+1)`.
2. Điền bảng theo công thức truy hồi 0/1 knapsack.
3. Truy vết ngược từ `dp[n][W]` để lấy `selected_items`.
4. Tính `gold_used`, `gold_remaining`, đo `exec_time_ms` bằng `time.perf_counter()`.

**Công thức bắt buộc ghi trong comment/tài liệu:**

$$
dp[i][w] =
\begin{cases}
dp[i-1][w], & \text{nếu } gold_i > w \\
\max(dp[i-1][w],\ dp[i-1][w-gold_i] + power_i), & \text{nếu } gold_i \le w
\end{cases}
$$

**Case biên cần xử lý trong code:**

- `items` rỗng.
- `max_gold <= 0`.
- item có `gold <= 0` (bỏ qua hoặc chuẩn hóa).

**Output code bắt buộc:**

- File `algorithms/dp.py` chạy độc lập không crash.
- Kết quả DP khớp B&B ở cùng input.

### 2.3 Quản lý Git (làm cụ thể từng bước)

**Nhánh đề xuất:** `feature/dp-architecture`.

**Quy trình làm việc bắt buộc:**

1. Pull `develop` mới nhất trước khi code.
2. Commit theo block nhỏ: kiến trúc -> DP core -> truy vết -> test.
3. Tạo PR kèm mô tả test case đã chạy.
4. Chỉ merge sau khi kiểm tra xung đột với UI và utils.

**Mẫu commit:**

- `[dp] implement table transition`
- `[dp] add traceback selected items`
- `[architecture] finalize shared solve() contract`

### 2.4 Viết tài liệu phân tích DP (phần của Lộc trong báo cáo)

**Phần bắt buộc phải viết:**

1. Mô tả trạng thái và công thức truy hồi.
2. Chứng minh tính đúng (ngắn gọn theo quy nạp).
3. Phân tích độ phức tạp:
   - Thời gian: $O(N \times W)$
   - Không gian: $O(N \times W)$, mở rộng thêm bản tối ưu 1D là $O(W)$
4. Nhận xét thực nghiệm từ bảng số liệu nhóm cung cấp.

**Đầu ra tài liệu:** 2-4 trang nội dung DP, có công thức, có bảng nhận xét.

---

## 3. Timeline

| Tuần | Công việc | Đầu ra cụ thể |
|---|---|---|
| Tuần 1 | Chốt kiến trúc + API + quy tắc Git | Sơ đồ module và chuẩn `solve()` thống nhất |
| Tuần 2 | Viết xong DP đầy đủ (core + traceback + timing) | `algorithms/dp.py` trả đúng format kết quả |
| Tuần 3 | Đối chiếu kết quả DP với B&B, hỗ trợ tích hợp UI | Kết quả hiển thị ổn định trên UI |
| Tuần 4 | Viết xong mục phân tích DP trong báo cáo | Mục DP hoàn chỉnh để ghép báo cáo cuối |

---

## 4. Phối hợp

- Với Đỗ Đình Chiến: thống nhất kiểu input/output giữa DP và Greedy.
- Với Hoàng Văn Hưng: đối chiếu `total_power(DP) == total_power(B&B)`.
- Với Nguyễn Văn Vũ: cung cấp dữ liệu mẫu để test giao diện hiển thị kết quả.
- Với Huỳnh Gia Huy: nhận bộ dữ liệu test và số liệu thực nghiệm cho phần viết báo cáo DP.
