from PyQt6.QtWidgets import QWidget, QVBoxLayout

from widgets.tables.table_text import TableTextWidget


class HtmlStructureView(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.tabWidget = TableTextWidget(self)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tabWidget)
