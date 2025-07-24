from dataclasses import dataclass

@dataclass
class InventoryItem:
    id: str
    name: str
    category: str      # Main category (e.g., Ingredients)
    subcategory: str   # Specific type (e.g., Grain)
    quantity: float
    unit: str
    threshold: float
