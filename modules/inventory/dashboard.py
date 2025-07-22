import streamlit as st
from modules.inventory.inventory_store import get_all_items

def render_inventory_dashboard():
    st.header("📦 Inventory Dashboard")
    items = get_all_items()
    if not items:
        st.info("No inventory items found.")
        return

    for item in items:
        st.markdown(f"**{item['name']}**")
        st.write(f"Category: {item['category']} | Quantity: {item['quantity']} {item['unit']}")
        if item["quantity"] < item["threshold"]:
            st.warning("⚠️ Below threshold!")