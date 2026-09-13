# Mobile Store Management System (Architecture Specification)

## 1. System Architecture
- Backend Core: Django REST Framework + PostgreSQL.
- Desktop Client: Python + PyQt6 + SQLite (Offline-First POS).
- Web Dashboard: React + Vite + TailwindCSS.
- Mobile App: Flutter (Phase 2).
- Containerization: Docker & Docker-compose.

## 2. Security & Licensing Architecture
- Algorithm: Asymmetric RSA-2048 / Ed25519.
- Backend: Signs license tokens using a private key.
- Desktop: Holds only the public key to verify token integrity and expiration.

## 3. Offline-First & Sync Engine
- Primary Keys: UUIDv4 for ALL models across all clients and server.
- Local Storage: SQLite mirrors schema (Inventory, Sales, Repairs).
- Sync Queue: Transactions saved locally with synced=false, pushed in chronological batches when connection restores.
