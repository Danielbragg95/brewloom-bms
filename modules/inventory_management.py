```python
class InventoryItem:
    def __init__(self, item_id, name, category, quantity):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity

    def add_stock(self, amount):
        """Add stock to the inventory item."""
        self.quantity += amount
        print(f"Added {amount} to {self.name}. New quantity: {self.quantity}")

    def deduct_stock(self, amount):
        """Deduct stock from the inventory item."""
        if amount > self.quantity:
            raise ValueError(f"Not enough stock to deduct. Current stock: {self.quantity}")
        self.quantity -= amount
        print(f"Deducted {amount} from {self.name}. New quantity: {self.quantity}")

    def is_low_stock(self, threshold):
        """Check if the stock is below a certain threshold."""
        return self.quantity < threshold


class InventoryManagement:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, name, category, quantity):
        """Add a new item to the inventory."""
        if item_id in self.inventory:
            raise KeyError(f"Item with ID {item_id} already exists.")
        self.inventory[item_id] = InventoryItem(item_id, name, category, quantity)
        print(f"Added new item: {name} with ID {item_id}")

    def update_stock(self, item_id, amount, operation='add'):
        """Update stock for a specific item."""
        if item_id not in self.inventory:
            raise KeyError(f"Item with ID {item_id} not found in inventory.")
        item = self.inventory[item_id]
        if operation == 'add':
            item.add_stock(amount)
        elif operation == 'deduct':
            item.deduct_stock(amount)
        else:
            raise ValueError("Operation must be 'add' or 'deduct'.")

    def check_low_inventory(self, threshold):
        """Check all items for low inventory and trigger alerts."""
        low_inventory_items = []
        for item_id, item in self.inventory.items():
            if item.is_low_stock(threshold):
                low_inventory_items.append(item)
                print(f"Low inventory alert for {item.name} (ID: {item_id}). Current stock: {item.quantity}")
        return low_inventory_items

    def get_inventory_report(self):
        """Generate a report of current inventory levels."""
        report = []
        for item_id, item in self.inventory.items():
            report.append({
                'item_id': item_id,
                'name': item.name,
                'category': item.category,
                'quantity': item.quantity
            })
        return report


# Example usage
if __name__ == "__main__":
    inventory_manager = InventoryManagement()
    inventory_manager.add_item(1, "Raw Material A", "Raw Materials", 100)
    inventory_manager.add_item(2, "Packaging B", "Packaging", 50)
    inventory_manager.add_item(3, "Finished Good C", "Finished Goods", 200)

    inventory_manager.update_stock(1, 20, 'add')
    inventory_manager.update_stock(2, 10, 'deduct')

    low_inventory_items = inventory_manager.check_low_inventory(30)

    report = inventory_manager.get_inventory_report()
    print("Current Inventory Report:")
    for item in report:
        print(item)
```
