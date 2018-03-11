from billapp import app,db
from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user,utils
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Pizza, Topping, Order, PizzaOrderItems, ToppingOrderItems
import json, ast, sys

# default route
@app.route("/")
def index():
  if current_user.is_authenticated:
    pizza = Pizza.query.all()
    toppingsmall = Topping.query.filter_by(type="small")
    toppingmedium = Topping.query.filter_by(type="medium")
    topping = Topping.query.filter_by(type="large")
    return render_template('index.html',title="Home", pizzas=pizza, toppings=topping, toppingsmall=toppingsmall,toppingmedium=toppingmedium)
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

  # Create toppings
@app.route('/topping',methods=['GET','POST'])
@login_required
def topping():
  if request.method == 'GET':
    toppings = Topping.query.all()
    return render_template('topping.html',title="Toppings",toppings=toppings)
  elif request.method == 'POST':
    if request.form['name'] and request.form['category'] and request.form['type'] and request.form['price']:
      if Pizza.query.filter_by(name=request.form['name']).first():
        error = "Topping already exists"
      else:
        newTopping = Topping(request.form['name'],request.form['category'],request.form['type'],request.form['price'])
        db.session.add(newTopping)
        db.session.commit()
        flash("New Topping Added")
        return redirect(url_for('topping'))
    else:
      error = "Please fill all the required fields"
    return render_template('topping.html',title="Toppings")
# Show topping
@app.route('/topping/<int:id>', methods=['GET', 'POST'])
@login_required
def view_topping(id):
  # List the topping details
  topping = Topping.query.filter_by(id=id).first()
  return render_template('view_topping.html',topping=topping)

# Edit topping
@app.route('/topping/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_topping(id):
  topping = Topping.query.get_or_404(id)
  if request.method == 'POST':
    if request.form['name'] and request.form['category'] and request.form['type'] and request.form['price']:
      topping.name = request.form['name']
      topping.type = request.form['type']
      topping.size = request.form['category']
      topping.price = request.form['price']
      db.session.add(topping)
      db.session.commit()
      flash('You have successfully Edited the topping.')
      return redirect(url_for('topping'))
  return render_template('edit_topping.html',form=topping, id=id)
# Delete topping
@app.route('/topping/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_topping(id):
  topping = Topping.query.get_or_404(id)
  db.session.delete(topping)
  db.session.commit()
  flash('You have successfully deleted the topping.')
  return redirect(url_for('topping'))

# Orders
@app.route('/order', methods=['POST'])
@login_required
def order():
  json_data = ast.literal_eval(json.dumps(request.form))
  data = json.loads(json.dumps(json_data, sys.stdout))['cart_list']
  datas = ast.literal_eval(data)
  order = Order(user_id=current_user.id)
  db.session.add(order)
  db.session.commit()
  for item in datas:
    pizza = Pizza.query.get_or_404(item['product_id'])
    topping = Topping.query.get_or_404(item['topping_id'])
    quantity = item['product_quantity']
    if pizza != None:
      pizza_items = PizzaOrderItems(order.id,pizza.id,quantity)
      db.session.add(pizza_items)
      db.session.commit()
    if topping != None:
      topping_items = ToppingOrderItems(order.id,topping.id,quantity)
      db.session.add(topping_items)
      db.session.commit()
  return generate_receipt(order.id)

  # return redirect(url_for('index'))

@app.route('/receipt/<int:id>', methods=['GET','POST'])
@login_required
def generate_receipt(id):
  topping_items = ToppingOrderItems.query.filter_by(order_id=id).all()
  pizza_items = PizzaOrderItems.query.filter_by(order_id=id).all()
  topps = [item.topping_id for item in topping_items]
  topp_q = [item.quantity for item in topping_items]
  pizz_q = [item.quantity for item in pizza_items]
  toppings = Topping.query.filter(Topping.id.in_(topps))
  items = [item.pizza_id for item in pizza_items]
  pizzas = Pizza.query.filter(Pizza.id.in_(items))
  return render_template('receipt.html', title="receipt", toppings=toppings, pizzas=pizzas,topp_q=topp_q,pizz_q=pizz_q)