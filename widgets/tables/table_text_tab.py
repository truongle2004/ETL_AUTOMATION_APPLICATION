from PyQt6.QtWidgets import (
    QTabWidget,
    QWidget,
    QHBoxLayout,
    QTableWidget,
    QTextEdit,
    QSizePolicy,
)


class TableTextTabWidget(QTabWidget):
    """Reusable tab widget with table and text edit tabs"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()

    def setupUI(self):
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)

        # Table tab
        tab1 = QWidget()
        self.tableWidget = QTableWidget(10, 10)
        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(self.tableWidget)
        tab1.setLayout(tab1hbox)

        # Text edit tab
        tab2 = QWidget()
        self.textEdit = QTextEdit()
        self.textEdit.setPlainText(
            "Twinkle, twinkle, little star,\n"
            "How I wonder what you are.\n"
            "Up above the world so high,\n"
            "Like a diamond in the sky.\n"
            "Twinkle, twinkle, little star,\n"
            "How I wonder what you are!\n"
        )

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(self.textEdit)
        tab2.setLayout(tab2hbox)

        self.addTab(tab1, "&Table")
        self.addTab(tab2, "Text &Edit")
