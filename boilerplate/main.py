"""hello world for flask"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

app = Flask(__name__, static_url_path='')
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def hello():
    """ function for route / """
    return render_template("hello.html")

if __name__ == '__main__':
    app.run()
