# підключення модулів з бібліотеки PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QHBoxLayout, QMessageBox

app = QApplication([]) # "додаток", який запускає програму
window = QWidget() # головне вікно

# створення віджетів
line = QLineEdit()
button_add = QPushButton("добавити завдання")
list1 = QListWidget()
button_done = QPushButton("виконано")
button_open = QPushButton("відкрити")

# прикріплення на леяути
vertical = QVBoxLayout()
horisont = QHBoxLayout()

horisont.addWidget(button_done)
horisont.addWidget(button_open)

vertical.addWidget(line)
vertical.addWidget(button_add)
vertical.addWidget(list1)
vertical.addLayout(horisont)

window.setLayout(vertical)


window_second = QWidget()
list2 = QListWidget()
button_return = QPushButton("повернутися")
vertical2 = QVBoxLayout()
vertical2.addWidget(list2)
vertical2.addWidget(button_return)
window_second.setLayout(vertical2)
window_second.hide()


def open():
    window.hide()
    window_second.show()


# QMessageBox
def add():
    text = line.text() # витягуємо текст з поля для введення
    if text: # перевярємо чи змінна містить якесь значення
        list1.addItem(text) # добавляємо до списку новий елемент
        line.clear() # "очищуємо" віджет
    else: # спрацює коли нічого не напишемо
                          # вікно     назва     текст який виведеться
        QMessageBox.warning(window, "Помилка","Будь ласка, введіть щось") 


# щоб програма добавляла елементи в інший список
# щоб вона зберігала елементи в тектовий файл
def delete():
    selected = list1.selectedItems() # записуємо "обрані" елементи
    if selected: # якщо обрано хоча б один елемент
        with open("test.txt", "a") as file:
            for item in selected: # робимо перебір всіх обраних елементів
                t = list1.takeItem(list1.row(item)).text()
                list2.addItem(t)
                file.write(t + "\n")

def load():
    with open("test.txt", "r") as file:
        for f in file:
            list2.addItem(f.strip()) # strip = видаляє пробіли на початку та кінці

load()


button_done.clicked.connect(delete)
button_add.clicked.connect(add)

window.show() # показує вікно
app.exec_() # запускає "додаток" у виконання


#TODO: зберігання невиконаних завдання у файл
#TODO: повернути завдання з виконаних у невиконані
