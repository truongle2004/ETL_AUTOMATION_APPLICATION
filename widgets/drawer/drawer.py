from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel, QPushButton


class Drawer(QFrame):
    """
    Simple drawer that shows/hides on the left side
    """

    def __init__(self, parent=None, width=250):
        super().__init__(parent)
        self.parent_widget = parent
        self.width = width
        self.is_open = False

        self.setupUI()
        self.hide()  # Start hidden

    def setupUI(self):
        """Setup the drawer"""
        # Set size and style
        self.setFixedWidth(self.width)
        self.setStyleSheet("""
            Drawer {
                background-color: #f0f0f0;
                border-right: 1px solid #ccc;
            }
        """)

        # Layout
        layout = QVBoxLayout(self)

        # Title
        title = QLabel("Drawer")
        title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        layout.addWidget(title)

        # Add some buttons
        for i in range(5):
            btn = QPushButton(f"Item {i + 1}")
            layout.addWidget(btn)

        layout.addStretch()

    def toggle(self):
        """Show or hide the drawer"""
        if self.is_open:
            self.hide()
            self.is_open = False
        else:
            # Position drawer
            if self.parent_widget:
                parent_rect = self.parent_widget.rect()
                self.setGeometry(0, 0, self.width, parent_rect.height())
            self.show()
            self.is_open = True

    def open(self):
        """Open the drawer"""
        if not self.is_open:
            self.toggle()

    def close(self):
        """Close the drawer"""
        if self.is_open:
            self.toggle()
