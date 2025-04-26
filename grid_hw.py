import sys
import json

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QCheckBox,
    QTextEdit,
    QGridLayout,
)
from PyQt6.QtCore import Qt, QDate, QLocale
from PyQt6.QtGui import QFont


class MainWindow(QWidget):
    """Клас для головного вікна"""

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Налаштування застосунку"""
        self.setMinimumSize(500, 300)
        self.setWindowTitle("QGridLayout")
        self.setUpMainWindow()
        self.loadWidgetValuesFromFile()
        self.show()

    def setUpMainWindow(self):
        header_label = QLabel("Щоденник")
        header_label.setFont(QFont("Arial", 20))
        header_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        today_label = QLabel("Головне завдання дня")
        today_label.setFont(QFont("Arial", 14))
        self.today_tedit = QTextEdit()

        notes_label = QLabel("Нотатки")
        notes_label.setFont(QFont("Arial", 14))
        self.notes_tedit = QTextEdit()

        homework_label = QLabel("Домашнє Завдання")
        homework_label.setFont(QFont('Arial', 14))
        self.homework_tedit = QTextEdit()

        self.main_grid = QGridLayout()
        self.main_grid.addWidget(header_label, 0, 0)
        self.main_grid.addWidget(today_label, 1, 0)
        self.main_grid.addWidget(self.today_tedit, 2, 0, 3, 1)
        self.main_grid.addWidget(notes_label, 5, 0)
        self.main_grid.addWidget(self.notes_tedit, 6, 0, 3, 1)
        self.main_grid.addWidget(homework_label, 10, 0)
        self.main_grid.addWidget(self.homework_tedit, 12, 0, 3, 10)

        today = QLocale().toString(QDate.currentDate())
        date_label = QLabel(today)
        date_label.setFont(QFont("Arial", 18))
        date_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        todo_label = QLabel("Список завдань")
        today_label.setFont(QFont("Arial", 14))

        self.main_grid.addWidget(date_label, 0, 2)
        self.main_grid.addWidget(todo_label, 1, 1, 1, 2)

        for row in range(2, 9):
            item_cb = QCheckBox()
            item_edit = QLineEdit()
            self.main_grid.addWidget(item_cb, row, 1)
            self.main_grid.addWidget(item_edit, row, 2)

        self.setLayout(self.main_grid)

    def saveWidgetValues(self):
        details = {
            "focus": self.today_tedit.toPlainText(),
            "notes": self.notes_tedit.toPlainText(),
            "homework": self.homework_tedit.toPlainText()
        }
        remaining_todo = []

        for row in range(2, 9):
            item = self.main_grid.itemAtPosition(row, 1)
            widget = item.widget()
            if not widget.isChecked():
                item = self.main_grid.itemAtPosition(row, 2)
                widget = item.widget()
                text = widget.text()
                if text:
                    remaining_todo.append(text)
        details["todo"] = remaining_todo

        with open("files/details.txt", "w") as f:
            f.write(json.dumps(details))

    def closeEvent(self, event):
        self.saveWidgetValues()

    def loadWidgetValuesFromFile(self):
        try:
            with open("files/details.txt") as f:
                details = json.load(f)
                self.today_tedit.setText(details["focus"])
                self.notes_tedit.setText(details["notes"])
                self.homework_tedit.setText(details["homework"])

                for row in range(len(details["todo"])):
                    item = self.main_grid.itemAtPosition(row + 2, 2)
                    widget = item.widget()
                    widget.setText(details["todo"][row])
        except FileNotFoundError:
            f = open("files/details.txt", "w")


# Запуск програми
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())