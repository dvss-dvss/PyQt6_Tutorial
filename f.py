import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QDateEdit,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QFormLayout,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont


class MainWindow(QWidget):
    """Клас для головного вікна"""

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Налаштування застосунку"""
        self.setMinimumSize(500, 400)
        self.setWindowTitle("QFormLayout")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Створення та розташування віджетів у головному вікні"""
        header_label = QLabel("Форма для призначення зустрічі")
        header_label.setFont(QFont("Arial", 18))
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.first_name_edit = QLineEdit()
        self.first_name_edit.setPlaceholderText("Ім'я")
        self.first_name_edit.textEdited.connect(self.clearText)
        self.last_name_edit = QLineEdit()
        self.last_name_edit.setPlaceholderText("Прізвище")
        self.last_name_edit.textEdited.connect(self.clearText)

        name_h_box = QHBoxLayout()
        name_h_box.addWidget(self.first_name_edit)
        name_h_box.addWidget(self.last_name_edit)

        gender_combo = QComboBox()
        gender_combo.addItems(["Чоловіча", "Жіноча"])

        self.phone_edit = QLineEdit()
        self.phone_edit.setInputMask("(999) 999-99-99;_")
        self.phone_edit.textEdited.connect(self.clearText)

        self.meeting_date_edit = QDateEdit()
        self.meeting_date_edit.setDisplayFormat("dd.MM.yyyy")
        self.meeting_date_edit.setMinimumDate(QDate.currentDate())
        self.meeting_date_edit.setCalendarPopup(True)
        self.meeting_date_edit.setDate(QDate.currentDate())

        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("username@domain.com")
        self.email_edit.textEdited.connect(self.clearText)

        extra_info_edit = QTextEdit()
        self.feedback_label = QLabel()
        submit_button = QPushButton("Надіслати")
        submit_button.setMaximumWidth(140)
        submit_button.clicked.connect(self.checkFormInformation)

        submit_h_box = QHBoxLayout()
        submit_h_box.addWidget(self.feedback_label)
        submit_h_box.addWidget(submit_button)

        main_form = QFormLayout()
        main_form.setFieldGrowthPolicy(
            main_form.FieldGrowthPolicy.AllNonFixedFieldsGrow
        )
        main_form.setFormAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop
        )
        main_form.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)

        main_form.addRow(header_label)
        main_form.addRow("Ім'я", name_h_box)
        main_form.addRow("Стать", gender_combo)
        main_form.addRow("Дата зустрічі", self.meeting_date_edit)
        main_form.addRow("Телефон", self.phone_edit)
        main_form.addRow("Email", self.email_edit)
        main_form.addRow(QLabel("Коментар"))
        main_form.addRow(extra_info_edit)
        main_form.addRow(submit_h_box)

        self.setLayout(main_form)

    def clearText(self, text):
        """Видалення тексту зворотного зв'язку"""
        self.feedback_label.clear()

    def checkFormInformation(self):
        if self.first_name_edit.text() == "" or self.last_name_edit.text() == "":
            self.feedback_label.setText("[INFO] Прощено імена")
        elif not self.phone_edit.hasAcceptableInput():
            self.feedback_label.setText("[INFO] Неправильно введено номер телефону")
        elif "@" not in self.email_edit.text():
            self.feedback_label.setText("[INFO] Email введено неправильно")


# Запуск програми
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())