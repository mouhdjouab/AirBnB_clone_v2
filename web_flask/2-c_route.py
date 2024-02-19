#!/usr/bin/python3
"""Flask web application.

listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by  <text>.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """ 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ 'C' followed by  <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
