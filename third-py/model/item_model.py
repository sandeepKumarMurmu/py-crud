from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Item:
    id: int
    name: str

# In-memory "database"
_db: List[Item] = [
    Item(1, "Apple"),
    Item(2, "Banana"),
    Item(3, "Cherry"),
]

def get_all_items() -> List[Item]:
    return list(_db)

def get_item(item_id: int) -> Optional[Item]:
    return next((it for it in _db if it.id == item_id), None)

def add_item(name: str) -> Item:
    new_id = max((it.id for it in _db), default=0) + 1
    item = Item(new_id, name)
    _db.append(item)
    return item
