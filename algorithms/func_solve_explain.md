Đây là giao diện lập trình chung (Common API Contract) — tức là một "hợp đồng" quy định rằng mọi thuật toán (DP, Greedy, Branch & Bound) đều phải triển khai hàm solve với cùng một chữ ký (signature).

Tại sao cần điều này?
Để tầng giao diện (UI) không cần biết bên trong từng thuật toán hoạt động ra sao. UI chỉ cần gọi solver.solve(items, max_gold) là nhận được cùng một cấu trúc kết quả, bất kể đang dùng thuật toán nào.

items:          list[Item]	Danh sách trang bị LOL (mỗi Item có name, gold_cost, power)
max_gold:       int	Số Vàng tối đa người chơi đang có
selected_items: Danh sách trang bị mà thuật toán đã chọn
total_power:    Tổng Điểm Sức Mạnh của các trang bị được chọn
gold_used:      Tổng Vàng đã tiêu
gold_remaining: Vàng còn thừa (max_gold - gold_used)
exec_time_ms:   Thời gian chạy thuật toán (mili-giây), dùng để so sánh hiệu suất


Ví dụ thực tế:

# UI gọi Greedy
result = greedy_solver.solve(items, 10000)

# UI gọi DP — cùng cách gọi, cùng cấu trúc kết quả
result = dp_solver.solve(items, 10000)

# Hiển thị kết quả
print(result["total_power"])    # → 850.5
print(result["exec_time_ms"])   # → 0.12 ms (Greedy nhanh hơn DP)

Nhờ chuẩn hóa API này, UI có thể chạy cả 3 thuật toán cùng lúc và so sánh kết quả mà không cần viết code riêng cho từng thuật toán.