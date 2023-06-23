from flask import Flask, session, redirect, url_for, request , flash , render_template
from auth import Auth
from data import Data

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    if 'loggedIn' in session:
        if session['loggedIn']:

            db = Data(session['username'])
            data=db.getUserData()
            del db

            return render_template('index.html' , username=session["username"] , data=data)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        handler = Auth(username)
        cpass = handler.getPassword()
        del handler
        if password == cpass:
            session['loggedIn'] = True 
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash("Incorrect username or password!!")
            return redirect(url_for('login'))
    return render_template("login.html")

@app.route('/logout')
def logout():
    try:
        session.pop('loggedIn')
        session.pop('username')
    finally:
        return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        handler = Auth(username)
        temp = handler.setPassword(password)
        del handler
        if temp:
            return redirect(url_for('login'))
        else:
            flash(f"Username \"{username}\" already exists!!")
            return redirect(url_for('signup'))

    return render_template('signup.html')


#API

@app.route('/api/todo/create', methods=["POST"])
def create():
    task = request.form["task"]
    db = Data(session['username'])
    db.setUserData(task)
    del db
    return redirect(url_for('index')) 

@app.route('/api/todo/update', methods=["POST"])
def update():
    print(request.form)
    data = request.form["update"]
    status = data.split(" ")[-1]
    task = data.rstrip(status).strip()
    print(task)
    db = Data(session['username'])
    db.updUserData(task, status)
    del db
    return redirect(url_for('index')) 

@app.route('/api/todo/delete',methods=["POST"])
def delete():
    task = request.form["delete"]
    db = Data(session['username'])
    db.delUserData(task)
    del db
    return redirect(url_for('index')) 


if __name__ == '__main__':
    app.run(debug=True)