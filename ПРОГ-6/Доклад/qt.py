import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Window')
        self.setGeometry(100, 100, 300, 200)

        button = QPushButton('Нажми на меня!', self)
        button.move(100, 100)
        button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print('Кнопка нажата')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())