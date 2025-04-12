import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        """Налаштування застосунку"""
        self.setWindowTitle("QPushButton")
        self.setGeometry(200, 100, 250, 150)
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Налаштування основного вікна"""
        self.times_pressed = 0
        self.name_label = QLabel("Не нажимайте на меня", self)
        self.name_label.adjustSize()
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.move(60, 30)
        self.button = QPushButton("Нажми на меня", self)
        self.button.move(80, 70)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        """Обробка натискання кнопки"""
        self.times_pressed += 1
        if self.times_pressed == 1:
            self.name_label.setText("Вы нажали на кнопку")
            self.name_label.adjustSize()
        elif self.times_pressed == 2:
            self.name_label.setText("Вы нажали на кнопку еще раз")
            self.name_label.adjustSize()
        elif self.times_pressed == 3:
            self.name_label.setText("Вы нажали на кнопку много раз")
            self.name_label.adjustSize()
        else:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())