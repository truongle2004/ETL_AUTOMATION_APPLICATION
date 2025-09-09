from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QFrame,
    QSplitter,
    QMainWindow,
)
from PyQt6.QtCore import pyqtSignal, Qt

from widgets.buttons.radio_button import RadioButtonGroup
from widgets.buttons.push_button import PushButtonGroup
from widgets.tables.table_text_tab import TableTextTabWidget
from widgets.inputs.input_control_group import InputControlsGroup
from widgets.progess_bar.animated_progess_bar import AnimatedProgressBar
from widgets.styles.style_control import StyleControls


class ResponsiveDrawer(QFrame):
    """
    Responsive drawer that doesn't overlap content
    """

    # Signals
    opened = pyqtSignal()
    closed = pyqtSignal()

    def __init__(self, parent=None, width=250):
        super().__init__(parent)
        self.drawer_width = width
        self.is_open = False

        self.setupUI()

    def setupUI(self):
        """Setup the drawer UI"""
        self.setFixedWidth(self.drawer_width)
        self.setStyleSheet("""
            ResponsiveDrawer {
                background-color: #f8f9fa;
                border-right: 1px solid #dee2e6;
            }
        """)

        # Layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # Title
        from PyQt6.QtWidgets import QLabel

        title = QLabel("Navigation")
        title.setStyleSheet("font-size: 16px; font-weight: bold; color: #495057;")
        layout.addWidget(title)

        # Menu items
        menu_items = ["Dashboard", "Profile", "Settings", "Reports", "Help"]
        for item in menu_items:
            btn = QPushButton(item)
            btn.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    background-color: #ffffff;
                    border: 1px solid #dee2e6;
                    border-radius: 4px;
                    padding: 10px 15px;
                    margin: 2px 0px;
                }
                QPushButton:hover {
                    background-color: #e9ecef;
                    color: #007bff;
                }
                QPushButton:pressed {
                    background-color: #dee2e6;
                }
            """)
            layout.addWidget(btn)

        # Add stretch to push content to top
        layout.addStretch()

        # Initially hidden
        self.hide()


class SplitterBasedGallery(QMainWindow):
    """Alternative implementation using QSplitter for smooth resizing"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()
        self.connectSignals()
        self.setWindowTitle("Splitter-Based Responsive Gallery")

    def setupUI(self):
        """Setup UI with QSplitter"""

        # Create central widget (required for QMainWindow)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Create horizontal splitter
        self.splitter = QSplitter(Qt.Orientation.Horizontal)

        # Drawer panel
        self.drawer_panel = QFrame()
        self.drawer_panel.setFrameStyle(QFrame.Shape.StyledPanel)
        self.drawer_panel.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border-right: 1px solid #dee2e6;
            }
        """)
        self.setupDrawerPanel()

        # Main content panel
        self.content_panel = QWidget()
        self.setupContentPanel()

        # Add panels to splitter
        self.splitter.addWidget(self.drawer_panel)
        self.splitter.addWidget(self.content_panel)

        # Set initial sizes (drawer: 250px, content: rest)
        self.splitter.setSizes([250, 600])

        # Make splitter handle more visible
        self.splitter.setHandleWidth(3)
        self.splitter.setStyleSheet("""
            QSplitter::handle {
                background-color: #dee2e6;
            }
            QSplitter::handle:hover {
                background-color: #007bff;
            }
        """)

        main_layout.addWidget(self.splitter)

        # Toggle button at top
        toggle_layout = QHBoxLayout()
        self.toggle_btn = QPushButton("Hide Menu")
        self.toggle_btn.setFixedSize(100, 30)
        toggle_layout.addWidget(self.toggle_btn)
        toggle_layout.addStretch()

        main_layout.insertLayout(0, toggle_layout)

    def setupDrawerPanel(self):
        """Setup drawer panel content"""
        layout = QVBoxLayout(self.drawer_panel)

        from PyQt6.QtWidgets import QLabel

        title = QLabel("Navigation")
        title.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
        layout.addWidget(title)

        for i in range(6):
            btn = QPushButton(f"Menu Item {i + 1}")
            layout.addWidget(btn)

        layout.addStretch()

    def setupContentPanel(self):
        """Setup main content panel"""
        content_layout = QGridLayout(self.content_panel)

        # Create components
        self.styleControls = StyleControls()
        self.radioButtonGroup = RadioButtonGroup("Group 1")
        self.pushButtonGroup = PushButtonGroup("Group 2")
        self.tabWidget = TableTextTabWidget()
        self.inputControlsGroup = InputControlsGroup("Group 3")
        self.progressBar = AnimatedProgressBar()

        # Add to layout
        content_layout.addWidget(self.styleControls, 0, 0, 1, 2)
        content_layout.addWidget(self.radioButtonGroup, 1, 0)
        content_layout.addWidget(self.pushButtonGroup, 1, 1)
        content_layout.addWidget(self.tabWidget, 2, 0)
        content_layout.addWidget(self.inputControlsGroup, 2, 1)
        content_layout.addWidget(self.progressBar, 3, 0, 1, 2)

        content_layout.setRowStretch(1, 1)
        content_layout.setRowStretch(2, 1)
        content_layout.setColumnStretch(0, 1)
        content_layout.setColumnStretch(1, 1)

    def connectSignals(self):
        """Connect signals"""
        self.toggle_btn.clicked.connect(self.toggleDrawerPanel)

    def toggleDrawerPanel(self):
        """Toggle drawer panel visibility"""
        if self.drawer_panel.isVisible():
            self.drawer_panel.hide()
            self.toggle_btn.setText("Show Menu")
        else:
            self.drawer_panel.show()
            self.toggle_btn.setText("Hide Menu")


# Example usage
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    # Choose which implementation to use:

    # Option 1: Responsive drawer with hide/show
    # gallery = ModularWidgetGallery()

    # Option 2: Splitter-based (uncomment to use instead)
    gallery = SplitterBasedGallery()

    # Set window size and show (don't use showMaximized initially to see buttons clearly)
    gallery.resize(1000, 700)
    gallery.showMaximized()

    sys.exit(app.exec())
