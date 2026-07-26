from PySide6.QtWidgets import QApplication, QLabel
import sys

app = QApplication(sys.argv)
label = QLabel('EcoLens AI\nStage 1 in progress...')
label.resize(500,200)
label.setWindowTitle('EcoLens AI')
label.show()
sys.exit(app.exec())