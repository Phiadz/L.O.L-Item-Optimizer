# Thuật toán Tham lam (Đỗ Đình Chiến)
from models.item import Item
















def solve(items: list[Item], max_gold: int) -> dict:
    """
    Trả về dict:
    {
        "selected_items": list[Item],  # Danh sách trang bị được chọn
        "total_power":    float,       # Tổng Sức Mạnh đạt được
        "gold_used":      int,         # Tổng Vàng đã dùng
        "gold_remaining": int,         # Vàng còn dư
        "exec_time_ms":   float,       # Thời gian thực thi (mili-giây)
    }
    """