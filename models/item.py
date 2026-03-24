# Lớp dữ liệu Item (trang bị)
'''
[items_data.json] → data_loader.py → [danh sách Item]
                                          ↓
                               [Nhập số Vàng từ UI]
                                          ↓
                    ┌─────────────────────┼─────────────────────┐
                 dp.py             greedy.py         branch_and_bound.py
                    └─────────────────────┼─────────────────────┘
                                          ↓
                               [Kết quả + Thời gian]
                                          ↓
                                    result_view.py
'''
class Item:
    def __init__(self, name: str, gold: int, power: float):
        self.name  = name    # Tên trang bị (ví dụ: "Vô Cực Kiếm")
        self.gold  = gold    # Giá Vàng (trọng lượng w_i)
        self.power = power   # Điểm Sức Mạnh (giá trị v_i)
    def ratio(self):
        """Tỷ lệ Sức Mạnh / Vàng, dùng cho thuật toán Tham lam."""
        return self.power / self.gold if self.gold > 0 else 0