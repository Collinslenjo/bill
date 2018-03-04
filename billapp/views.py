from billapp import app,db
from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user,utils
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Pizza, Topping, Order 


# default route
@app.route("/")
def index():
	if current_user.is_authenticated:
		return render_template('index.html',title="Home")
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
    return render_template('login.html',title="Login")
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
  return render_template('login.html', error=error,title="Login")


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
    return render_template('signup.html',title="Signup")
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
    return render_template('signup.html',error=error,title="Signup")


# Create Pizza Sizes
@app.route('/pizza',methods=['GET','POST'])
@login_required
def pizza():
  if request.method == 'GET':
    pizzas = Pizza.query.all()
    return render_template('pizza.html',title="Pizza",pizzas=pizzas)
  elif request.method == 'POST':
    if request.form['name'] and request.form['size'] and request.form['price']:
      if Pizza.query.filter_by(size=request.form['size']).first():
        error = "Pizza Size already exists"
      else:
        newPizza = Pizza(request.form['name'],request.form['size'],request.form['price'])
        db.session.add(newPizza)
        db.session.commit()
        flash("New Pizza Added")
        return redirect(url_for('pizza'))
    else:
      error = "Please fill all the required fields"
    return render_template('pizza.html',title="Pizza")
# Show pizza
@app.route('/pizza/<int:id>', methods=['GET', 'POST'])
@login_required
def view_app(id):
  # List the pizza details
  pizza = Pizza.query.filter_by(id=id).first()
  return render_template('view.html',pizza=pizza)

# Edit Pizza
@app.route('/pizza/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_pizza(id):
  pizza = Pizza.query.get_or_404(id)
  if request.method == 'POST':
    if request.form['name'] and request.form['size'] and request.form['price']:
      pizza.name = request.form['name']
      pizza.size = request.form['size']
      pizza.price = request.form['price']
      db.session.add(pizza)
      db.session.commit()
      flash('You have successfully Edited the pizza.')
      return redirect(url_for('pizza'))
  return render_template('editpizza.html',form=pizza, id=id)
# Delete Pizza
@app.route('/pizza/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_pizza(id):
  pizza = Pizza.query.get_or_404(id)
  db.session.delete(pizza)
  db.session.commit()
  flash('You have successfully deleted the pizza.')
  return redirect(url_for('pizza'))