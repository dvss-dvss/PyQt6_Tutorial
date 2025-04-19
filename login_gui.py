import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QCheckBox,
    QMessageBox,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap

from registration import NewUserDialog


class LoginWindow(QWidget):
    """Клас для головного вікна"""

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Налаштування застосунку"""
        self.setFixedSize(300, 220)
        self.setWindowTitle("Login")
        self.setUpWindow()
        self.show()

    def setUpWindow(self):
        self.login_is_successful = False

        login_label = QLabel("Login", self)
        login_label.setFont(QFont("Arial", 20))
        login_label.move(120, 10)

        username_label = QLabel("Ім'я користувача:", self)
        username_label.move(20, 54)

        self.username_edit = QLineEdit(self)
        self.username_edit.resize(160, 24)
        self.username_edit.move(120, 50)

        password_label = QLabel("Пароль:", self)
        password_label.move(20, 86)

        self.password_edit = QLineEdit(self)
        self.password_edit.resize(160, 24)
        self.password_edit.move(120, 82)
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

        self.show_password_cb = QCheckBox("Показати пароль", self)
        self.show_password_cb.move(90, 110)
        self.show_password_cb.toggled.connect(self.displayPasswordIfChecked)

        login_button = QPushButton("Login", self)
        login_button.resize(260, 34)
        login_button.move(20, 140)
        login_button.clicked.connect(self.clickLoginButton)

        not_account_label = QLabel("Немає аккаунту?", self)
        not_account_label.move(20, 186)

        sign_up_button = QPushButton("Зареєструватися", self)
        sign_up_button.move(120, 180)
        sign_up_button.clicked.connect(self.createNewUser)

    def clickLoginButton(self):
        users = {}
        file = "files/users.txt"

        try:
            with open(file, encoding="UTF8") as f:
                for line in f:
                    user_info = line.split()
                    username_info = user_info[0]
                    password_info = user_info[1].strip("\n")
                    users[username_info] = password_info

            username = self.username_edit.text()
            password = self.password_edit.text()
            if (username, password) in users.items():
                QMessageBox.information(
                    self,
                    "Login Successful!",
                    "Login Successful!",
                    QMessageBox.StandardButton.Ok,
                    QMessageBox.StandardButton.Ok,
                )
                self.login_is_successful = True
                self.close()
                self.openMainWindow()
            else:
                QMessageBox.warning(
                    self,
                    "Повідомлення про помилку",
                    "Ім'я користувача та пароль помилкові",
                    QMessageBox.StandardButton.Close,
                    QMessageBox.StandardButton.Close,
                )
        except FileNotFoundError as error:
            QMessageBox.warning(
                self,
                "Повідомлення про помилку",
                f"Файл не знайдено.\nError: {error}",
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok,
            )
            f = open(file, "w", encoding="UTF8")

    def closeEvent(self, event):
        if self.login_is_successful:
            event.accept()
        else:
            answer = QMessageBox.question(
                self,
                "Закрити застосунок",
                "Ви впевнені, що хочете закрити програму?",
                QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.Yes,
            )
            if answer == QMessageBox.StandardButton.Yes:
                event.accept()
            else:
                event.ignore()

    def createNewUser(self):
        self.new_user_window = NewUserDialog()
        self.new_user_window.show()

    def displayPasswordIfChecked(self, checked):
        if checked:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def openMainWindow(self):
        self.main_window = MainWindow()
        self.main_window.show()


class MainWindow(QWidget):
    """Клас для головного вікна"""

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Налаштування застосунку"""
        self.setMinimumSize(500, 500)
        self.setWindowTitle("Головне вікно")
        self.setUpMainWindow()

    def setUpMainWindow(self):
        image = "images/python_whale.jpg"

        try:
            with open(image):
                main_label = QLabel(self)
                pixmap = QPixmap(image)
                main_label.setPixmap(pixmap)
                main_label.move(0, 0)
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")


# Запуск програми
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())