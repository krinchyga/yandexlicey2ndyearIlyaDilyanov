import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        uic.loadUi('form.ui', self)  # Загружаем дизайн
        QMainWindow.setFixedSize(self, 900, 700)
        self.ButtonStart.clicked.connect(self.start_program)
        self.ButtonLeft.clicked.connect(self.button_left)
        self.ButtonRight.clicked.connect(self.button_right)
        self.ButtonCentre.clicked.connect(self.button_centre)
        self.BackGround.setStyleSheet("border-image: url('BackGround.jpg') 0 0 0 0;")
        self.setWindowIcon(QIcon('takeoff.ico'))
        self.hide_all()
        self.labels = open('Labels.txt', 'r', encoding='utf8').readlines()
        self.iLabel = -1

    def hide_all(self):
        self.ButtonRight.hide()
        self.ButtonLeft.hide()
        self.ButtonCentre.hide()
        self.label.hide()

    def start_program(self):
        self.next_label()
        self.ButtonStart.hide()
        self.ButtonRight.setText('Мужской')
        self.ButtonRight.show()
        self.ButtonLeft.setText('Женский')
        self.ButtonLeft.show()
        self.label.show()

    def next_label(self):
        self.iLabel += 1
        self.label.setText(self.labels[self.iLabel])

    def button_left(self):
        if self.ButtonLeft.text() == "Женский":
            self.first_ans()
            self.pol = "Женский"
        elif self.ButtonLeft.text() == "Неделя":
            self.second_ans()
            self.time = "Неделя"
        elif self.ButtonLeft.text() == "Отдых на пляжу":
            self.third_ans()
            self.type = "Отдых на пляжу"
        elif self.ButtonLeft.text() == "По стране":
            self.fourth_ans()
            self.place = "По стране"
        else:
            self.temp = "Тепло"

    def button_right(self):
        if self.ButtonRight.text() == "Мужской":
            self.first_ans()
            self.pol = "Мужской"
        elif self.ButtonRight.text() == "2 Недели":
            self.second_ans()
            self.time = "2 Недели"
        elif self.ButtonRight.text() == "Командировка":
            self.third_ans()
            self.type = "Командировка"
        elif self.ButtonRight.text() == "За границу":
            self.fourth_ans()
            self.place = "За границу"
        else:
            self.temp = "Холодно"

    def button_centre(self):
        if self.ButtonCentre.text() == "Месяц":
            self.second_ans()
            self.pol = "Месяц"
        else:
            self.third_ans()
            self.time = "Активный отдых"

    def first_ans(self):
        self.next_label()
        self.ButtonLeft.setText('Неделя')
        self.ButtonRight.setText('2 Недели')
        self.ButtonCentre.setText('Месяц')
        self.ButtonCentre.show()

    def second_ans(self):
        self.next_label()
        self.ButtonLeft.setText('Отдых на пляжу')
        self.ButtonRight.setText('Командировка')
        self.ButtonCentre.setText('Активный отдых')

    def third_ans(self):
        self.next_label()
        self.ButtonLeft.setText('По стране')
        self.ButtonRight.setText('За границу')
        self.ButtonCentre.hide()

    def fourth_ans(self):
        self.next_label()
        self.ButtonLeft.setText('Тепло')
        self.ButtonRight.setText('Холодно')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
