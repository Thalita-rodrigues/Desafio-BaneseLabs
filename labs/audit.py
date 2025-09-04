import csv, os
from typing import Dict
from datetime import datetime

AUDIT_HEADERS = ["timestamp", "endpoint", "params", "num_records", "user"]

def write_audit(path: str, endpoint: str, params: Dict, num_records: int, user: str = "analyst"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    exists = os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if not exists:
            w.writerow(AUDIT_HEADERS)
        w.writerow([datetime.utcnow().isoformat(), endpoint, str(params), num_records, user])
