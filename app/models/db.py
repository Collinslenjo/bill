from flask import Flask

# Application Configuration
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:!Sparrtan1@localhost/drive'

# Db configuration
db = SQLAlchemy(app)
# def init_db():
#     db.init_app(app)
#     db.app = app
#     db.create_all()