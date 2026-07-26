from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QStackedWidget, QLabel, QStatusBar
from PySide6.QtCore import Qt

from .theme import Theme
from .sidebar import Sidebar
from .dashboard import DashboardPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('EcoLens AI')
        self.resize(1400, 850)
        self.setMinimumSize(1200, 700)
        self.setStyleSheet(Theme.stylesheet())

        central = QWidget()
        self.setCentralWidget(central)

        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        self.sidebar = Sidebar()
        self.sidebar.section_changed.connect(self.on_section_changed)
        root.addWidget(self.sidebar)

        self.stack = QStackedWidget()
        self.stack.addWidget(self._placeholder('Dashboard'))
        self.stack.addWidget(self._placeholder('Appliance Scanner'))
        self.stack.addWidget(self._placeholder('Standby Checker'))
        self.stack.addWidget(self._placeholder('Solar Advisor'))
        self.stack.addWidget(self._placeholder('Reports'))
        self.stack.addWidget(self._placeholder('Settings'))
        self.stack.addWidget(self._placeholder('About'))
        self.stack.insertWidget(0, DashboardPage())
        root.addWidget(self.stack, 1)

        status = QStatusBar()
        status.showMessage('Ready. Stage 1 interface loaded.')
        self.setStatusBar(status)

    def _placeholder(self, title):
        page = QWidget()
        layout = QHBoxLayout(page)
        label = QLabel(f'{title} coming soon')
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        return page

    def on_section_changed(self, name):
        self.sidebar.set_active(name)
        mapping = {
            'Dashboard': 0,
            'Appliance Scanner': 1,
            'Standby Checker': 2,
            'Solar Advisor': 3,
            'Reports': 4,
            'Settings': 5,
            'About': 6,
        }
        self.stack.setCurrentIndex(mapping.get(name, 0))