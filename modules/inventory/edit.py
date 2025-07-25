import streamlit as st
from modules.inventory.inventory_store import get_all_items, save_items

def render_edit_inventory_item():
    st.header("✏️ Edit Inventory Item")

    inventory = get_all_items()
    item_names = [item["name"] for item in inventory]

    selected_item_name = st.selectbox("Select an item to edit", item_names)
    selected_item = next((item for item in inventory if item["name"] == selected_item_name), None)

    if selected_item:
        name = st.text_input("Item Name", value=selected_item["name"])
        category = st.text_input("Category", value=selected_item["category"])
        subcategory = st.text_input("Subcategory", value=selected_item.get("subcategory", ""))
        quantity = st.number_input("Quantity", value=float(selected_item["quantity"]), step=0.1)
        unit = st.text_input("Unit", value=selected_item["unit"])
        threshold = st.number_input("Threshold", value=float(selected_item.get("threshold", 0)), step=0.1)

        if st.button("Save Changes"):
            selected_item.update({
                "name": name,
                "category": category,
                "subcategory": subcategory,
                "quantity": quantity,
                "unit": unit,
                "threshold": threshold
            })
            save_items(inventory)
            st.success("Item updated successfully.")
