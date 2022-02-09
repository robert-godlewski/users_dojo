from flask import Flask, render_template, redirect, session, request


app = Flask(__name__)

app.secret_key = 'hello users'

@app.route('/')
def read(): return render_template("index.html")

@app.route('/create')
def create(): return render_template("create.html")


if __name__ == "__main__": app.run(debug=True, port=8000)
