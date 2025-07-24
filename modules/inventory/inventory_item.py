from dataclasses import dataclass

@dataclass
class InventoryItem:
    id: str
    name: str
    category: str
    quantity: float
    unit: str
    threshold: float
