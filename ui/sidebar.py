from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QLabel, QSizePolicy, QButtonGroup
from PySide6.QtCore import Qt, Signal

from .theme import Theme

class Sidebar(QFrame):
    section_changed = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('Sidebar')
        self.setMinimumWidth(250)
        self.setMaximumWidth(280)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        self.buttons = {}
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 22, 18, 18)
        layout.setSpacing(10)

        title = QLabel('EcoLens AI')
        title.setStyleSheet('font-size: 22px; font-weight: 800; color: white;')
        subtitle = QLabel('Energy conservation dashboard')
        subtitle.setStyleSheet(f'font-size: 12px; color: {Theme.SUBTEXT};')

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(12)

        self._add_button(layout, 'Dashboard', 'dashboard')
        self._add_button(layout, 'Appliance Scanner', 'scanner')
        self._add_button(layout, 'Standby Checker', 'standby')
        self._add_button(layout, 'Solar Advisor', 'solar')
        self._add_button(layout, 'Reports', 'reports')
        self._add_button(layout, 'Settings', 'settings')
        self._add_button(layout, 'About', 'about')

        layout.addStretch(1)

        footer = QLabel('Offline desktop edition')
        footer.setStyleSheet(f'font-size: 11px; color: {Theme.SUBTEXT};')
        layout.addWidget(footer)

        self.set_active('Dashboard')

    def _add_button(self, layout, text, key):
        button = QPushButton(text)
        button.setCheckable(True)
        button.setCursor(Qt.PointingHandCursor)
        button.setMinimumHeight(44)
        button.clicked.connect(lambda: self.section_changed.emit(text))
        self.button_group.addButton(button)
        self.buttons[text] = button
        layout.addWidget(button)

    def set_active(self, name):
        for text, button in self.buttons.items():
            is_active = text == name
            button.setChecked(is_active)
            if is_active:
                button.setStyleSheet(f'''
                    QPushButton {{
                        background: {Theme.PRIMARY};
                        color: #0B1220;
                        border-radius: 14px;
                        font-weight: 700;
                        text-align: left;
                        padding-left: 16px;
                    }}
                    QPushButton:hover {{
                        background: #4ade80;
                    }}
                ''')
            else:
                button.setStyleSheet('')