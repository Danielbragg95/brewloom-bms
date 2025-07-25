import streamlit as st
import json
import os

LOG_FILE = "data/audit_log.json"

def render_inventory_audit_log():
    st.header("📜 Inventory Audit Log")

    if not os.path.exists(LOG_FILE):
        st.info("No audit log entries found.")
        return

    with open(LOG_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
    if not logs:
        st.info("Audit log is empty.")
        return

    for entry in reversed(logs):  # newest first
        st.markdown(f"**{entry['timestamp']}** — *{entry['action'].capitalize()}*")
        st.markdown(f"- **Item**: {entry['item_name']} (`{entry['item_id']}`)")
        if entry.get("before") or entry.get("after"):
            with st.expander("Details"):
                if entry.get("before"):
                    st.json(entry["before"], expanded=False)
                if entry.get("after"):
                    st.json(entry["after"], expanded=False)
        st.markdown("---")