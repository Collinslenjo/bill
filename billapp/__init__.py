from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Application Configuration
app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:!Sparrtan1@localhost/bill'
# for development only
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db initialization
db = SQLAlchemy(app)
# login instance
login_manager = LoginManager()


def create_app():
    db.init_app(app)
    db.app = app
    db.create_all()
    login_manager.init_app(app)

    return app



import billapp.views
import billapp.models