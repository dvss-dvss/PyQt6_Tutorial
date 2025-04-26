import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QLineEdit, QPushButton, QDateEdit, QComboBox, QFormLayout, QHBoxLayout

from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        """Налаштування застосунку"""
        self.setWindowTitle("Форма для заповнення")
        self.setMinimumSize(500, 300)
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Налаштування основного вікна"""
        header_label = QLabel("Форма для призначення зустрічі")
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header_label.setFont(QFont("Arial", 18))

        # Поля для вводу
        self.first_name_edit = QLineEdit()
        self.first_name_edit.setPlaceholderText("Ім'я")
        self.first_name_edit.textEdited.connect(self.clearText)
        self.last_name_edit = QLineEdit()
        self.last_name_edit.setPlaceholderText("Призвище")
        self.last_name_edit.textEdited.connect(self.clearText)

        name_h_box = QHBoxLayout()
        name_h_box.addWidget(self.first_name_edit)
        name_h_box.addWidget(self.last_name_edit)

        gender_combo = QComboBox()
        gender_combo.addItems(["Чоловік", "Жінка"])

        self.phone_edit = QLineEdit()
        self.phone_edit.setInputMask("+38 (099) 999-99-99")
        self.phone_edit.textEdited.connect(self.clearText)

        self.meeting_edit = QDateEdit()
        self.meeting_edit.setDate(QDate.currentDate())
        self.meeting_edit.setCalendarPopup(True)
        self.meeting_edit.setDisplayFormat("dd.MM.yyyy")
        self.meeting_edit.setMinimumDate(QDate.currentDate())

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
        main_form.addRow("Дата зустрічі", self.meeting_edit)
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
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())