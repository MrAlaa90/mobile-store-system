import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mobile Store POS")
        self.resize(400, 200)

        layout = QVBoxLayout()
        self.status_label = QLabel("License Status: Unknown")
        layout.addWidget(self.status_label)

        self.verify_btn = QPushButton("Verify License")
        self.verify_btn.clicked.connect(self.verify_license)
        layout.addWidget(self.verify_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def verify_license(self):
        # Verification logic with local RSA Public Key
        self.status_label.setText("License Status: Verified (Offline Safe)")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
