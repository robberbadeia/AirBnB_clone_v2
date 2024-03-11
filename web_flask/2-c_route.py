#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Method that return string 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Method that return string 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """Method that return string 'HBNB' """
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    """Main Method"""
    app.run(host='0.0.0.0', port=5000)
