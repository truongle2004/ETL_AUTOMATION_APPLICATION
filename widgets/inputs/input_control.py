from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel


class SingleInputControl(QWidget):
    """Reusable widget with a labeled text input control (Material UI style)."""

    def __init__(
        self,
        parent=None,
        label_text: str = "Input:",
        default_text: str = "",
        is_password: bool = False,
    ):
        """Initialize the widget with a label text, default text, and optional password mode."""
        super().__init__(parent)
        self.setupUI(label_text, default_text, is_password)
        self.apply_style()

    def setupUI(self, label_text, default_text, is_password):
        """Set up the UI with a QLabel and QLineEdit."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        # Label
        self.label = QLabel(label_text)
        layout.addWidget(self.label)

        # Text input
        self.lineEdit = QLineEdit(default_text)
        self.lineEdit.setPlaceholderText("Enter url here")
        if is_password:
            self.lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.lineEdit)

    def apply_style(self):
        """Apply Material UI-like style to label and input field."""
        self.label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #555;   /* Subtle gray like MUI label */
                font-weight: 500;
            }
        """)

        self.lineEdit.setStyleSheet("""
            QLineEdit {
                border: 2px solid #cfd8dc;   /* Light gray border */
                border-radius: 6px;
                padding: 6px 10px;
                font-size: 14px;
                selection-background-color: #1976d2;
            }
            QLineEdit:focus {
                border: 2px solid #1976d2;   /* Blue highlight */
                outline: none;
            }
            QLineEdit:disabled {
                background-color: #f5f5f5;
                color: #9e9e9e;
                border: 2px solid #e0e0e0;
            }
        """)

    def get_text(self):
        """Return the current text in the input field."""
        return self.lineEdit.text()

    def set_text(self, text):
        """Set the text in the input field."""
        self.lineEdit.setText(text)

    def set_label_text(self, text):
        """Set the text of the label."""
        self.label.setText(text)
