import random, datetime
from peewee import *

sqlite_db = SqliteDatabase('book.db')

class Book(Model):
    title = CharField()
    pages = IntegerField()
    date_of_issue = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = sqlite_db

sqlite_db.connect()
sqlite_db.create_tables([Book], safe = True)

# sorting

# books = Book.select().order_by(Book.pages)
# books = Book.select().order_by(Book.pages.desc())

# for book in books:
#     print(str(book.pages) + " " + book.title)


# def get_rand():
#     return random.randint(1,100)

# data = [
#     {'title': 'Belajar Membaca Untuk Anak', 'pages': get_rand()},
#     {'title': 'Dongeng Sebelum Tidur', 'pages': get_rand()},
#     {'title': 'Masak Bareng Bunda', 'pages': get_rand()},
#     {'title': 'Ikan Hiu Makan Tomat', 'pages': get_rand()}
# ]

# Book.insert_many(data).execute()

# Update data

# book = Book.select().where(Book.title == 'Belajar Membaca Untuk Anak').get()
# book.title = 'Menari'
# book.pages = 999
# book.save()

# cara lain
# Book.update(title = 'Bekerja', pages = 354).where(Book.title == 'Anak Cantik').execute()

# cara menghapus data
# delete satu data delete_instance
# book = Book.get(Book.id == 2)
# book.delete_instance()

# delete beberapa data
# Book.delete().where(Book.pages > 100).execute()

# cara count
# print(Book.select().count())
# limit
# books = Book.select().limit(5)
# for book in books:
#     print(book.title)

# pagination
# books = Book.select().paginate(2, 10)
# for book in books:
#     print(str(book.id) + ' ' + book.title)


