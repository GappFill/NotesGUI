from notes import Ui_Form
from PyQt5 import QtWidgets
import datetime
from message import *
from dbw import *

import sys


def get_time():
    now = datetime.datetime.now()
    now_date = now.strftime("%d-%m-%Y %H:%M")
    return now_date

def fill_combobox():  # Заполняем комбобокс значениями
    ui.comboBox.clear()
    ui.comboBox.addItem('Тестовая заметка')
    for i in get_titles():  # Добовляем все заметки в коибобокс
        ui.comboBox.addItem(i[0])
    ui.comboBox.addItem('Создать заметку')


def testNotes():
    ui.lineEdit.setText('Это тестовая заметка')
    ui.textEdit.setText('Это самая первая заметка, которая была создана автоматически!'
                        'Да, Скайнет уже здесь :)')

def add_notes():  # Добовляем новую заметку
    insert(ui.lineEdit.text(), ui.textEdit.toPlainText(), get_time())
    fill_combobox()


def delete():  # Удаляем заметку
    value = Warning()
    if value == True:
        delet(ui.lineEdit.text(), ui.textEdit.toPlainText())
        ui.lineEdit.setText('')
        ui.textEdit.setText('')
        fill_combobox()

def onActivated():  # Получаем значение из комбобокса которое потом, надо передать в базу данных
    data = ui.comboBox.currentText()
    if data == 'Создать заметку':
        ui.lineEdit.setText('')
        ui.textEdit.setText('')

    elif data == 'Тестовая заметка':
        testNotes()
    else:
        # Сюда выводим текст, который должны получить из функции
        note = get_note(data)
        ui.lineEdit.setText(note[1])
        ui.textEdit.setText(note[2])
        ui.label_2.setText(note[3])





app = QtWidgets.QApplication(sys.argv)  # Инициализируем окно
Form = QtWidgets.QWidget()  # Создаем окно
ui = Ui_Form()  # Создаем интерфейс
ui.setupUi(Form)  # Добовляем интерфейс к нашему окну
Form.show()  # Показываем окно
create_table()
fill_combobox()



# Функционал
ui.pushButton_2.clicked.connect(delete)
ui.pushButton.clicked.connect(add_notes)
ui.comboBox.activated[str].connect(onActivated)  # Подключаемся к комбобоксу






sys.exit(app.exec_())  # Обрабатываем события

