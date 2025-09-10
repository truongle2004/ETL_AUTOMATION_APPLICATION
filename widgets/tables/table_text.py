import re
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTextEdit,
                             QSizePolicy, QPushButton, QCheckBox)


class TableTextWidget(QWidget):
    """Reusable widget with text edit that auto-doubles curly brackets on typing/pasting"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()

    def setupUI(self):
        # Size policy for the widget
        self.setSizePolicy(QSizePolicy.Policy.Expanding,
                           QSizePolicy.Policy.Expanding)

        # Buttons with tooltips
        self.btn_clear = QPushButton("Clear")
        self.btn_clear.setToolTip("Clear all text in the editor")
        self.btn_clear.clicked.connect(self.clear_text)

        self.btn_copy = QPushButton("Copy")
        self.btn_copy.setToolTip("Copy all text to clipboard")
        self.btn_copy.clicked.connect(self.copy_all_text)

        # Fix braces button (manual doubling of single braces)
        self.btn_fix_braces = QPushButton("Fix Braces")
        self.btn_fix_braces.setToolTip(
            "Double all single curly brackets { } to {{ }}")
        self.btn_fix_braces.clicked.connect(self.double_curly_brackets)

        # Auto-double checkbox
        self.chk_auto_double = QCheckBox("Auto-double { } as you type")
        self.chk_auto_double.setChecked(True)  # Enabled by default
        self.chk_auto_double.setToolTip(
            "Toggle automatic doubling of curly brackets")

        # Text edit setup (custom subclass for auto-doubling)
        self.textEdit = CustomTextEdit(self)
        self.textEdit.setPlainText(
            "Twinkle, twinkle, little star,\n"
            "How I wonder what you are.\n"
            "Up above the world so high,\n"
            "Like a diamond in the sky.\n"
            "Twinkle, twinkle, little star,\n"
            "How I wonder what you are!\n"
        )
        self.textEdit.setPlaceholderText("Enter or paste text here...")
        self.textEdit.setFont(QFont("Arial", 12))  # Clean, readable font
        self.textEdit.setLineWrapMode(
            QTextEdit.LineWrapMode.WidgetWidth)  # Word wrap
        self.textEdit.setAcceptRichText(False)  # Plain text only
        self.textEdit.textChanged.connect(self.update_button_states)
        self.textEdit.set_auto_double_checkbox(self.chk_auto_double)

        self.textEdit.setTabStopDistance(40)  # Set tab width to 40 pixels

        # Button layout (horizontal)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.btn_clear)
        button_layout.addWidget(self.btn_copy)
        button_layout.addWidget(self.btn_fix_braces)
        button_layout.addWidget(self.chk_auto_double)  # Add checkbox
        button_layout.addStretch()  # Push to left

        # Main layout (vertical)
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(8)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.textEdit)
        main_layout.addStretch()

        # Initial button state
        self.update_button_states()

    def clear_text(self):
        self.textEdit.clear()
        self.textEdit.setFocus()

    def copy_all_text(self):
        self.textEdit.selectAll()
        self.textEdit.copy()
        self.textEdit.textCursor().clearSelection()
        self.textEdit.setFocus()

    def update_button_states(self):
        """Enable/disable buttons based on text content"""
        has_text = bool(self.textEdit.toPlainText().strip())
        self.btn_clear.setEnabled(has_text)
        self.btn_copy.setEnabled(has_text)
        # Enable fix button if single braces exist
        text = self.textEdit.toPlainText()
        # Match { or } not preceded/followed by another
        has_single_braces = bool(
            re.search(r'(?<!\{)\{(?!\{)|(?<!\})\}(?!\})', text))
        self.btn_fix_braces.setEnabled(has_text and has_single_braces)

    def double_curly_brackets(self):
        """Manual: Double all single curly brackets in full text"""
        text = self.textEdit.toPlainText()
        # print(f"Manual fix - Original text: {text}")

        # Double single { to {{ and } to }}, avoiding existing doubles
        cleaned_text = re.sub(
            r'(?<!\{)\{(?!\{)', '{{', re.sub(r'(?<!\})\}(?!\})', '}}', text))

        # print(f"Manual fix - Doubled text: {cleaned_text}")

        self.textEdit.setPlainText(cleaned_text)
        self.update_button_states()
        self.textEdit.setFocus()


class CustomTextEdit(QTextEdit):
    """Custom QTextEdit that auto-doubles curly brackets on typing/pasting"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.auto_double_checkbox = None

    def set_auto_double_checkbox(self, checkbox):
        self.auto_double_checkbox = checkbox

    def keyPressEvent(self, event):
        """Auto-double { to {{ and } to }} when typing"""
        if not self.auto_double_checkbox or not self.auto_double_checkbox.isChecked():
            super().keyPressEvent(event)
            return

        char = event.text()
        # print(f"char {char}")
        if char == '{':
            cursor = self.textCursor()
            pos = cursor.position()

            # Insert double braces instead of single
            double_char = '{}'
            cursor.insertText(double_char)

            # Move cursor between the braces (e.g., {{|}})
            cursor.setPosition(pos + 1)
            self.setTextCursor(cursor)

            # print(f"Auto-doubled {char} to {double_char} at position {pos}")
        else:
            super().keyPressEvent(event)

    def insertFromMimeData(self, source):
        """Auto-double braces in pasted text"""
        if not self.auto_double_checkbox or not self.auto_double_checkbox.isChecked():
            super().insertFromMimeData(source)
            return

        pasted_text = source.text().strip()
        if not pasted_text:
            super().insertFromMimeData(source)
            return

        # Double single braces in pasted text
        cleaned_paste = re.sub(
            r'(?<!\{)\{(?!\{)', '{{', re.sub(r'(?<!\})\}(?!\})', '}}', pasted_text))
        # print(f"Auto-doubled pasted text: {pasted_text} -> {cleaned_paste}")

        # Insert cleaned text
        cursor = self.textCursor()
        cursor.insertText(cleaned_paste)
        self.setTextCursor(cursor)
