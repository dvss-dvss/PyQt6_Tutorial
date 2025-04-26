from json import tool
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTextEdit, QFileDialog, QInputDialog, QFontDialog, QColorDialog

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor, QIcon, QAction, QTextCursor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        """Налаштування застосунку"""
        self.setWindowTitle("PyQt Notepad")
        self.setMinimumSize(400, 500)
        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()

    def setUpMainWindow(self):
        """Налаштування основного вікна"""
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

    def createActions(self):
        """Створення дій"""
        self.quit_action = QAction(QIcon("image/exit.png"), "&Вихід", self)
        self.quit_action.setShortcut("Ctrl+Q")
        self.quit_action.triggered.connect(self.close)

        self.new_action = QAction(QIcon("image/new.png"), "&Новий", self)
        self.new_action.setShortcut("Ctrl+N")
        self.new_action.triggered.connect(self.clearText)

        self.open_action = QAction(QIcon("image/open_file.png"), "&Відкрити", self)
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.triggered.connect(self.openFile)

        self.save_action = QAction(QIcon("image/save_file.png"), "&Зберегти", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.triggered.connect(self.saveToFile)

        self.undo_action = QAction(QIcon("image/undo.png"), "&Скасувати", self)
        self.undo_action.setShortcut("Ctrl+Z")
        self.undo_action.triggered.connect(self.text_edit.undo)

        self.redo_action = QAction(QIcon("image/redo.png"), "&Повторити", self)
        self.redo_action.setShortcut("Ctrl+Y")
        self.redo_action.triggered.connect(self.text_edit.redo)

        self.cut_action = QAction(QIcon("image/cut.png"), "&Вирізати", self)
        self.cut_action.setShortcut("Ctrl+X")
        self.cut_action.triggered.connect(self.text_edit.cut)

        self.copy_action = QAction(QIcon("image/copy.png"), "&Копіювати", self)
        self.copy_action.setShortcut("Ctrl+C")
        self.copy_action.triggered.connect(self.text_edit.copy)

        self.paste_action = QAction(QIcon("image/paste.png"), "&Вставити", self)
        self.paste_action.setShortcut("Ctrl+V")
        self.paste_action.triggered.connect(self.text_edit.paste)

        self.find_action = QAction(QIcon("image/find.png"), "&Знайти", self)
        self.find_action.setShortcut("Ctrl+F")
        self.find_action.triggered.connect(self.searchText)

        self.font_action = QAction(QIcon("image/font.png"), "&Шрифт", self)
        self.font_action.setShortcut("Ctrl+T")
        #self.font_action.triggered.connect(self.setFont)

        self.color_action = QAction(QIcon("image/color.png"), "&Колір", self)
        self.color_action.setShortcut("Ctrl+Shift+C")
        #self.color_action.triggered.connect(self.setColor)

        self.highlight_action = QAction(QIcon("image/highlight.png"), "&Виділити", self)
        self.highlight_action.setShortcut("Ctrl+H")
        #self.highlight_action.triggered.connect(self.highlightText)
         
        self.about_action = QAction("&Про програму")
        #self.about_action.triggered.connect(self.aboutDialog)   

    def createMenu(self):
        """Створення меню"""
        self.menuBar().setNativeMenuBar(False)
        
        file_menu = self.menuBar().addMenu("&Файл")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.quit_action)
        file_menu.addSeparator()
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_action)

        edit_menu = self.menuBar().addMenu("&Правка")
        edit_menu.addAction(self.undo_action)
        edit_menu.addAction(self.redo_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.cut_action)
        edit_menu.addAction(self.copy_action)
        edit_menu.addAction(self.paste_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.find_action)

        tool_menu = self.menuBar().addMenu("&Інструменти")
        tool_menu.addAction(self.font_action)
        tool_menu.addAction(self.color_action)
        tool_menu.addAction(self.highlight_action)

        help_menu = self.menuBar().addMenu("&Допомога")
        help_menu.addAction(self.about_action)

    def clearText(self):
        """Очистити текстове поле"""
        answer = QMessageBox.question(
            self,
            "Очистити текст",
            "Ви впевнені, що хочете очистити текст?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.text_edit.clear()
                            
    def saveToFile(self):
        """Зберегти текст у файл"""
        file_name, _ = QFileDialog.getSaveFileName(self, "Зберегти файл", "", "Text Files (*.txt);;HTML Files (*.html)")
        if file_name.endswith(".txt"):
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(self.text_edit.toPlainText())

        elif file_name.endswith(".html"):
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(self.text_edit.toHtml())

        else:
            QMessageBox.warning(
                self,
                "Помилка",
                "Невірний формат файлу! Виберіть .txt або .html",
                QMessageBox.StandardButton.Ok   
            )

    def openFile(self):
        """Відкрити файл"""
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Відкрити файл", "", "Text Files (*.txt);;HTML Files (*.html)"
            )
        if file_name:
            with open(file_name, "r", encoding="utf-8") as file:
                self.text_edit.setText(file.read())

    def searchText(self):
        """Пошук тексту"""
        search_text, ok = QInputDialog.getText(self, "Пошук", "Введіть текст для пошуку:")
        if ok and search_text:
            extra_selections = []
            self.text_edit.moveCursor(QTextCursor.MoveOperation.Start)
            color = QColor(Qt.GlobalColor.gray)
            while self.text_edit.find(search_text):
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(color)
                selection.cursor = self.text_edit.textCursor()
                extra_selections.append(selection)
            self.text_edit.setExtraSelections(extra_selections)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())