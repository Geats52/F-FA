'''
Задание №2
Создать базу данных для хранения информации о книгах в библиотеке.
База данных должна содержать две таблицы: "Книги" и "Авторы".
В таблице "Книги" должны быть следующие поля: id, название, год издания,
количество экземпляров и id автора.
В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
Необходимо создать связь между таблицами "Книги" и "Авторы".
Написать функцию-обработчик, которая будет выводить список всех книг с
указанием их авторов.

'''

from flask import Flask, render_template
from model_01 import db, Books, Authors

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase1.db'
db.init_app(app)

@app.route('/')
def index():
    return 'HI!'


@app.cli.command("init_db")
def init_db():
    db.create_all()


@app.cli.command("fill-db")
def fill_tables():
    for author in range(1, 7):
        new_author = Authors(name=f'Факультет {author}'),
        db.session.add(new_author)
    db.session.commit()

    for book in range(2013, 2023):
        for i in range(1, 7):
            new_book = book(title = f'Название книги: {book}', 
                            year_of_publication = f'Год публикации: {book}', 
                            number_of_copies = 4000 + book,
                            id_author = i)
            db.session.add(new_book)
    db.session.commit()

@app.route('/books/')
def write_books():
    books = Books.query.all()
    context = {'books': books}
    return render_template('books.html', **context)



if __name__ == '__main__':
    app.run(debug=True)
