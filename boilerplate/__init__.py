"""hello world for flask"""
from flask import Flask, url_for
from flask import render_template
app = Flask(__name__, static_url_path='')

@app.route("/")
def hello():
    """ function for route / """
    return render_template("hello.html")
