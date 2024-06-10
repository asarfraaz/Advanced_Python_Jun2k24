from flask import render_template, url_for, request, flash, redirect
from mychoice import app, db
from mychoice.models import Book
from mychoice.forms import BuyForm

@app.route("/") # Routes URL to this function/view
@app.route("/home") # Routes URL to this function/view
def home_view():
    # return "Hello World" # Info to be displayed on the webpage
    # return "<h1>Hello World</h1>" # Info to be displayed on the webpage
    # return "<h1>My Choice Online Store</h1>" # Info to be displayed on the webpage
    return render_template('home.html')

@app.route("/about") # Routes URL to this function/view
def about_view():
    return "<h1>About Page</h1>" # Info to be displayed on the webpage

@app.route("/books")
def show_all_books_view():
    allbooks = Book.query.all()
    return render_template('all_books.html', books=allbooks)

@app.route("/books/<int:book_id>")
def show_book_view(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book.html', title=book.title, book=book)

@app.route("/books/<int:book_id>/buy", methods=['GET', 'POST'])
def buy_book_view(book_id):
    book = Book.query.get_or_404(book_id)
    form = BuyForm()
    #val_ans = form.validate_on_submit()
    #print("Validation", val_ans)
    if form.validate_on_submit():
        book.sell(form.quant.data)
        db.session.commit()
        #flash('Thank you for your purchase')
        return redirect(url_for('show_book_view', book_id=book.id))
    #else:
        #flash('Failed Validation')
    return render_template('buy_book.html', title=book.title, book=book, form=form)

