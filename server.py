from flask import Flask, render_template, redirect, request
from user import User


app = Flask(__name__)

app.secret_key = 'hello users'

# Used to search for the id to rout for showing individual groups
def search_by_id(form_data):
    data = {
        "first_name": form_data['first_name'],
        "last_name": form_data['last_name'],
        "email": form_data['email']
    }
    data_id_raw = User.get_id_by_email(data)
    return data_id_raw[0]['id']


# index is routed to users
@app.route('/')
def main_page(): return redirect("/users")

# Main page that shows all of the users
@app.route('/users')
def read(): 
    users = User.get_all()
    return render_template("index.html", all_users=users)

# Page that allows the client to make a new user
@app.route('/users/new')
def new(): return render_template("new_user.html")

# Creates the new user from create
@app.route('/user/create', methods=['POST'])
def create():
    User.save(request.form)
    # return redirect('/users')
    data_id = search_by_id(request.form)
    return redirect(f'/user/show/{data_id}')

# Shows you only one user
@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id": id
    }
    return render_template("show_user.html", user=User.get_one(data))

# Edits a user
@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    return render_template("edit_user.html", user=User.get_one(data))

# Updates the new edits
@app.route('/user/update', methods=['POST'])
def update():
    User.edit_one(request.form)
    # return redirect('/users')
    data_id = search_by_id(request.form)
    return redirect(f'/user/show/{data_id}')

# Finds the user to delete and removes them from the database
@app.route('/user/destroy/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    User.destroy_one(data)
    return redirect('/users')


if __name__ == "__main__": app.run(debug=True, port=8000)
