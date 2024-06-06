from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_view(): # https://127.0.0.1/
    return "<h1>My Choice Online Store</h1>"

if __name__ == "__main__":
    app.run()
