from PyQt6.QtWidgets import QPushButton, QGroupBox, QVBoxLayout


class PushButtonGroup(QGroupBox):
    """Reusable group box with different push button types"""

    def __init__(self, title="Group 2", parent=None):
        super().__init__(title, parent)
        self.setupUI()

    def setupUI(self):
        self.defaultPushButton = QPushButton("Default Push Button")
        self.defaultPushButton.setDefault(True)

        self.togglePushButton = QPushButton("Toggle Push Button")
        self.togglePushButton.setCheckable(True)
        self.togglePushButton.setChecked(True)

        self.flatPushButton = QPushButton("Flat Push Button")
        self.flatPushButton.setFlat(True)

        layout = QVBoxLayout()
        layout.addWidget(self.defaultPushButton)
        layout.addWidget(self.togglePushButton)
        layout.addWidget(self.flatPushButton)
        layout.addStretch(1)
        self.setLayout(layout)
