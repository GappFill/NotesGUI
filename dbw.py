import sqlite3

def create_table():
    db_user = sqlite3.connect("notes.db")
    cursor_user = db_user.cursor()
    cursor_user.execute("""CREATE TABLE IF NOT EXISTS notes(
	"id"	INTEGER,
	"title"	TEXT UNIQUE,
	"text"	TEXT UNIQUE,
	"date"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
)""")






def insert(title, text, date):
    try:  # Пробуем обновить данные
        with sqlite3.connect('notes.db') as db:
            cursor = db.cursor()
            cursor.execute(f"INSERT INTO notes VALUES(NULL,'{title}', '{text}', '{date}')")
        print("Notes was add")
    except:  # Если не обновились, создаем новую заметку
        with sqlite3.connect('notes.db') as db:
            cursor = db.cursor()
            cursor.execute(
                f"UPDATE notes SET title = '{title}', text = '{text}' WHERE title = '{title}' OR text = '{text}'")
            print("Notes was update")


def delet(title, text):
    try:  # Пробуем обновить данные
        with sqlite3.connect('notes.db') as db:
            cursor = db.cursor()
            cursor.execute(f"DELETE FROM notes WHERE title='{title}' AND text = '{text}'")
        print("Notes was add")
    except:
        print('note wa remove')


def get_note(title):  # Получаем заметку
    try:
        with sqlite3.connect('notes.db') as db:
            cursor = db.cursor()
            note = cursor.execute(f"SELECT * FROM notes WHERE TITLE = '{title}' ").fetchone()
            return note
    except:  # Если не обновились, создаем новую заметку
        print(0)


def get_titles():  # Получаем все данные для комбобокса
    try:
        with sqlite3.connect('notes.db') as db:
            cursor = db.cursor()
            titles = cursor.execute(f"SELECT title FROM notes").fetchall()
            return titles
    except:
        print(0)
