import streamlit as st
import json
import os
import uuid

VENDOR_FILE = "data/vendors.json"

def load_vendors():
    if not os.path.exists(VENDOR_FILE):
        return []
    with open(VENDOR_FILE, "r") as f:
        return json.load(f)

def save_vendors(data):
    with open(VENDOR_FILE, "w") as f:
        json.dump(data, f, indent=2)

def render_vendor_directory():
    st.header("📇 Vendor Directory")

    vendors = load_vendors()
    st.subheader("Add New Vendor")
    with st.form("add_vendor_form"):
        name = st.text_input("Vendor Name")
        contact_name = st.text_input("Contact Name")

        col1, col2 = st.columns(2)
        email = col1.text_input("Email")
        phone = col2.text_input("Phone")

        address = st.text_input("Street Address")

        col3, col4, col5 = st.columns([2, 1, 1])
        city = col3.text_input("City")
        state = col4.text_input("State")
        zip_code = col5.text_input("Zip Code")

        payment_terms = st.selectbox("Payment Terms", ["Due on Receipt", "Net 15", "Net 30", "Net 45", "Net 60"], index=2)
        notes = st.text_area("Internal Notes")
        submitted = st.form_submit_button("Add Vendor")

        if submitted:
            if not name:
                st.warning("Vendor name is required.")
            else:
                vendors.append({
                    "id": str(uuid.uuid4()),
                    "name": name,
                    "contact_name": contact_name,
                    "email": email,
                    "phone": phone,
                    "address": address,
                    "city": city,
                    "state": state,
                    "zip": zip_code,
                    "payment_terms": payment_terms,
                    "notes": notes,
                    "active": True
                })
                save_vendors(vendors)
                st.success(f"Vendor '{name}' added.")

    st.subheader("Existing Vendors")
    if not vendors:
        st.info("No vendors added yet.")
    else:
        for v in vendors:
            st.markdown(f"**{v['name']}**")
            st.markdown(f"- Contact: {v.get('contact_name', '')}")
            st.markdown(f"- Email: {v.get('email', '')}")
            st.markdown(f"- Phone: {v.get('phone', '')}")
            st.markdown(f"- Address: {v.get('address', '')}, {v.get('city', '')}, {v.get('state', '')} {v.get('zip', '')}")
            st.markdown(f"- Payment Terms: {v.get('payment_terms', '')}")
            st.markdown(f"- Active: {'✅' if v.get('active', True) else '❌'}")
            if v.get("notes"):
                st.markdown(f"> _{v['notes']}_")
            st.markdown("---")
