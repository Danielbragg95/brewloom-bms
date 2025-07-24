import streamlit as st
from modules.inventory.inventory_item import InventoryItem
from modules.inventory.inventory_store import add_item

def render_add_inventory_item():
    st.header("➕ Add Inventory Item")

    CATEGORY_MAP = {
        "Ingredients": ["Grain", "Hops", "Yeast", "Adjuncts"],
        "Packaging": ["Cans", "Labels", "Caps"],
        "Custodial Supplies": ["Soap", "Paper Towels", "Sanitizer"],
        "Other": ["Miscellaneous"]
    }

    UNIT_DEFAULTS = {
        "Grain": "lbs",
        "Hops": "lbs",
        "Yeast": "oz",
        "Adjuncts": "oz",
        "Cans": "count",
        "Labels": "count",
        "Caps": "count",
        "Soap": "gal",
        "Sanitizer": "gal",
        "Paper Towels": "rolls",
        "Miscellaneous": "units"
    }

    main_category = st.selectbox("Select Category", list(CATEGORY_MAP.keys()))
    subcategories = sorted(CATEGORY_MAP[main_category])
    subcategory = st.selectbox("Select Subcategory", subcategories)

    name = st.text_input("Item Name")
    quantity = st.number_input("Starting Quantity", min_value=0.0, step=0.5)
    default_unit = UNIT_DEFAULTS.get(subcategory, "units")
    unit = st.text_input("Unit (e.g. lbs, oz, gal)", value=default_unit)
    threshold = st.number_input("Threshold for Alerts", min_value=0.0, step=0.5)

    if st.button("Add Item"):
        if not name or not unit:
            st.warning("Name and Unit are required.")
        else:
            item = InventoryItem(
                id="temp",
                name=name,
                category=main_category,
                subcategory=subcategory,
                quantity=quantity,
                unit=unit,
                threshold=threshold
            )
            add_item(item)
            st.success(f"Item '{name}' added to {main_category} > {subcategory}")
