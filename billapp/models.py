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