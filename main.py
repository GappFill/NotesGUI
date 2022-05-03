
import sys
forTest = []

# Обрабатывает поступившую информацию
def controller(user_input):
    if user_input == '1':
        showAllNotes()
    elif user_input == '2':
        createNewNotes()


def editNotes():
    number = input('Введите номер/название заметки: ')
    print()


def createNewNotes():
    print('Содание новой заметки')
    title = input('Название заметки: ')
    text = input('Текст заметки: ')
    forTest.append(title)
    forTest.append(text)


def showAllNotes():
    print('Все ваши заметки:')
    for i in forTest:
        print(i)


def menu():
    print("""----Меню----
Вывести все земетки   - 1
Создать новую заметку - 2
Редактировать заметку - 3
Поиск заметок         - 4
Показать меню еще раз - 3
    """)


def main():
    menu()
    while True:
        user_input = input('>>>')
        controller(user_input)


sys.stdout.write('строка')



