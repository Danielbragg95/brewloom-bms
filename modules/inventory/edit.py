import streamlit as st
from modules.inventory.inventory_store import get_all_items, _save_data
from modules.inventory.audit_utils import write_audit_log
from modules.inventory.inventory_item import InventoryItem

def render_edit_inventory_item():
    st.header("✏️ Edit Inventory Item")

    items = get_all_items()
    if not items:
        st.info("No inventory items found.")
        return

    item_options = {f"{item['name']} ({item['category']})": item for item in items}
    selected_label = st.selectbox("Select item to edit", list(item_options.keys()))
    selected = item_options[selected_label]

    with st.form("edit_item_form"):
        name = st.text_input("Item Name", value=selected["name"])
        category = st.selectbox("Category", [
            "Grain", "Hops", "Yeast", "Adjuncts",
            "Packaging", "Cleaning Supplies",
            "Raw Materials", "Finished Goods", "Other"
        ], index=[
            "Grain", "Hops", "Yeast", "Adjuncts",
            "Packaging", "Cleaning Supplies",
            "Raw Materials", "Finished Goods", "Other"
        ].index(selected["category"]) if selected["category"] in [
            "Grain", "Hops", "Yeast", "Adjuncts",
            "Packaging", "Cleaning Supplies",
            "Raw Materials", "Finished Goods", "Other"
        ] else 0)
        unit = st.text_input("Unit (e.g. lbs, oz, gal)", value=selected["unit"])
        threshold = st.number_input("Reorder Threshold", min_value=0.0, step=0.5, value=selected["threshold"])
        submitted = st.form_submit_button("Update Item")

        if submitted:
            for item in items:
                if item["id"] == selected["id"]:
                    item["name"] = name
                    item["category"] = category
                    item["unit"] = unit
                    item["threshold"] = threshold
                    break
            _save_data(items)
            write_audit_log('edit', selected['id'], selected['name'], before=selected, after=item)
            st.success("Item updated successfully!")
