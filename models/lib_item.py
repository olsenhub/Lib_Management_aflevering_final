class LibraryItem:
    def __init__(self, item_id: str, title: str):
        self.item_id = item_id
        self.title = title

    def display_info(self) -> str:
        return f"ID: {self.item_id}, Title: {self.title}"