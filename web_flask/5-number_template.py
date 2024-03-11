#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, render_template

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


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ replace more text with another variable. """
    text = text.replace('_', ' ')
    return f'Python {text}'


# Retur 'n' only when int value passed
@app.route('/number/<int:n>', strict_slashes=False)
def display_n(n):
    """Method that return string 'HBNB' """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_template(n):
    """Method that return HTML template"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    """Main Method"""
    app.run(host='0.0.0.0', port=5000)
