import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QListView
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QStringListModel
import sqlite3


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
            self.open_form()

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
            self.open_form()

    def button_centre(self):
        if self.ButtonCentre.text() == "Месяц":
            self.second_ans()
            self.time = "Месяц"
        else:
            self.third_ans()
            self.type = "Активный отдых"

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

    def open_form(self):
        self.window = QDialog()
        self.window.setFixedSize(500, 700)
        self.window.setFont(QFont("MS Shell Dlg 2", 18))
        self.window.setWindowIcon(QIcon('takeoff.ico'))
        self.window.setWindowTitle('Список вещей')
        con = sqlite3.connect("List.db")
        cur = con.cursor()
        if self.pol == "Мужской":
            pol = cur.execute("""SELECT Мужской FROM Pol""").fetchall()
        else:
            pol = cur.execute("""SELECT Женский FROM Pol""").fetchall()
        if self.time == "Неделя":
            time = cur.execute("""SELECT Неделя FROM Dlitelnost""").fetchall()
        elif self.time == "2 Недели":
            time = cur.execute("""SELECT двеНедели FROM Dlitelnost""").fetchall()
        else:
            time = cur.execute("""SELECT Месяц FROM Dlitelnost""").fetchall()
        if self.type == "Активный отдых":
            typ = cur.execute("""SELECT Активныйотдых FROM Type""").fetchall()
        elif self.type == "Отдых на пляжу":
            typ = cur.execute("""SELECT Отдыхнапляжу FROM Type""").fetchall()
        else:
            typ = cur.execute("""SELECT Командировка FROM Type""").fetchall()
        if self.place == "По стране":
            place = cur.execute("""SELECT Постране FROM Kuda""").fetchall()
        else:
            place = cur.execute("""SELECT Заграницу FROM Kuda""").fetchall()
        if self.temp == "Тепло":
            temp = cur.execute("""SELECT Тепло FROM Temper""").fetchall()
        else:
            temp = cur.execute("""SELECT Холодно FROM Temper""").fetchall()
        items = list(filter(lambda x: x, map(lambda x: x[0], pol + time + typ + place + temp)))
        self.lst = QListView(self.window)
        self.lst.resize(480, 650)
        self.lst.move(10, 10)
        self.model = QStringListModel(self.window)
        self.model.setStringList(items)
        self.lst.setModel(self.model)
        self.window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())