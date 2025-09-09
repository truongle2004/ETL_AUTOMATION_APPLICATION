from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGroupBox, QRadioButton, QVBoxLayout, QCheckBox


class RadioButtonGroup(QGroupBox):
    """Reusable group box with radio buttons and checkbox"""

    def __init__(self, title="Group 1", parent=None):
        super().__init__(title, parent)
        self.setupUI()

    def setupUI(self):
        self.radioButton1 = QRadioButton("Radio button 1")
        self.radioButton2 = QRadioButton("Radio button 2")
        self.radioButton3 = QRadioButton("Radio button 3")
        self.radioButton1.setChecked(True)

        self.checkBox = QCheckBox("Tri-state check box")
        self.checkBox.setTristate(True)
        self.checkBox.setCheckState(Qt.CheckState.PartiallyChecked)

        layout = QVBoxLayout()
        layout.addWidget(self.radioButton1)
        layout.addWidget(self.radioButton2)
        layout.addWidget(self.radioButton3)
        layout.addWidget(self.checkBox)
        layout.addStretch(1)
        self.setLayout(layout)
