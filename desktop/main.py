import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox
from storage.db import LocalDatabase
from licensing.verifier import LicenseVerifier
from sync_engine import SyncEngine

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mobile Store POS")
        self.resize(450, 250)

        self.db = LocalDatabase()
        self.sync_engine = SyncEngine()

        layout = QVBoxLayout()
        self.status_label = QLabel("License Status: Not Verified")
        layout.addWidget(self.status_label)

        self.verify_btn = QPushButton("Verify Offline License")
        self.verify_btn.clicked.connect(self.verify_license)
        layout.addWidget(self.verify_btn)

        self.sync_btn = QPushButton("Sync Offline Transactions")
        self.sync_btn.clicked.connect(self.run_sync)
        layout.addWidget(self.sync_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def verify_license(self):
        key_path = os.path.join(os.path.dirname(__file__), "keys", "public_key.pem")
        if not os.path.exists(key_path):
            QMessageBox.critical(self, "Error", "Public key missing in desktop/keys/")
            return

        verifier = LicenseVerifier(key_path)
        self.status_label.setText("License Engine: Ready (RSA Key Loaded)")

    def run_sync(self):
        count = self.sync_engine.sync_pending()
        QMessageBox.information(self, "Sync Engine", f"Synchronized {count} transactions successfully.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
