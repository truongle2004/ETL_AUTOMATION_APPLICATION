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
    QSizePolicy,
    QLabel,
)
from PyQt6.QtCore import pyqtSignal, Qt
import sys
import threading

from widgets.inputs.input_control import SingleInputControl as InputControl
from widgets.buttons.button import Button
from widgets.tables.table_text import TableTextWidget
from widgets.dropdown.dropdown import Dropdown
from usecases.impl.fetch_url_use_case_impl import FetchUrlUseCaseImpl as fuUseCase
from usecases.impl.convert_into_beautifulsoup_use_case_impl import (
    ConvertIntoBeautifulSoupUseCaseImpl as cibsuUseCase,
)
from usecases.impl.get_one_tag_use_case_impl import GetOneTagUseCaseImpl as gotuUseCase
from interface_adapter.controller.controller import Controller


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

    def __init__(self, parent=None, controller: Controller = None):
        super().__init__(parent)

        self.controller = controller

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
        self.drawer_panel.hide()

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

        self.table_text = TableTextWidget(controller=self.controller)

        # Create components
        self.dropdown = Dropdown(
            items=["Option 1", "Option 2", "Option 3"], placeholder="Choose..."
        )

        self.singleInputControl = InputControl(
            label_text="Enter Url here:",
            is_password=False,
        )

        self.button_submit = Button("Submit", theme="primary")
        # TODO: add detach enter button keymap
        self.button_submit.setFixedSize(100, 30)

        self.button_submit.clicked.connect(self.on_submit_clicked)

        self.singleInputControl.setSizePolicy(
            self.singleInputControl.sizePolicy().horizontalPolicy(),
            QSizePolicy.Policy.Fixed,
        )

        # Now add widgets in proper rows
        content_layout.addWidget(
            self.singleInputControl, 0, 0, alignment=Qt.AlignmentFlag.AlignTop
        )
        content_layout.addWidget(
            self.button_submit, 1, 0, alignment=Qt.AlignmentFlag.AlignTop
        )
        content_layout.addWidget(
            self.dropdown, 2, 0, alignment=Qt.AlignmentFlag.AlignTop
        )
        content_layout.addWidget(
            self.table_text, 3, 0, alignment=Qt.AlignmentFlag.AlignTop
        )
        content_layout.setRowStretch(5, 1)

    def dropdown_changed(self):
        """this dropdown will handle widget change"""
        # TODO
        pass

    def on_submit_clicked(self):
        url = self.singleInputControl.get_text()

        thread = threading.Thread(target=self.controller.fetch_url, args=(url,))
        thread.start()

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

    def action_add_new_table_text(self):
        """Add new table text"""
        # TODO
        pass


if __name__ == "__main__":
    fetch_url_use_case = fuUseCase()
    convert_into_beautifulsoup_use_case = cibsuUseCase()
    get_one_tag_use_case = gotuUseCase()

    controller = Controller(
        fetch_url_use_case=fetch_url_use_case,
        convert_into_beautifulsoup_use_case=convert_into_beautifulsoup_use_case,
        get_one_tag_use_case=get_one_tag_use_case,
    )
    app = QApplication(sys.argv)
    gallery = SplitterBasedGallery(controller=controller)
    gallery.resize(1000, 700)
    gallery.show()

    sys.exit(app.exec())
