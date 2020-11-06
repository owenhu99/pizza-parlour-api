from flask import Flask

app = Flask("Assignment 2")

@app.route('/')
def index():
    return 'Home page'

@app.route('/pizza')
def welcome_pizza():
    return 'Welcome to Pizza Planet!'

if __name__ == "__main__":
    app.run()
