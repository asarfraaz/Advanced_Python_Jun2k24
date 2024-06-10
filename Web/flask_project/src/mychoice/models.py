from mychoice import db
print("model", db, id(db))

class Book(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    title   = db.Column(db.String(100), unique=True, nullable=False)
    author  = db.Column(db.String(30), unique=True, nullable=False)
    price   = db.Column(db.Integer, default=1)
    quant   = db.Column(db.Integer, default=100, nullable=True)

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.price})"

    def sell(self, n_items):
        self.quant -= n_items
