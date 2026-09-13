import sqlite3
import uuid
from datetime import datetime

class LocalDatabase:
    def __init__(self, db_path="local_storage.db"):
        self.db_path = db_path
        self.init_schema()

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_schema(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS local_license (
                    id TEXT PRIMARY KEY,
                    license_key TEXT,
                    token TEXT,
                    valid_until TEXT,
                    verified_at TEXT
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS local_inventory (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    brand TEXT,
                    model TEXT,
                    sale_price REAL,
                    stock INTEGER
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sync_outbox (
                    id TEXT PRIMARY KEY,
                    entity_type TEXT,
                    payload TEXT,
                    created_at TEXT,
                    synced INTEGER DEFAULT 0
                );
            """)
            conn.commit()

    def queue_transaction(self, entity_type: str, payload_json: str):
        record_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO sync_outbox (id, entity_type, payload, created_at, synced)
                VALUES (?, ?, ?, ?, 0)
            """, (record_id, entity_type, payload_json, timestamp))
            conn.commit()
        return record_id

    def get_pending_sync_records(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sync_outbox WHERE synced = 0 ORDER BY created_at ASC")
            return cursor.fetchall()
