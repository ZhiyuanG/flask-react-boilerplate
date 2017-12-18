"""hello world for flask"""
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    """ function for route / """
    return render_template("hello.html")
