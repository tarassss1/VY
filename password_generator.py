# імпорт необхідних модулів
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from random import *

class Widget(QMainWindow):
    def   __init__(self):
        # Підключаємо функції з бібліотеки PyQt5
        super().__init__()
        # Підключаємо графічний інтерфейс
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Підключаємо функцію до кнопки
        self.ui.pushButton.clicked.connect(self.generator)

    # Функція генерації пароля
    def generator(self):
        password = ""  # Створюємо порожній рядок для збереження можливих символів

        # Якщо вибраний перший чекбокс, додаємо цифри до рядка password
        if self.ui.checkBox.isChecked():
            password += "0123456789"

        # Якщо вибраний другий чекбокс, додаємо малі літери до рядка password
        if self.ui.checkBox_2.isChecked():
            password += "qwertyuiopasdfghjklzxcvbnm"

        result = ""  # Створюємо порожній рядок для збереження згенерованого пароля

        # Якщо рядок password не порожній (тобто вибраний хоча б один чекбокс)
        if password:
            # Генеруємо пароль довжиною 8 символів
            for i in range(8):
                result += choice(password)  # Додаємо випадковий символ з рядка password до результату
            self.ui.label_2.setText(result)  # Виводимо згенерований пароль на екран (label_2)
        else:
            # Якщо жоден чекбокс не вибраний, виводимо повідомлення з попередженням
            self.ui.label_2.setText("Виберіть хоча б один checkbox")

# Створюємо додаток QApplication
app = QApplication([])

# Створюємо екземпляр нашого головного вікна Widget
ex = Widget()

# Відображаємо головне вікно
ex.show()

# Запускаємо головний цикл обробки подій програми
app.exec_()


