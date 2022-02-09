from flask import Flask, render_template, redirect, request
from user import User


app = Flask(__name__)

app.secret_key = 'hello users'

# Main page that shows all of the users
@app.route('/')
def read(): 
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users=users)

# Page that allows the client to make a new user
@app.route('/create')
def create(): return render_template("create.html")

# Creates the new user from create
@app.route('/add_new_user', methods=['POST'])
def add_new_user():
    new_user = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.save(new_user)
    return redirect('/')


if __name__ == "__main__": app.run(debug=True, port=8000)
