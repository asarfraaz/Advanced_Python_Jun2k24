from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# For CSRF problem with WTF forms
# From : https://stackoverflow.com/a/53460575/4106458
# import os
# SECRET_KEY = os.urandom(32)

SECRET_KEY = 'pythonisfun'

app = Flask(__name__) # Helps flask to look for static files and templates
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"

db = SQLAlchemy(app)
print(db, id(db))

from mychoice import routes
