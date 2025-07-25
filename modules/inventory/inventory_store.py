import json
import os

INVENTORY_FILE = "data/inventory.json"

def get_all_items():
    if not os.path.exists(INVENTORY_FILE):
        return []
    with open(INVENTORY_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
def save_items(data):
    os.makedirs(os.path.dirname(INVENTORY_FILE), exist_ok=True)
    with open(INVENTORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_item(new_item):
    items = get_all_items()
    items.append(new_item)
    save_items(items)

def update_quantity(item_id, delta):
    items = get_all_items()
    for item in items:
        if item["id"] == item_id:
            item["quantity"] += delta
            break
    save_items(items)