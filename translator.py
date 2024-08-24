# Імпортуємо необхідні класи з бібліотеки PyQt5 для створення графічного інтерфейсу
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow  # Імпортуємо клас, створений за допомогою Qt Designer
from googletrans import Translator  # Імпортуємо клас для перекладу тексту

# Створюємо клас Widget, який наслідує QMainWindow з PyQt5
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()  # Викликаємо конструктор батьківського класу
        self.ui = Ui_MainWindow()  # Ініціалізуємо інтерфейс користувача
        self.ui.setupUi(self)  # Налаштовуємо інтерфейс у головному вікні
        self.trans = Translator()  # Створюємо екземпляр перекладача з googletrans
        self.dictionary = {  # Словник для відповідності назв мов їх кодам
            "англійська": "en",
            "французька": "fr",
            "іспанська": "es"
        }
        
        # Додаємо назви мов до комбобоксу для вибору
        self.ui.comboBox.addItems(self.dictionary.keys())
        
        # Підключаємо кнопку до методу перекладу тексту
        self.ui.pushButton.clicked.connect(self.translate_text)
        
    # Метод для перекладу тексту
    def translate_text(self):
        text = self.ui.textEdit.toPlainText()  # Отримуємо текст з текстового поля для вводу
        t = self.ui.comboBox.currentText()  # Отримуємо вибрану мову з комбобоксу
        
        if text:  # Перевіряємо, чи введений текст не порожній
            # Виконуємо переклад тексту на обрану мову
            result = self.trans.translate(text, dest=self.dictionary[t])
            # Відображаємо перекладений текст у другому текстовому полі
            self.ui.textEdit_2.setPlainText(result.text)
        else:
            # Якщо текст не введено, можна додати повідомлення або іншу логіку
            self.ui.textEdit_2.setPlainText("Будь ласка, введіть текст для перекладу.")

# Створюємо додаток QApplication
app = QApplication([])

# Створюємо екземпляр головного вікна Widget
ex = Widget()

# Відображаємо головне вікно
ex.show()

# Запускаємо головний цикл обробки подій додатка
app.exec_()
