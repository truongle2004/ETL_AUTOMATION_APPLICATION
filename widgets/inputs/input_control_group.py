from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtWidgets import (
    QGroupBox,
    QGridLayout,
    QLineEdit,
    QSpinBox,
    QDateTimeEdit,
    QSlider,
    QScrollBar,
    QDial,
)


class InputControlsGroup(QGroupBox):
    """Reusable group box with various input controls"""

    def __init__(self, title="Group 3", parent=None):
        super().__init__(title, parent)
        self.setCheckable(True)
        self.setChecked(True)
        self.setupUI()

    def setupUI(self):
        self.lineEdit = QLineEdit("s3cRe7")
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.spinBox = QSpinBox()
        self.spinBox.setValue(50)

        self.dateTimeEdit = QDateTimeEdit()
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setValue(40)

        self.scrollBar = QScrollBar(Qt.Orientation.Horizontal)
        self.scrollBar.setValue(60)

        self.dial = QDial()
        self.dial.setValue(30)
        self.dial.setNotchesVisible(True)

        layout = QGridLayout()
        layout.addWidget(self.lineEdit, 0, 0, 1, 2)
        layout.addWidget(self.spinBox, 1, 0, 1, 2)
        layout.addWidget(self.dateTimeEdit, 2, 0, 1, 2)
        layout.addWidget(self.slider, 3, 0)
        layout.addWidget(self.scrollBar, 4, 0)
        layout.addWidget(self.dial, 3, 1, 2, 1)
        layout.setRowStretch(5, 1)
        self.setLayout(layout)
