import streamlit as st
from modules.inventory.inventory_store import get_all_items, save_items
from modules.inventory.audit_utils import write_audit_log

def render_delete_inventory_item():
    st.header("🗑️ Delete Inventory Item")

    items = get_all_items()
    if not items:
        st.info("No inventory items available.")
        return

    item_names = [item["name"] for item in items]
    selected_name = st.selectbox("Select Item to Delete", item_names)

    if "confirm_delete" not in st.session_state:
        st.session_state.confirm_delete = False

    if st.button("Delete Item"):
        st.session_state.confirm_delete = True

    if st.session_state.confirm_delete:
        st.warning("Are you sure you want to delete this item? This cannot be undone.")

        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Yes, Delete Permanently"):
                updated_items = [item for item in items if item["name"] != selected_name]
                deleted_item = next((item for item in items if item["name"] == selected_name), None)
                if deleted_item:
                    write_audit_log("delete", deleted_item, selected_name)
                save_items(updated_items)
                st.success(f"Item '{selected_name}' deleted successfully.")
                st.session_state.confirm_delete = False

        with col2:
            if st.button("Cancel"):
                st.session_state.confirm_delete = False
                st.rerun()