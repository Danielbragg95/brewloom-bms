import streamlit as st
import pandas as pd
from modules.inventory.inventory_item import InventoryItem
from modules.inventory.inventory_store import add_item

def render_import_inventory():
    st.header("📁 Import Inventory from CSV")

    st.markdown("Upload a CSV with the following columns (headers required):")
    st.code("name,category,quantity,unit,threshold", language="text")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            required_cols = {"name", "category", "quantity", "unit", "threshold"}
            if not required_cols.issubset(df.columns):
                st.error("CSV missing required columns.")
                return

            added_count = 0
            for _, row in df.iterrows():
                item = InventoryItem(
                    id="temp",
                    name=str(row["name"]),
                    category=str(row["category"]),
                    quantity=float(row["quantity"]),
                    unit=str(row["unit"]),
                    threshold=float(row["threshold"])
                )
                add_item(item)
                added_count += 1

            st.success(f"Successfully imported {added_count} items.")
        except Exception as e:
            st.error(f"Error importing CSV: {e}")
