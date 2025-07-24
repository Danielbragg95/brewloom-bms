import streamlit as st
from modules.inventory.inventory_item import InventoryItem
from modules.inventory.inventory_store import add_item

def render_add_inventory_item():
    st.header("➕ Add Inventory Item")

    with st.form("add_item_form"):
        name = st.text_input("Item Name")
        category = st.selectbox("Category", [
            "Grain", "Hops", "Yeast", "Adjuncts",
            "Packaging", "Cleaning Supplies",
            "Raw Materials", "Finished Goods", "Other"
        ])
        quantity = st.number_input("Starting Quantity", min_value=0.0, step=0.5)
        unit = st.text_input("Unit (e.g. lbs, oz, gal)")
        threshold = st.number_input("Threshold for Alerts", min_value=0.0, step=0.5)
        submitted = st.form_submit_button("Add Item")

        if submitted:
            if not name or not unit:
                st.warning("Name and Unit are required.")
            else:
                item = InventoryItem(
                    id="temp",  # This will be replaced in store
                    name=name,
                    category=category,
                    quantity=quantity,
                    unit=unit,
                    threshold=threshold,
                )
                add_item(item)
                st.success(f"Item '{name}' added successfully!")
