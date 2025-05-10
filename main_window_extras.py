import sys

from PyQt6.QtWidgets import QApplication, QMainWindow,QDockWidget, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout, QSpacerItem, QSizePolicy, QTextEdit, QStatusBar, QToolBar, QCheckBox,QCheckBox, QRadioButton, QComboBox, QTabWidget, QGroupBox, QFormLayout, QGridLayout, QListWidget, QListWidgetItem, QTreeWidget
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        """Налаштування застосунку"""
        self.setWindowTitle("PyQt Main Window")
        self.setMinimumSize(500, 400)
        self.setUpMainWindow()
        self.createDockWidgets()
        self.createActions()
        self.createMenu()
        self.createToolBar()
        self.show()

    def setUpMainWindow(self):
        """Налаштування основного вікна"""
        self.text_edit = QTextEdit()
        self.text_edit.setAcceptRichText(True)
        self.setStatusBar(QStatusBar())
        self.setCentralWidget(self.text_edit)

    def createActions(self):
        """Створення дій"""
        self.quit_act = QAction(QIcon("images/exit.png") ,"&Вихід")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.setStatusTip("Вихід з програми")
        self.quit_act.triggered.connect(self.close)

        self.full_screen_act = QAction("&На весь екран", checkable=True)
        self.full_screen_act.setStatusTip("Перемкнути на весь екран")
        self.full_screen_act.triggered.connect(self.switchFullScreen)

    def createMenu(self):
        """Створення меню"""
        self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("&Файл")
        file_menu.addAction(self.quit_act)

        view_menu = self.menuBar().addMenu("&Вигляд")
        appearance_menu = view_menu.addMenu("&Зовнішній вигляд")
        appearance_menu.addAction(self.full_screen_act)

    def switchFullScreen(self, state):
        """Перемикання на повноекранний режим"""
        if state:
            self.showFullScreen()
        else:
            self.showNormal()
        
    def createToolBar(self):
        """Створення панелі інструментів"""
        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar.addAction(self.quit_act)

    def createDockWidgets(self):
        """Створення док-віджета"""
        dock_widget = QDockWidget("Фоматування")
        dock_widget.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)

        auto_bullet_cb = QCheckBox("Автоматичний неупрядкований список")
        auto_bullet_cb.toggled.connect(self.changeTextEditSettings)

        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(auto_bullet_cb)
        dock_v_box.addStretch(1)

        dock_container = QWidget()
        dock_container.setLayout(dock_v_box)

        dock_widget.setWidget(dock_container)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock_widget)


    def changeTextEditSettings(self, checked):
        """Зміна налаштувань QTextEdit"""
        if checked:
            self.text_edit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoBulletList)
        else:
            self.text_edit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoNone)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())