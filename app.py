import streamlit as st
from modules.inventory.dashboard import render_inventory_dashboard
from modules.inventory.adjust import render_inventory_adjust
from modules.inventory.add import render_add_inventory_item

st.set_page_config(page_title="BrewLoom BMS", layout="wide")

st.sidebar.title("📚 BrewLoom Modules")
module = st.sidebar.radio("Select Module", [
    "📦 Inventory Dashboard",
    "➕ Add Inventory Item",
    "✏️ Adjust Inventory"
])

if module == "📦 Inventory Dashboard":
    render_inventory_dashboard()
elif module == "➕ Add Inventory Item":
    render_add_inventory_item()
elif module == "✏️ Adjust Inventory":
    render_inventory_adjust()
