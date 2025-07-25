import streamlit as st
import json
import os
import pandas as pd

PO_FILE = "data/po_records.json"

def load_po_records():
    if not os.path.exists(PO_FILE):
        return []
    try:
        with open(PO_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def render_po_dashboard():
    st.title("PO Dashboard")
    po_records = load_po_records()
    if not po_records:
        st.info("No purchase orders found.")
        return

    flat_rows = []
    for record in po_records:
        for item in record["items"]:
            flat_rows.append({
                "PO ID": record["po_id"],
                "Vendor": record.get("vendor", "Unknown"),
                "Item": item["item_name"],
                "Qty": item["quantity"],
                "Unit Cost": item["unit_cost"],
                "Date": record["timestamp"],
                "Status": record["status"]
            })

    df = pd.DataFrame(flat_rows)
    df = df.drop(columns=["PO ID"])
    st.dataframe(df, hide_index=True)
