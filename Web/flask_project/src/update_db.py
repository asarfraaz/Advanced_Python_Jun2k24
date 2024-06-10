from mychoice import db
from mychoice.models import Book

db.create_all() # To create db file is not present

bk1 = Book(title="Outlier", author="Malcolm Gladwell", price=123.5, quant=50)
bk2 = Book(title="Who moved my cheese", author="Dr. Johnson", price=45, quant=100)

db.session.add(bk1)
db.session.add(bk2)

db.session.commit()

for book in Book.query.all():
    print(book)
