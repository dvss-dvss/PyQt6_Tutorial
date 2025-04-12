import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        """Налаштування застосунку"""
        self.setWindowTitle("Line Edits")
        self.setMaximumSize(310, 310)
        self.setUpMainWindow()
        self.setGeometry(100, 100, 310, 310)
        self.show()

    def setUpMainWindow(self):
        """Налаштування основного вікна"""
        QLabel("Enter your name:", self).move(70, 10)

        name_label = QLabel("Name:", self)
        name_label.adjustSize()
        name_label.move(20, 50)

        self.name_edit = QLineEdit(self)
        self.name_edit.resize(210, 20)
        self.name_edit.move(70, 50)

        clear_button = QPushButton("Clear", self)
        clear_button.move(100, 90)
        clear_button.clicked.connect(self.clearText)

        accept_button = QPushButton("OK", self)
        accept_button.move(210, 90)
        accept_button.clicked.connect(self.acceptText)

    def clearText(self):
        """Очистка текстового поля"""
        self.name_edit.clear()

    def acceptText(self):
        """Обробка натискання кнопки OK"""
        name = self.name_edit.text()
        if name:
            self.name_edit.setText(f"Hello, {name}!")
            self.name_edit.setReadOnly(True)
        else:
            self.name_edit.setText("Please enter your name.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())