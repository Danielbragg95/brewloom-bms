def generate_po_id(existing_records):
    existing_ids = [record["po_id"] for record in existing_records if "po_id" in record]
    next_number = len(existing_ids) + 1
    return f"PO-{next_number:04d}"
