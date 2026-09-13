# Mobile Store Management System (Architecture Specification)

## 1. System Architecture
- **Backend Core:** Django REST Framework + PostgreSQL (Single Source of Truth).
- **Desktop Client:** Python + PyQt6 + SQLite (Offline-First POS).
- **Web Dashboard:** React (TypeScript) + Vite + TailwindCSS (Management & Analytics).
- **Mobile App:** Flutter (Android/iOS) - Phase 2.
- **Containerization:** Docker & Docker-compose (Backend + Database).

## 2. Security & Licensing Architecture
- **Algorithm:** Asymmetric RSA-2048 / Ed25519.
- **Backend:** Signs license tokens using a securely held Private Key.
- **Desktop/Client:** Holds only the Public Key to verify token integrity and expiration.
- **Remote Kill:** Blacklist check via periodic heartbeat when internet is available.

## 3. Offline-First & Sync Engine
- **Primary Keys:** UUIDv4 for ALL models across all clients and server to eliminate ID collisions during sync.
- **Local Storage (Desktop):** SQLite mirrors required schema (Inventory, Sales, Repairs).
- **Sync Queue (Outbox Pattern):**
  - Offline transactions are saved locally with `synced: false` and a UTC timestamp.
  - When connection is detected, transactions are pushed in chronological batches to `/api/v1/sync/`.
  - Conflict Resolution: Server timestamp takes precedence for inventory updates; sales events are strictly append-only.

## 4. Database Core Entities (UUID-based)
- Users (id, username, email, role)
- Licenses (id, user_id, license_key, public_token, valid_until, status)
- Devices (id, license_id, hardware_fingerprint, last_seen)
- Inventory (id, name, sku, purchase_price, sale_price, stock_quantity, updated_at)
- Sales (id, device_id, total_amount, profit, created_at, synced)
- Repairs (id, customer_id, device_info, cost, payment, status, created_at, synced)
- Customers (id, name, phone, email, created_at)
