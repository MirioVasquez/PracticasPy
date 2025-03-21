from flask import Flask, url_for, redirect, render_template, Request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'hola'
app.permanent_session_lifetime = timedelta(minutes=5)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if Request.method == 'POST':
        session.permanent = True
        user = Request.form['nm']
        session['user'] = user
        
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session['email'] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()
            
        flash('You have been logged in successfully!', 'info')
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            flash('Already logged in', 'info')
            return redirect(url_for('user'))
        
        return render_template('login.html')

@app.route('/user', methods=['POST','GET'])
def user():
    email = None
    if 'user' in session:
        user = session['user']
        
        if Request.method == 'POST':
            email = Request.form['email']
            session['email'] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash('Email was saved!')
        else:
            if 'email' in session:
                email = session['email']
        return render_template('user.html', user=user)
    else:
        flash('You need to logged in', 'info')
        return redirect(url_for('login'))

@app.route('/view')
def view():
    if 'user' in session:
        return render_template('view.html', values=users.query.all())
    else:
        flash('You need to logged in', 'info')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    if 'user' in session:
        flash('You have been logged out!', 'info')
    else:
        flash('You have been already logged out')
    session.pop('user', None)
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()