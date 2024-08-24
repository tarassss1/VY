# підключення модулів з бібліотеки PyQt5
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl

# Оголошення класу Widget, який успадковується від QMainWindow
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        # підключення файлу з інтерфейсом
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)  
        self.player = QMediaPlayer()  # Створення плеєра для відтворення аудіо
        # Зв'язування кнопок з функціями
        self.ui.select_button.clicked.connect(self.select_music)
        self.ui.play_button.clicked.connect(self.play_music)
        self.ui.stop_button.clicked.connect(self.stop_music)

    def select_music(self):
        # Відкриває діалогове вікно для вибору аудіофайлу
        file, n = QFileDialog.getOpenFileName(self, "Select audio", "", 
                                              "Audio Files(*.mp3 *.wav)")
        if file:
            # Встановлює вибраний файл як джерело медіа для плеєра
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file)))
            self.player.setVolume(50)  # Встановлення гучності на 50%

    def play_music(self):
        # Відтворення або пауза аудіо в залежності від стану плеєра
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()  # Призупинити відтворення
        else:
            self.player.play()  # Розпочати відтворення

    def stop_music(self):
        # Зупинка відтворення аудіо
        self.player.stop()

# Основна частина програми
app = QApplication([])
ex = Widget()  # Створення екземпляра Widget
ex.show()  # Показати вікно
app.exec_()  # Запуск основного циклу програми
