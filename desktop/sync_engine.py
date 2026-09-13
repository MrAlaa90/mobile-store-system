import json
import requests
from storage.db import LocalDatabase

class SyncEngine:
    def __init__(self, api_base_url="http://localhost:8000/api/v1/"):
        self.api_url = f"{api_base_url}sync/"
        self.db = LocalDatabase()

    def sync_pending(self):
        records = self.db.get_pending_sync_records()
        if not records:
            return 0

        payload = [
            {
                "id": r["id"],
                "entity_type": r["entity_type"],
                "payload": r["payload"],
                "created_at": r["created_at"]
            }
            for r in records
        ]

        try:
            response = requests.post(self.api_url, json={"records": payload}, timeout=10)
            if response.status_code == 200:
                synced_ids = response.json().get("synced_ids", [])
                with self.db.get_connection() as conn:
                    cursor = conn.cursor()
                    for s_id in synced_ids:
                        cursor.execute("UPDATE sync_outbox SET synced = 1 WHERE id = ?", (s_id,))
                    conn.commit()
                return len(synced_ids)
        except requests.RequestException:
            pass

        return 0
