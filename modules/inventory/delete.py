import streamlit as st
from modules.inventory.inventory_store import get_all_items, _save_data

def render_delete_inventory_item():
    st.header("🗑️ Delete Inventory Item")

    items = get_all_items()
    if not items:
        st.info("No inventory items available.")
        return

    item_options = {f"{item['name']} ({item['category']})": item["id"] for item in items}
    selection = st.selectbox("Select item to delete", list(item_options.keys()))
    item_id = item_options[selection]

    # Use session state to manage confirmation state
    if "confirming_delete" not in st.session_state:
        st.session_state.confirming_delete = False
    if "pending_delete_id" not in st.session_state:
        st.session_state.pending_delete_id = None

    if st.button("Delete Item"):
        st.session_state.confirming_delete = True
        st.session_state.pending_delete_id = item_id
        st.session_state.pending_delete_label = selection

    if st.session_state.confirming_delete and st.session_state.pending_delete_id == item_id:
        st.warning("Are you sure? This cannot be undone.")
        if st.button("Confirm Delete"):
            updated_items = [item for item in items if item["id"] != item_id]
            _save_data(updated_items)
            st.success(f"Item '{selection}' has been permanently deleted.")
            st.session_state.confirming_delete = False
            st.session_state.pending_delete_id = None
            st.session_state.pending_delete_label = None
