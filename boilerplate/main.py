"""hello world for flask"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

app = Flask(__name__, static_url_path='')
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

@app.route("/")
def hello():
    """ function for route / """
    return render_template("hello.html")

if __name__ == '__main__':
    app.run()
