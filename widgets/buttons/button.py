from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt


class Button(QPushButton):
    """Reusable styled button class with different Material UI themes"""
    THEMES = {
        "primary": {
            "bg": "#1976d2",
            "bg_hover": "#1565c0",
            "bg_pressed": "#0d47a1",
            "fg": "white",
            "disabled_bg": "#90caf9",
            "disabled_fg": "#e0e0e0",
        },
        "secondary": {
            "bg": "#9c27b0",
            "bg_hover": "#7b1fa2",
            "bg_pressed": "#4a148c",
            "fg": "white",
            "disabled_bg": "#ce93d8",
            "disabled_fg": "#f5f5f5",
        },
        "danger": {
            "bg": "#d32f2f",
            "bg_hover": "#c62828",
            "bg_pressed": "#b71c1c",
            "fg": "white",
            "disabled_bg": "#ef9a9a",
            "disabled_fg": "#f5f5f5",
        },
        "outlined": {
            "bg": "transparent",
            "bg_hover": "#eeeeee",
            "bg_pressed": "#e0e0e0",
            "fg": "#1976d2",
            "disabled_bg": "transparent",
            "disabled_fg": "#9e9e9e",
        },
    }

    def __init__(self, text="Button", theme="primary", parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.set_theme(theme)

    def set_theme(self, theme: str):
        """Apply theme from predefined styles"""
        theme_data = self.THEMES.get(theme, self.THEMES["primary"])

        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {theme_data["bg"]};
                color: {theme_data["fg"]};
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: 500;
            }}
            QPushButton:hover {{
                background-color: {theme_data["bg_hover"]};
            }}
            QPushButton:pressed {{
                background-color: {theme_data["bg_pressed"]};
            }}
            QPushButton:disabled {{
                background-color: {theme_data["disabled_bg"]};
                color: {theme_data["disabled_fg"]};
            }}
        """)
