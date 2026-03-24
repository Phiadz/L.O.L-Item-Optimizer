# Kế Hoạch Thực Hiện — Đỗ Đình Chiến (MSSV: 51205005553)

**Vai trò:** Cài đặt thuật toán Tham lam (Greedy), Viết tài liệu phân tích thuật toán Greedy

---

## 1. Tổng Quan Nhiệm Vụ

Đỗ Đình Chiến phụ trách trọn gói phần Greedy của dự án:

1. Viết code đầy đủ thuật toán Greedy trong `algorithms/greedy.py`.
2. Viết mục báo cáo phân tích thuật toán Greedy (nguyên lý, độ phức tạp, giới hạn).

Lưu ý phân công mới: không phụ trách code Branch and Bound.

---

## 2. Nội Dung Công Việc Chi Tiết

### 2.1 Viết code thuật toán Greedy (cụ thể)

**Yêu cầu code bắt buộc:**

1. Tính `ratio = power / gold` cho mỗi item.
2. Sắp xếp item giảm dần theo ratio (trên bản sao list).
3. Duyệt list đã sắp xếp và chọn item nếu còn đủ vàng.
4. Trả kết quả đúng format API chung.

**Khung xử lý cần có trong `greedy.py`:**

```python
sorted_items = sorted(items, key=lambda x: x.ratio(), reverse=True)
selected = []
gold_remaining = max_gold
for item in sorted_items:
	if item.gold <= gold_remaining:
		selected.append(item)
		gold_remaining -= item.gold
```

**Case biên phải xử lý:**

- `items` rỗng.
- `max_gold <= 0`.
- item có giá trị `gold <= 0`.

### 2.2 Kiểm thử cụ thể cho Greedy

**Bộ test cần chuẩn bị:**

1. Test cơ bản (5-10 item, tính tay được).
2. Test biên (`W=0`, list rỗng, chỉ 1 item).
3. Test phản ví dụ: Greedy cho kết quả thấp hơn DP/B&B.

**Tiêu chí pass:**

- Không crash.
- Dict output đúng key.
- Runtime thấp hơn DP ở dataset lớn.

### 2.3 Viết tài liệu phân tích Greedy

**Nội dung phải có trong báo cáo:**

1. Mô tả thuật toán theo từng bước.
2. Phân tích độ phức tạp:
   - Sắp xếp: $O(N \log N)$
   - Duyệt: $O(N)$
   - Tổng: $O(N \log N)$
3. Giải thích vì sao Greedy không luôn tối ưu cho 0/1 Knapsack.
4. Đưa phản ví dụ số cụ thể.
5. Nhận xét thực nghiệm (nhanh nhưng không đảm bảo optimal).

---

## 3. Timeline

| Tuần | Công việc | Đầu ra cụ thể |
|---|---|---|
| Tuần 1 | Code Greedy bản hoàn chỉnh đầu tiên | `algorithms/greedy.py` chạy được trên dữ liệu thật |
| Tuần 2 | Viết test case và fix edge cases | Bộ test Greedy + minh họa phản ví dụ |
| Tuần 3 | Đối chiếu Greedy với DP/B&B trên cùng dataset | Bảng so sánh quality và runtime |
| Tuần 4 | Viết xong mục phân tích Greedy trong báo cáo | Mục Greedy hoàn chỉnh để ghép báo cáo cuối |

---

## 4. Phối hợp

- Với Lê Thiên Lộc: thống nhất API chung và đối chiếu với DP.
- Với Hoàng Văn Hưng: so sánh Greedy và B&B trên cùng input.
- Với Huỳnh Gia Huy: lấy bộ test phản ví dụ và bộ test hiệu năng.
- Với Nguyễn Văn Vũ: thống nhất thông điệp hiển thị trên UI rằng Greedy là heuristic.
