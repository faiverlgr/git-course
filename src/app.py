
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Bye Code!"

@app.route('/hello')
def greating():
    return "Hello World!"

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    resultado = a + b
    return f"La suma es: {str(resultado)}"