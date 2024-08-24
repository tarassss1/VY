from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtCore import Qt
import json

# Оголошення класу Widget, який успадковується від QMainWindow
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Ініціалізація UI
        self.ui.setupUi(self)  # Налаштування UI
        self.notes = {}  # Ініціалізація словника для нотаток
        self.load_data()  # Завантаження даних з файлу
        # Зв'язування кнопок з методами
        self.ui.pushButton.clicked.connect(self.save_note)
        self.ui.pushButton_2.clicked.connect(self.delete_note)
        self.ui.calendarWidget.clicked.connect(self.show_note)
        
    def save_note(self):
        # Збереження нотатки за вибраною датою
        date = self.ui.calendarWidget.selectedDate() # зберігаємо вибрану дату у змінну date
        text = self.ui.textEdit.toPlainText()  # зберігаємо нотатку у змінну text
        self.notes[date.toString(Qt.ISODate)] = text # додаємо замітку до словника
        self.save_data()  # Оновлення файлу з даними

    def show_note(self):
        # Відображення нотатки для вибраної дати
        date = self.ui.calendarWidget.selectedDate() # зберігаємо вибрану дату у змінну date
        note = self.notes.get(date.toString(Qt.ISODate)) # зберігаємо нотатку у змінну note
        self.ui.textEdit.setPlainText(note)

    def save_data(self):
        # Збереження нотаток у файл JSON
        with open("notes.json", "w") as file:
            json.dump(self.notes, file)
    
    def load_data(self):
        # Завантаження нотаток з файлу JSON
        try:
            with open("notes.json", "r") as file:
                self.notes = json.load(file)
        except:
            self.notes = {}  # Якщо файл не існує або не може бути прочитаний

    def delete_note(self):
        # Видалення нотатки для вибраної дати
        date = self.ui.calendarWidget.selectedDate() # зберігаємо вибрану дату у змінну date
        del self.notes[date.toString(Qt.ISODate)] # видаляємо замітку до словника
        self.ui.textEdit.clear()  # Очищення текстового поля
        self.save_data()  # Оновлення файлу з даними

# Основна частина програми
app = QApplication([])
ex = Widget()  # Створення екземпляра Widget
ex.show()  # Показати вікно
app.exec_()  # Запуск основного циклу програми
