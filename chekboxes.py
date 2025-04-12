import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        """Налаштування застосунку"""
        self.setWindowTitle("Chekboxes")
        self.setGeometry(200, 100, 250, 150)
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Налаштування основного вікна"""
        header_label = QLabel("Какие Python библиотеки вы знаете?", self)
        header_label.setWordWrap(True)
        header_label.adjustSize()
        header_label.move(20, 20)

        pygame_cb = QCheckBox("Pygame", self)
        pygame_cb.move(40, 60)
        pygame_cb.toggled.connect(self.printSelected)

        pyqt_cb = QCheckBox("PyQt6", self)
        pyqt_cb.move(40, 80)
        pyqt_cb.toggled.connect(self.printSelected)

        django_cb = QCheckBox("Django", self)
        django_cb.move(40, 100)
        django_cb.toggled.connect(self.printSelected)

    def printSelected(self):
        """Виведення вибраних бібліотек у консоль"""
        sender = self.sender()
        if sender.isChecked():
            print(f"{sender.text()} вибрано")
        else:
            print(f"{sender.text()} знято з вибору")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())