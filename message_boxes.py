import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        """Налаштування застосунку"""
        self.setWindowTitle("Message Boxes")
        self.setGeometry(100, 100, 340, 140)
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Налаштування основного вікна"""
        catalog_label = QLabel("Каталог авторов", self)
        catalog_label.move(100, 10)
        catalog_label.setFont(QFont("Arial", 20))
        catalog_label.adjustSize()

        search_label = QLabel("Пошук автора", self)
        search_label.move(20, 40) 

        self.author_edit = QLineEdit(self)
        self.author_edit.move(70, 70)
        self.author_edit.setPlaceholderText("Введіть автора")
        self.author_edit.resize(240, 24)

        search_button = QPushButton("Пошук", self)
        search_button.move(140, 100)
        search_button.clicked.connect(self.searchAuthor)

    def searchAuthor(self):
        """Обробка натискання кнопки пошуку"""
        file = "files/authors.txt"
        try:
            with open(file, "r", encoding="utf-8") as f:
                authors = [line.strip() for line in f.readlines()]
            author = self.author_edit.text()
            if author in authors:
                QMessageBox.information(self, "Результат", f"Автор {author} знайдено!", QMessageBox.StandardButton.Ok)
            else:
                answer = QMessageBox.question(self, "Результат пошуку", f"""<p>Автор {author} не знайдений у каталозі.</p>
                                    <p>Ви бажаете продовжити пошук?</p>""",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                    QMessageBox.StandardButton.No,
                )
                if answer == QMessageBox.StandardButton.No:
                    self.close()
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", f"Файл {file} не знайдено.", QMessageBox.StandardButton.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())