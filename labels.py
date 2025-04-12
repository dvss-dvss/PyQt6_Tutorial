from ast import expr
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        self.setWindowTitle("Пустое окно")
        self.setGeometry(100, 100, 800, 600)
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Створення QLabel з текстом та зображенням"""
        hello_label = QLabel("Привіт, PyQt!", self)
        hello_label.move(105, 15) # Встановлення позиції тексту
        image = "images/world.png" # Шлях до зображення
        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.setGeometry(50, 50, pixmap.width(), pixmap.height())
                # Встановлення позиції зображення
        except FileNotFoundError:
            print(f"Файл {image} не знайдено.")
            # Обробка помилки, якщо файл не знайдено

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())