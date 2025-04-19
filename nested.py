import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QComboBox,
    QSpinBox,
    QHBoxLayout,
    QVBoxLayout,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class MainWindow(QWidget):
    """Клас для головного вікна"""

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Налаштування застосунку"""
        self.setMaximumSize(460, 160)
        self.setWindowTitle("Nested Layout")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        info_label = QLabel("Оберіть дві страви для обіду та їх вартість")
        info_label.setFont(QFont("Arial", 16))
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        food_list = ["Котлета по-київські", "Салат Цезарь", "Чізкейк", "Борщ", "Шашлик"]

        food_combo1 = QComboBox()
        food_combo1.addItems(food_list)
        food_combo2 = QComboBox()
        food_combo2.addItems(food_list)

        self.price_sb1 = QSpinBox()
        self.price_sb1.setRange(0, 100)
        self.price_sb1.setSuffix("₴")
        self.price_sb1.valueChanged.connect(self.calculateTotal)

        self.price_sb2 = QSpinBox()
        self.price_sb2.setRange(0, 100)
        self.price_sb2.setSuffix("₴")
        self.price_sb2.valueChanged.connect(self.calculateTotal)

        item1_h_box = QHBoxLayout()
        item1_h_box.addWidget(food_combo1)
        item1_h_box.addWidget(self.price_sb1)

        item2_h_box = QHBoxLayout()
        item2_h_box.addWidget(food_combo2)
        item2_h_box.addWidget(self.price_sb2)

        self.totals_label = QLabel("Разом:")
        self.totals_label.setFont(QFont("Arial", 16))
        self.totals_label.setAlignment(Qt.AlignmentFlag.AlignRight)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(info_label)
        main_v_box.addLayout(item1_h_box)
        main_v_box.addLayout(item2_h_box)
        main_v_box.addWidget(self.totals_label)

        self.setLayout(main_v_box)

    def calculateTotal(self, value):
        total = self.price_sb1.value() + self.price_sb2.value()
        self.totals_label.setText(f"Разом: {total} ₴")


# Запуск програми
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())