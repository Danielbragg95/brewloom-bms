import streamlit as st
import pandas as pd
from modules.inventory.inventory_store import get_all_items

def render_inventory_dashboard():
    st.header("📦 Inventory Dashboard")
    items = get_all_items()
    if not items:
        st.info("No inventory items found.")
        return

    df = pd.DataFrame(items)
    df = df[["name", "category", "quantity", "unit", "threshold"]]
    df.columns = ["Name", "Category", "Quantity", "Unit", "Reorder Threshold"]

    st.dataframe(df, use_container_width=True, hide_index=True)
