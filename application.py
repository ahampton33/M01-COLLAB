from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.testing import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))

    def __init__(self, id, name, author, publisher):
        self.id = id
        self.name = name
        self.author = author
        self.publisher = publisher

    def __repr__(self):
        return f'{self.name} - {self.author}'


@app.route('/')
def home():
    return 'hello world'


@app.route('/books')
def get_all_books():
    books = Book.query.all()
    result = []
    for book in books:
        book = {'id': book.id,
                'name': book.name,
                'author': book.author,
                'publisher': book.publisher
                }
        result.append(book)
    return {"books": result}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)

    result = {'id': book.id,
                'name': book.name,
                'author': book.author,
                'publisher': book.publisher
                }

    return {"books": result}