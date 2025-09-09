from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QProgressBar


class AnimatedProgressBar(QProgressBar):
    """Reusable progress bar with automatic animation"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()

    def setupUI(self):
        self.setRange(0, 10000)
        self.setValue(0)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.advance)
        self.timer.start(1000)

    def advance(self):
        curVal = self.value()
        maxVal = self.maximum()
        self.setValue(curVal + (maxVal - curVal) // 100)

    def startAnimation(self):
        self.timer.start(1000)

    def stopAnimation(self):
        self.timer.stop()
