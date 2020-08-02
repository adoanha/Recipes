from flask import Flask, render_template, url_for

app = Flask(__name__)
@app.route('/home/')
@app.route('/home/<name>')
@app.route('/')


def home(name=None):
    return render_template("home.html", name=name)

with app.test_request_context():
    print(url_for("static", filename="style.css"))