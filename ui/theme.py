from PySide6.QtGui import QColor, QFont

class Theme:
    BG = '#0F172A'
    SIDEBAR = '#111827'
    CARD = '#1E293B'
    CARD_HOVER = '#273449'
    PRIMARY = '#22C55E'
    SECONDARY = '#3B82F6'
    TEXT = '#FFFFFF'
    SUBTEXT = '#94A3B8'
    WARNING = '#F59E0B'
    BORDER = '#334155'
    SHADOW = 'rgba(0, 0, 0, 0.25)'

    FONT_FAMILY = 'Segoe UI'

    @staticmethod
    def base_font(size=10, weight=QFont.Normal):
        font = QFont(Theme.FONT_FAMILY, size)
        font.setWeight(weight)
        return font

    @staticmethod
    def stylesheet():
        return f'''
            QWidget {{
                background: {Theme.BG};
                color: {Theme.TEXT};
                font-family: {Theme.FONT_FAMILY};
            }}

            QMainWindow {{
                background: {Theme.BG};
            }}

            QLabel#TitleLabel {{
                font-size: 28px;
                font-weight: 700;
                color: {Theme.TEXT};
            }}

            QLabel#SubtitleLabel {{
                font-size: 13px;
                color: {Theme.SUBTEXT};
            }}

            QLabel#CardTitle {{
                font-size: 18px;
                font-weight: 700;
                color: {Theme.TEXT};
            }}

            QLabel#CardText {{
                font-size: 12px;
                color: {Theme.SUBTEXT};
            }}

            QPushButton {{
                border: none;
                border-radius: 14px;
                padding: 12px 16px;
                background: {Theme.CARD};
                color: {Theme.TEXT};
                font-size: 13px;
            }}

            QPushButton:hover {{
                background: {Theme.CARD_HOVER};
            }}

            QPushButton:pressed {{
                background: {Theme.SECONDARY};
            }}

            QFrame#Sidebar {{
                background: {Theme.SIDEBAR};
                border-right: 1px solid {Theme.BORDER};
            }}

            QFrame#Card {{
                background: {Theme.CARD};
                border: 1px solid {Theme.BORDER};
                border-radius: 20px;
            }}

            QScrollBar:vertical {{
                background: transparent;
                width: 10px;
                margin: 0px;
            }}

            QScrollBar::handle:vertical {{
                background: {Theme.BORDER};
                min-height: 30px;
                border-radius: 5px;
            }}

            QScrollBar::handle:vertical:hover {{
                background: {Theme.SECONDARY};
            }}
        '''