from PyQt6.QtWidgets import QComboBox
from PyQt6.QtCore import Qt


class Dropdown(QComboBox):
    """Reusable styled dropdown (Material UI style)."""

    def __init__(self, parent=None, items=None, placeholder="Select an option"):
        super().__init__(parent)

        # Add placeholder (disabled item at index 0)
        if placeholder:
            self.addItem(placeholder)
            self.setCurrentIndex(0)
            self.model().item(0).setEnabled(False)

        # Add items
        if items:
            self.addItems(items)

        # Apply Material-like style
        self.setStyleSheet("""
            QComboBox {
                border: 2px solid #cfd8dc;
                border-radius: 6px;
                padding: 6px 10px;
                font-size: 14px;
                min-width: 150px;
                background: white;
            }
            QComboBox:focus {
                border: 2px solid #1976d2; /* Blue border on focus */
            }
            QComboBox::drop-down {
                border: none;
                width: 25px;
            }
            QComboBox::down-arrow {
                image: url(:/qt-project.org/styles/commonstyle/images/arrowdown-16.png);
                width: 12px;
                height: 12px;
            }
            QComboBox QAbstractItemView {
                border: 1px solid #cfd8dc;
                border-radius: 4px;
                selection-background-color: #1976d2;
                selection-color: white;
                padding: 4px;
            }
        """)

        # Cursor change
        self.setCursor(Qt.CursorShape.PointingHandCursor)
