from fastapi import HTTPException


class ItemNotFoundError(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id
        super().__init__(f"Item with ID {item_id} not found")
    

