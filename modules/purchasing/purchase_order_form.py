import streamlit as st
import json
import os
from datetime import datetime
from modules.inventory.inventory_store import get_all_items, save_items
from modules.purchasing.po_utils import generate_po_id

PO_FILE = "data/po_records.json"
CATEGORY_SUBCATEGORY_MAP = {
    "Ingredients": ["Hops", "Grain", "Yeast", "Adjuncts"],
    "Packaging": ["Cans", "Bottles", "Labels", "Boxes"],
    "Custodial Supplies": ["Paper Towels", "Cleaner", "Gloves"]
}

def load_po_records():
    if not os.path.exists(PO_FILE):
        return []
    try:
        with open(PO_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_po_records(records):
    os.makedirs(os.path.dirname(PO_FILE), exist_ok=True)
    with open(PO_FILE, "w") as f:
        json.dump(records, f, indent=2)

def render_create_purchase_order():
    st.title("Create Purchase Order")
    vendor_name = ""
    try:
        with open("data/vendors.json", "r") as vf:
            vendors = json.load(vf)
            vendor_options = [v["name"] for v in vendors]
            vendor_name = st.selectbox("Vendor", vendor_options)
    except (FileNotFoundError, json.JSONDecodeError):
        vendor_name = st.text_input("Vendor Name")

    if "po_entries" not in st.session_state:
        st.session_state.po_entries = [{}]

    inventory = get_all_items()
    inventory_item_names = [item["name"] for item in inventory]

    st.subheader("Line Items")
    for idx, entry in enumerate(st.session_state.po_entries):
        st.markdown(f"##### Item {idx + 1}")
        col1, col2, col3 = st.columns([4, 2, 2])
        with col1:
            item_name = st.text_input("Item Name", value=entry.get("item_name", ""), key=f"item_name_{idx}")
        with col2:
            quantity = st.number_input("Qty", min_value=0, value=entry.get("quantity", 0), key=f"qty_{idx}")
        with col3:
            unit_cost = st.number_input("Unit Cost ($)", min_value=0.0, format="%.2f", value=entry.get("unit_cost", 0.0), key=f"unit_cost_{idx}")

        item_data = {
            "item_name": item_name,
            "quantity": quantity,
            "unit_cost": unit_cost
        }

        if item_name and item_name not in inventory_item_names:
            category = st.selectbox("Category", list(CATEGORY_SUBCATEGORY_MAP.keys()), key=f"cat_{idx}")
            subcategory = st.selectbox("Subcategory", CATEGORY_SUBCATEGORY_MAP.get(category, []), key=f"subcat_{idx}")
            unit = st.text_input("Unit", value=entry.get("unit", ""), key=f"unit_{idx}")
            item_data.update({"category": category, "subcategory": subcategory, "unit": unit})

        st.session_state.po_entries[idx] = item_data

    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ Add Item"):
            st.session_state.po_entries.append({})
            st.rerun()
    with col2:
        if len(st.session_state.po_entries) > 1 and st.button("➖ Remove Last Item"):
            st.session_state.po_entries.pop()
            st.rerun()

    st.markdown("---")
    if st.button("Create Purchase Order"):
        if not vendor_name.strip():
            st.error("Please enter a vendor name.")
            return

        po_records = load_po_records()
        valid_entries = [
            item for item in st.session_state.po_entries
            if item.get("item_name") and item.get("quantity", 0) > 0
        ]
        if not valid_entries:
            st.error("Please add at least one valid item.")
            return

        po_id = generate_po_id(po_records)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_po = {
            "po_id": po_id,
            "vendor": vendor_name,
            "items": valid_entries,
            "timestamp": timestamp,
            "status": "Pending"
        }
        po_records.append(new_po)
        save_po_records(po_records)

        # Update inventory
        for item in valid_entries:
            match = next((i for i in inventory if i["name"] == item["item_name"]), None)
            if match:
                match["quantity"] += item["quantity"]
            else:
                inventory.append({
                    "id": len(inventory) + 1,
                    "name": item["item_name"],
                    "quantity": item["quantity"],
                    "category": item["category"],
                    "subcategory": item["subcategory"],
                    "unit": item["unit"]
                })
        save_items(inventory)
        st.success(f"Purchase Order {po_id} created successfully!")
        st.session_state.po_entries = [{}]