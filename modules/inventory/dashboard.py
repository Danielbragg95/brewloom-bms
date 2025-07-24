import streamlit as st
from modules.inventory.inventory_store import get_all_items

def render_inventory_dashboard():
    st.header("📦 Inventory Dashboard")
    items = get_all_items()
    if not items:
        st.info("No inventory items found.")
        return

    for item in sorted(items, key=lambda x: x["name"]):
        cols = st.columns([3, 2, 2])
        cols[0].markdown(f"**{item['name']}**")
        cols[1].write(f"{item['quantity']} {item['unit']}")
        cols[2].write(f"Category: {item['category']}")
        if item["quantity"] < item["threshold"]:
            st.warning(f"⚠️ {item['name']} is below threshold!")
