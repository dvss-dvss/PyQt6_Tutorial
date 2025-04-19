import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QSpacerItem, QCheckBox, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        """Налаштування застосунку"""
        self.setWindowTitle("Vertical Box Layout")
        self.setMinimumSize(350, 200)
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Налаштування основного вікна"""
        first_label = QLabel("Python-бібліотеки")
        first_label.setFont(QFont("Arial", 18))
        first_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        header_label = QLabel("Яки бібліотеки ви знаєте? (будть ласка, оберіть усі які використовували)") 
        header_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        header_label.setWordWrap(True)

        libreries = (
            "PyQt6",
            "Tkinter",
            "Django",
            "Pygame",
        )
        libraries_group = QPushButton(self)
        libraries_group.setAutoExclusive(False)
        libraries_group.buttonClicked.connect(self.onLibrarySelected)
        
        self.confirm_button = QPushButton("Підтвердити")
        self.confirm_button.setEnabled(False)
        self.confirm_button.clicked.connect(self.close)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(first_label)
        main_v_box.addWidget(header_label)
        for library in libreries:
            checkbox = QCheckBox(library)
            libraries_group.addButton(checkbox)
            main_v_box.addWidget(checkbox)
        main_v_box.addWidget(self.confirm_button)
        self.setLayout(main_v_box)

    def onLibrarySelected(self, button):
        """Обробка натискання кнопки"""
        if button.isChecked():
            print(f"Вибрано: {button.text()}")
        else:
            print(f"Скасовано: {button.text()}")
            self.confirm_button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())