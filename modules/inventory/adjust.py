import streamlit as st
from modules.inventory.inventory_store import get_all_items, update_quantity

def render_inventory_adjust():
    st.header("✏️ Adjust Inventory")

    items = get_all_items()
    if not items:
        st.info("No inventory items to adjust.")
        return

    options = {item["name"]: item["id"] for item in items}
    item_name = st.selectbox("Select item", list(options.keys()))
    delta = st.number_input("Adjustment quantity (+/-)", value=0.0, step=0.5)

    if st.button("Apply Adjustment"):
        try:
            update_quantity(options[item_name], delta)
            st.success(f"{item_name} updated by {delta}.")
        except Exception as e:
            st.error(f"Error: {e}")
