import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        """Налаштування застосунку"""
        self.setWindowTitle("Горизонтальне розташування")
        self.setMinimumWidth(600)
        self.setFixedHeight(60)
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Налаштування основного вікна"""
        name_label = QLabel("Нове ім'я користувача")
        name_edit = QLineEdit()
        name_edit.setClearButtonEnabled(True)
        name_edit.textEdited.connect(self.check_username)
        self.accept_botton = QPushButton("Пидтвердити")
        self.accept_botton.setEnabled(False)
        #self.accept_botton.clicked.connect(self.on_button_clicked)
        main_h_box = QHBoxLayout()
        main_h_box.addWidget(name_label)
        main_h_box.addWidget(name_edit)
        main_h_box.addWidget(self.accept_botton)
        self.setLayout(main_h_box)

    def check_username(self, text):
        """Перевірка введеного імені"""
        if text and all(char.isalpha() or char.isdigit() or char in text):
            self.accept_botton.setEnabled(True)
        else:
            self.accept_botton.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())