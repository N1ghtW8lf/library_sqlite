import sqlite3
import pandas as pd
conn = sqlite3.connect('library.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, description TEXT, genre TEXT)''')

print("Cписок команд:\n список\n поиск\n найти по жанру\n найти по автору\n инфо")
def add_book(title, author, description, genre):

    c.execute("INSERT INTO books (title, author, description, genre) VALUES (?, ?, ?, ?)", (title, author, description, genre))
    conn.commit()


def view_books():
    c.execute("SELECT title, author FROM books")
    print(pd.read_sql_query("SELECT * FROM books", conn))

def search_books():
    request = input('Запрос: ')
    search_query = f"SELECT * FROM books WHERE title LIKE ?"
    search_value = ('%' + request + '%',)
    c.execute(search_query, search_value)
    found_books = c.fetchall()
    for book in found_books:
        print(book[1]+" - "+book[2])
def search_by_genre(book_genre):
    search_query = f"SELECT * FROM books WHERE genre LIKE ?"
    search_value = ('%' + book_genre + '%',)
    c.execute(search_query, search_value)
    found_books = c.fetchall()
    for book in found_books:
        print(book[1]+" - "+book[2])
def search_by_author(auth):
    search_query = f"SELECT * FROM books WHERE author LIKE ?"
    search_value = ('%' + author + '%',)
    c.execute(search_query, search_value)
    found_books = c.fetchall()
    for book in found_books:
        print(book[1]+" - "+book[2])
def info(name):
    query = f"SELECT * FROM books WHERE title LIKE ?"
    value = ('%' + name + '%',)
    c.execute(query, value)
    foundbooks = c.fetchall()
    for book in foundbooks:
        print(f'{book[1]}\nАвтор: {book[2]}\nЖанр: {book[4]}\nОписание: {book[3]}')


def delete_book(title):
    c.execute("DELETE FROM books WHERE title=?", (title,))
    conn.commit()
#обработка фунций
message = input().lower()
if message == 'список':
    view_books()
elif message == 'добавить':
    title = input('Введите название: ')
    author = input('Введите автора: ')
    description = input('Описание: ')
    genre = input('Жанр: ')
    add_book(title, author, description, genre)
elif message == 'удалить':
    title = input('Введите название: ')
    delete_book(title)
elif message == 'поиск':
    search_books()
elif message == 'найти по жанру':
    request_genre = input('Жанр: ')
    search_by_genre(request_genre)
elif message == 'найти по автору':
    author = input('Введите автора:')
    search_by_author(author)
elif message == 'инфо':
    info_request = input('Название: ')
    info(info_request)
