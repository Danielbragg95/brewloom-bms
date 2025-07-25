import streamlit as st
import uuid
from modules.inventory.inventory_store import add_item

CATEGORY_STRUCTURE = {
    "Ingredients": {
        "Grain": "lbs",
        "Hops": "oz",
        "Yeast": "g"
    },
    "Packaging": {
        "Bottles": "ea",
        "Cans": "ea",
        "Labels": "rolls"
    },
    "Custodial Supplies": {
        "Cleaner": "gal",
        "Paper Towels": "rolls",
        "Gloves": "box"
    }
}

def render_add_inventory_item():
    st.header("➕ Add Inventory Item")

    if "selected_category" not in st.session_state:
        st.session_state.selected_category = list(CATEGORY_STRUCTURE.keys())[0]

    # Let user select category (outside form so it triggers rerender)
    st.session_state.selected_category = st.selectbox(
        "Main Category", list(CATEGORY_STRUCTURE.keys()), index=list(CATEGORY_STRUCTURE.keys()).index(st.session_state.selected_category)
    )

    subcategory_options = list(CATEGORY_STRUCTURE[st.session_state.selected_category].keys())

    with st.form("add_inventory_form"):
        name = st.text_input("Item Name")

        subcategory = st.selectbox("Subcategory", subcategory_options)
        unit_default = CATEGORY_STRUCTURE[st.session_state.selected_category][subcategory]
        quantity = st.number_input("Quantity", min_value=0.0, step=0.5)
        unit = st.text_input("Unit", value=unit_default)
        threshold = st.number_input("Reorder Threshold", min_value=0.0, step=0.5)

        submitted = st.form_submit_button("Add Item")
        if submitted:
            if not name:
                st.warning("Item name is required.")
            else:
                item_data = {
                    "id": str(uuid.uuid4()),
                    "name": name,
                    "category": st.session_state.selected_category,
                    "subcategory": subcategory,
                    "quantity": quantity,
                    "unit": unit,
                    "threshold": threshold
                }
                add_item(item_data)
                st.success(f"Item '{name}' added to inventory.")
