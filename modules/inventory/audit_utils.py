import json
import os
from datetime import datetime

LOG_FILE = "data/audit_log.json"

def write_audit_log(action, item_id, item_name, before=None, after=None):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "action": action,
        "item_id": item_id,
        "item_name": item_name,
        "before": before,
        "after": after
    }

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)
