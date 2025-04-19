import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
    QLabel,
    QPushButton,
    QLineEdit,
    QMessageBox,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap


class NewUserDialog(QDialog):
    """Клас для реєстрації"""

    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initializeUI()

    def initializeUI(self):
        """Налаштування застосунку"""
        self.setFixedSize(360, 320)
        self.setWindowTitle("Sign Up")
        self.setUpWindow()

    def setUpWindow(self):
        login_label = QLabel("Створити новий акаунт", self)
        login_label.setFont(QFont("Arial", 20))
        login_label.move(50, 20)

        user_image = "images/new_user_icon.png"

        try:
            with open(user_image):
                user_label = QLabel(self)
                pixmap = QPixmap(user_image)
                user_label.setPixmap(pixmap)
                user_label.move(150, 60)
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")

        name_label = QLabel("Логін:", self)
        name_label.move(20, 144)

        self.name_edit = QLineEdit(self)
        self.name_edit.resize(250, 24)
        self.name_edit.move(90, 140)

        full_label = QLabel("Повне ім'я:", self)
        full_label.move(20, 174)

        self.full_edit = QLineEdit(self)
        self.full_edit.resize(250, 24)
        self.full_edit.move(90, 170)

        new_passwd_label = QLabel("Пароль:", self)
        new_passwd_label.move(20, 204)

        self.new_passwd_edit = QLineEdit(self)
        self.new_passwd_edit.resize(250, 24)
        self.new_passwd_edit.move(90, 200)
        self.new_passwd_edit.setEchoMode(QLineEdit.EchoMode.Password)

        confirm_label = QLabel("Пароль (2):", self)
        confirm_label.move(20, 234)

        self.confirm_edit = QLineEdit(self)
        self.confirm_edit.resize(250, 24)
        self.confirm_edit.move(90, 230)
        self.confirm_edit.setEchoMode(QLineEdit.EchoMode.Password)

        sign_up_button = QPushButton("Реєстрація", self)
        sign_up_button.resize(320, 32)
        sign_up_button.move(20, 270)
        sign_up_button.clicked.connect(self.confirmSignUp)

    def confirmSignUp(self):
        name_text = self.name_edit.text()
        pswd_text = self.new_passwd_edit.text()
        confirm_text = self.confirm_edit.text()

        if name_text == "" or pswd_text == "":
            QMessageBox.warning(
                self,
                "Помилка",
                "Будь ласка, введіть ім'я користувача та пароль",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close,
            )
        elif pswd_text != confirm_text:
            QMessageBox.warning(
                self,
                "Помилка",
                "Введені паролі не співпадають",
                QMessageBox.StandardButton.Close,
                QMessageBox.StandardButton.Close,
            )
        else:
            with open("files/users.txt", "a", encoding="UTF8") as f:
                f.write("\n" + name_text + " " + pswd_text)
            self.close()