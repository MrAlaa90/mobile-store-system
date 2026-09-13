# Database Design Constraints

1. Primary Keys: All tables must use UUIDv4 to support offline replication.
2. Tables:
   - users (id, username, password_hash, role, created_at)
   - licenses (id, user_id, license_key, public_token, valid_until, status)
   - devices (id, license_id, hardware_hash, last_seen)
   - inventory (id, name, brand, model, purchase_price, sale_price, stock, updated_at)
   - sales (id, device_id, total_amount, profit, created_at, synced)
   - repairs (id, customer_id, device_info, cost, payment, status, created_at, synced)
   - customers (id, name, phone, email, created_at)
3. Licensing Algorithm:
   - Server signs payload (device_id + expiry) with private RSA key.
   - Desktop verifies signature using public RSA key stored in desktop/keys/public.pem.
