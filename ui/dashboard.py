from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QSizePolicy
from PySide6.QtCore import Qt

from .cards import FeatureCard
from .theme import Theme

class DashboardPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        root = QVBoxLayout(self)
        root.setContentsMargins(28, 24, 28, 24)
        root.setSpacing(18)

        title = QLabel('Welcome to EcoLens AI')
        title.setObjectName('TitleLabel')
        subtitle = QLabel('Monitor your electricity usage, reduce energy waste, and discover smarter ways to save power.')
        subtitle.setObjectName('SubtitleLabel')
        subtitle.setWordWrap(True)

        root.addWidget(title)
        root.addWidget(subtitle)

        cards_row = QHBoxLayout()
        cards_row.setSpacing(16)
        cards_row.addWidget(FeatureCard('Appliance Scanner', 'Identify appliances from an uploaded image and estimate electricity usage.', '🔍'))
        cards_row.addWidget(FeatureCard('Standby Power Checker', 'Find hidden standby losses from devices left plugged in all day.', '⚡'))
        cards_row.addWidget(FeatureCard('Solar Advisor', 'Estimate solar savings, panel count, and payback potential.', '☀'))
        cards_row.addWidget(FeatureCard('Energy Dashboard', 'View total usage, savings, and efficiency score in one place.', '📊'))
        root.addLayout(cards_row)

        activity = QFrame()
        activity.setObjectName('Card')
        activity_layout = QVBoxLayout(activity)
        activity_layout.setContentsMargins(22, 20, 22, 20)
        activity_layout.setSpacing(8)

        activity_title = QLabel('Recent Activity')
        activity_title.setObjectName('CardTitle')
        activity_text = QLabel('No scans yet. Your energy insights will appear here once modules are connected.')
        activity_text.setObjectName('CardText')
        activity_text.setWordWrap(True)

        activity_layout.addWidget(activity_title)
        activity_layout.addWidget(activity_text)
        root.addWidget(activity)
        root.addStretch(1)