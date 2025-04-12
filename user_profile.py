from math import pi
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QFont, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        """Налаштування застосунку"""
        self.setWindowTitle("Профіль користувача")
        self.setGeometry(100, 100, 260, 400)
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        """Створення міток для зображень"""
        image = ["images/skyblue.png", "images/profile_image.png"]
        for image in image:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    label.setGeometry(0, 0 , pixmap.width(), pixmap.height())
                    if image == "images/profile_image.png":
                        label.move(80, 20)
            except FileNotFoundError:
                print(f"Файл {image} не знайдено.")


    def setUpMainWindow(self):
        """Налаштування основного вікна"""
        self.createImageLabels()
        user_label = QLabel("Давид", self)
        user_label.setFont(QFont("Arial", 20))
        user_label.adjustSize()
        user_label.move(55, 140)

        bio_label = QLabel("Биография", self)
        bio_label.setFont(QFont("Arial", 17))
        bio_label.adjustSize()
        bio_label.move(15, 170)

        about_label = QLabel("Привет, я Давид, и я люблю программировать на Python.", self)
        about_label.setWordWrap(True)
        about_label.adjustSize()
        about_label.move(15, 195)

        skills_label = QLabel("Технологии", self)
        skills_label.setFont(QFont("Arial", 17))
        skills_label.adjustSize()
        skills_label.move(15, 240)

        languages_label = QLabel("Python | Pygame | PyQt6 | Django", self)
        languages_label.adjustSize()
        languages_label.move(15, 265)

        expirience_label = QLabel("Опыт", self)
        expirience_label.setFont(QFont("Arial", 17))
        expirience_label.adjustSize()
        expirience_label.move(15, 290)

        developer_label = QLabel("Python-разработчик", self)
        developer_label.adjustSize()
        developer_label.move(15, 320)

        dev_dates_label = QLabel("2023 - сейчас", self)
        #dev_dates_label.setFont(QFont("Arial", 10))
        dev_dates_label.adjustSize()
        dev_dates_label.move(15, 340)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())