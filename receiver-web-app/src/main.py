from flask import Flask
from flask import request
app = Flask(__name__)
from .send import say_hello


@app.route('/', methods=['POST'])
def receiver():
    text = request.form['text']
    print(text)
    say_hello(text)
    return ''
