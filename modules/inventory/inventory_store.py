import json
import os
from uuid import uuid4
from modules.inventory.inventory_item import InventoryItem

DATA_FILE = "data/inventory.json"

def _load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def _save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_all_items():
    return _load_data()

def add_item(item: InventoryItem):
    data = _load_data()
    for existing in data:
        if (
            existing["name"].lower() == item.name.lower() and
            existing["subcategory"] == item.subcategory and
            existing["category"] == item.category
        ):
            existing["quantity"] += item.quantity
            _save_data(data)
            return
    item_dict = item.__dict__.copy()
    item_dict["id"] = str(uuid4())
    data.append(item_dict)
    _save_data(data)

def update_quantity(item_id, delta):
    data = _load_data()
    for item in data:
        if item["id"] == item_id:
            item["quantity"] += delta
            break
    _save_data(data)
