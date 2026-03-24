# Kế Hoạch Thực Hiện — Hoàng Văn Hưng (MSSV: 040206020805)

**Vai trò:** Cài đặt thuật toán Quay lui Nhánh cận (Branch and Bound), Viết tài liệu phân tích thuật toán B&B

---

## 1. Tổng Quan Nhiệm Vụ

Theo phân công mới, Hoàng Văn Hưng phụ trách toàn bộ nhánh Branch and Bound:

1. Viết code thuật toán B&B trong `algorithms/branch_and_bound.py`.
2. Viết mục báo cáo phân tích riêng cho B&B.

Không phụ trách slide và không phụ trách phần tổng hợp báo cáo chung.

---

## 2. Nội Dung Công Việc Chi Tiết

### 2.1 Viết code Branch and Bound (cụ thể)

**Mục tiêu code bắt buộc:**

1. Tiền xử lý item theo ratio giảm dần.
2. Cài đặt hàm `upper_bound(...)` bằng ý tưởng fractional knapsack.
3. Duyệt trạng thái theo Best-First Search hoặc DFS có pruning.
4. Cập nhật nghiệm tốt nhất và truy vết item đã chọn.

**Khung node nên có:**

```python
# level, current_gold, current_power, bound, selected_indices
```

**Điều kiện cắt nhánh bắt buộc:**

- Nếu `bound <= best_power` thì bỏ nhánh.
- Nếu `current_gold > max_gold` thì bỏ nhánh.

### 2.2 Kiểm thử thuật toán B&B

**Bộ test cần có:**

1. Test cơ bản (dataset nhỏ, dễ kiểm tra).
2. Test biên (W=0, items rỗng).
3. Test so sánh với DP: kết quả `total_power` phải bằng DP.
4. Test hiệu năng dataset trung bình/lớn.

**Tiêu chí pass:**

- Không sai nghiệm tối ưu.
- Không vòng lặp vô hạn.
- Runtime chấp nhận được trên bộ test lớp học.

### 2.3 Viết tài liệu phân tích B&B

**Các ý bắt buộc phải viết:**

1. Cây trạng thái chọn/không chọn item.
2. Khái niệm upper bound và vì sao dùng fractional bound.
3. Cơ chế pruning và tác động đến tốc độ.
4. Độ phức tạp:
	- Trường hợp xấu nhất: $O(2^N)$
	- Trường hợp thực tế: nhanh hơn brute force nhờ cắt nhánh
5. So sánh thực nghiệm với DP và Greedy.

---

## 3. Timeline

| Tuần | Công việc | Đầu ra cụ thể |
|---|---|---|
| Tuần 1 | Hoàn thiện thiết kế thuật toán và hàm bound | Skeleton B&B + mô tả logic |
| Tuần 2 | Viết xong code duyệt nhánh và pruning | `branch_and_bound.py` chạy được case cơ bản |
| Tuần 3 | Test và đối chiếu với DP | Bảng so sánh kết quả B&B và DP |
| Tuần 4 | Viết xong mục phân tích B&B trong báo cáo | Mục B&B hoàn chỉnh để ghép báo cáo tổng |

---

## 4. Phối hợp

- Với Lê Thiên Lộc: kiểm chứng tối ưu B&B bằng cách đối chiếu kết quả DP.
- Với Đỗ Đình Chiến: so sánh khác biệt giữa Greedy và B&B trong phần thảo luận.
- Với Huỳnh Gia Huy: nhận dataset và số liệu benchmark để viết nhận xét thực nghiệm.
- Với Nguyễn Văn Vũ: xác nhận dữ liệu B&B hiển thị đúng trên giao diện.
