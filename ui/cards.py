from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from .theme import Theme

class FeatureCard(QFrame):
    def __init__(self, title: str, description: str, icon_text: str = '•', parent=None):
        super().__init__(parent)
        self.setObjectName('Card')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumHeight(170)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(22, 20, 22, 20)
        layout.setSpacing(10)

        icon = QLabel(icon_text)
        icon.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        icon.setStyleSheet(f'color: {Theme.PRIMARY}; font-size: 24px; font-weight: 700;')

        title_label = QLabel(title)
        title_label.setObjectName('CardTitle')
        title_label.setWordWrap(True)

        desc_label = QLabel(description)
        desc_label.setObjectName('CardText')
        desc_label.setWordWrap(True)

        layout.addWidget(icon)
        layout.addWidget(title_label)
        layout.addWidget(desc_label)
        layout.addStretch(1)

        self._title = title_label
        self._desc = desc_label

    def enterEvent(self, event):
        self.setStyleSheet('QFrame#Card { background: #273449; border: 1px solid #4b6b8a; border-radius: 20px; }')
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet('QFrame#Card { background: #1E293B; border: 1px solid #334155; border-radius: 20px; }')
        super().leaveEvent(event)