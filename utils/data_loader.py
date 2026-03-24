# Đọc/ghi JSON
from models.item import Item


def load_items(file_path: str = "items_data.json") -> list[Item]:
	raise NotImplementedError(f"TODO: implement load_items() for '{file_path}'")


def save_items(items: list[Item], file_path: str = "items_data.json") -> None:
	raise NotImplementedError(
		f"TODO: implement save_items() for {len(items)} items to '{file_path}'"
	)