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

    # Ensure threshold column exists
    if "threshold" not in df.columns:
        df["threshold"] = 0

    df["Status"] = df.apply(lambda row: "🔔 Reorder Needed" if row.get("threshold") is not None and row["quantity"] < row["threshold"] else "", axis=1)
    df["Needs Reorder"] = df["quantity"] < df["threshold"]

    df = df[["name", "category", "subcategory", "quantity", "unit", "threshold", "Status", "Needs Reorder"]]
    df.columns = ["Name", "Category", "Subcategory", "Quantity", "Unit", "Reorder Threshold", "Status", "Needs Reorder"]

    # Main category filter
    categories = sorted(df["Category"].dropna().unique().tolist())
    selected_category = st.selectbox("Filter by Category", ["All"] + categories)
    if selected_category != "All":
        df = df[df["Category"] == selected_category]

    # Low stock toggle
    show_low_only = st.checkbox("Show only low-stock items", value=False)
    if show_low_only:
        df = df[df["Needs Reorder"]]

    df = df.drop(columns=["Needs Reorder"])

    def highlight_low_stock(row):
        if row["Quantity"] < row["Reorder Threshold"]:
            return ["background-color: #ffe6e6"] * len(row)
        return [""] * len(row)

    styled_df = df.style.apply(highlight_low_stock, axis=1).format({"Quantity": "{:.2f}", "Reorder Threshold": "{:.2f}"})

    st.dataframe(styled_df, use_container_width=True, hide_index=True)