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
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    order = db.relationship('Order', backref='user', lazy='dynamic')
    
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
    size = db.Column(db.String(10), unique=True)
    price = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    Order_items = db.relationship('OrderItems', backref='pizza', lazy='dynamic')

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
    category = db.Column(db.String(36))
    type = db.Column(db.String(36))
    price = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    Order_items = db.relationship('OrderItems', backref='topping', lazy='dynamic')

    def __init__(self, name, category, type, price):
        self.name = name
        self.type = type
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
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    oderId = db.relationship('OrderItems', backref='order', lazy='dynamic')

    def __init__(self, user_id):
        self.user_id = user_id

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)

class OrderItems(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    topping_id = db.Column(db.Integer, db.ForeignKey('topping.id'), nullable=False)
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())