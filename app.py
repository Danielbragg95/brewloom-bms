import streamlit as st
from modules.inventory.dashboard import render_inventory_dashboard
from modules.inventory.add import render_add_inventory_item
from modules.inventory.edit import render_edit_inventory_item
from modules.inventory.adjust import render_inventory_adjust
from modules.inventory.delete import render_delete_inventory_item
from modules.inventory.import_csv import render_import_inventory

st.set_page_config(page_title="BrewLoom BMS", layout="wide")

st.sidebar.title("📚 BrewLoom Modules")

with st.sidebar.expander("📦 Inventory Management", expanded=True):
    inventory_module = st.radio("Select Inventory View", [
        "Dashboard",
        "Add Item",
        "Edit Item",
        "Adjust Item",
        "Delete Item",
        "Import CSV"
    ])

if inventory_module == "Dashboard":
    render_inventory_dashboard()
elif inventory_module == "Add Item":
    render_add_inventory_item()
elif inventory_module == "Edit Item":
    render_edit_inventory_item()
elif inventory_module == "Adjust Item":
    render_inventory_adjust()
elif inventory_module == "Delete Item":
    render_delete_inventory_item()
elif inventory_module == "Import CSV":
    render_import_inventory()
