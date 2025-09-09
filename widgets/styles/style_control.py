from PyQt6.QtWidgets import (
    QWidget,
    QComboBox,
    QLabel,
    QHBoxLayout,
    QCheckBox,
    QApplication,
    QStyleFactory,
)


class StyleControls(QWidget):
    """Reusable style control panel"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.originalPalette = QApplication.palette()
        self.setupUI()
        self.connectSignals()

    def setupUI(self):
        self.styleComboBox = QComboBox()
        self.styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("&Style:")
        styleLabel.setBuddy(self.styleComboBox)

        self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
        self.useStylePaletteCheckBox.setChecked(True)

        self.disableWidgetsCheckBox = QCheckBox("&Disable widgets")

        layout = QHBoxLayout()
        layout.addWidget(styleLabel)
        layout.addWidget(self.styleComboBox)
        layout.addStretch(1)
        layout.addWidget(self.useStylePaletteCheckBox)
        layout.addWidget(self.disableWidgetsCheckBox)
        self.setLayout(layout)

    def connectSignals(self):
        self.styleComboBox.textActivated.connect(self.changeStyle)
        self.useStylePaletteCheckBox.toggled.connect(self.changePalette)

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()

    def changePalette(self):
        if self.useStylePaletteCheckBox.isChecked():
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)
