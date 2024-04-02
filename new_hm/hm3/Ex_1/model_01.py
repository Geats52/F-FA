from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    year_of_publication = db.Column(db.String(8), nullable=False)
    number_of_copies = db.Column(db.Integer, nullable=False)
    id_author = db.Column(db.String(20), db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return f'Название книги: {self.title}, Имя автора: {self.id_author}, Год издания: {self.number_of_copies}'

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    secondname = db.relationship('Books', backref=db.backref('author'), lazy=True)

    def __repr__(self):
        return f'Фамилия и Имя автора: {self.secondname} {self.firstname}'