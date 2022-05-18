from flask import Flask, render_template

app = Flask('Hello')

@app.route('/')
def hello():
    return render_template('hello.html')
