#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''returns Hello'''
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''returns HBNB'''
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def display_text():
    '''returns C ” followed by the value of the text variable'''
    return (f'C {text.replace('_', ' ')}')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
