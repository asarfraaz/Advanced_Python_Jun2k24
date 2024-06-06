from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_view(): # https://127.0.0.1/
    return "<h1>My Choice Online Store</h1>"

@app.route("/about")
def about_view():
    return "<h1>About Us</h1>"

if __name__ == "__main__":
    app.run(debug=True)
