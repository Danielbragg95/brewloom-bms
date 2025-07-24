import streamlit as st
from modules.inventory.dashboard import render_inventory_dashboard
from modules.inventory.add import render_add_inventory_item
from modules.inventory.edit import render_edit_inventory_item
from modules.inventory.adjust import render_inventory_adjust
from modules.inventory.delete import render_delete_inventory_item
from modules.inventory.import_csv import render_import_inventory
from modules.inventory.audit_log import render_inventory_audit_log
from modules.purchasing.vendor_directory import render_vendor_directory

st.set_page_config(page_title="BrewLoom BMS", layout="wide")

st.sidebar.title("📚 BrewLoom Modules")

with st.sidebar.expander("📦 Inventory Management", expanded=True):
    show_dashboard = st.checkbox("Dashboard")
    show_add = st.checkbox("Add Item")
    show_edit = st.checkbox("Edit Item")
    show_adjust = st.checkbox("Adjust Item")
    show_delete = st.checkbox("Delete Item")
    show_import = st.checkbox("Import CSV")
    show_audit = st.checkbox("Audit Log")

with st.sidebar.expander("📑 Purchasing", expanded=True):
    show_vendors = st.checkbox("Vendor Directory")

# Inventory module views
if show_dashboard:
    render_inventory_dashboard()
if show_add:
    render_add_inventory_item()
if show_edit:
    render_edit_inventory_item()
if show_adjust:
    render_inventory_adjust()
if show_delete:
    render_delete_inventory_item()
if show_import:
    render_import_inventory()
if show_audit:
    render_inventory_audit_log()

# Purchasing module views
if show_vendors:
    render_vendor_directory()
