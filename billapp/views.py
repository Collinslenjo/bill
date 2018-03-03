from billapp import app,db
from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user,utils
from werkzeug.security import generate_password_hash, check_password_hash
from models import User


# default route
@app.route("/")
def index():
	if current_user.is_authenticated:
		return render_template('index.html')
	return redirect(url_for('login'))

# static files 
@app.route('/<path:path>',methods=['GET'])
def static_file(path):
    return app.send_static_file(path)

# Login route 
@app.route('/login', methods=['GET','POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  error = None
  if request.method == 'GET':
    return render_template('login.html')
  elif request.method == 'POST':
    if request.form['email'] and request.form['password']:
      user=User.query.filter_by(email=request.form['email']).first()
      if user:
        if check_password_hash(user.password,request.form['password']):
          login_user(user)
          flash('You were successfully logged in')
          return redirect(url_for('index'))
        else:
          error = 'Invalid credentials'
      else:
        error = "user doesn't exist"
    else:
      error = "Please fill all the required fields"
  return render_template('login.html', error=error)


  # Logout route and method
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You were successfully logged out')
    return redirect(url_for('login'))


@app.route("/signup",methods=['GET','POST'])
def signup():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  error = None
  if request.method == 'GET':
    return render_template('signup.html')
  elif request.method == 'POST':
    # create user and redirect to home.
    if request.form['name'] and request.form['email'] and request.form['password']:
      if User.query.filter_by(email=request.form['email']).first():
        error = "Email address already exists"
      else:
        newuser = User(request.form['name'], request.form['email'], request.form['password'])
        db.session.add(newuser)
        db.session.commit()
        login_user(newuser)
        flash("New Account created")
        return redirect(url_for('index'))
    else:
      error = "Please fill all the required fields"
    return render_template('signup.html',error=error)