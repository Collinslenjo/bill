from billapp import app, db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


"""
User Model
"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(25))
    email = db.Column(db.String(80), primary_key=False, unique=True)
    password = db.Column(db.String(256))
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
    def __repr__(self):
        return '<User %r>' % self.email

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.email)

# Login Methods
@login_manager.user_loader
def load_user(email):
    return User.query.filter_by(email = email).first()

# Products model
class Pizza(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25))
    size = db.Column(db.String(10))
    price = db.Column(db.Integer)

    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)


# Toppings model
class Topping(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25))
    size = db.Column(db.String(10))
    price = db.Column(db.Integer)
    category = db.Column(db.String(36))

    def __init__(self, name, size, price, category):
        self.name = name
        self.size = size
        self.price = price
        self.category = category

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)


# Design the orders and toppings tables

class Order(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer)
    order_details = db.Column(db.String(600)) 
    total_amount = db.Column(db.Integer)

    def __init__(self, user_id, order_details, total_amount):
        self.user_id = user_id
        self.order_details = order_details
        self.total_amount = total_amount

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)