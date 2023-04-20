from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '76b7dbec0285b9d18cee5f2902c4677f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # i projektbiblioteket.

app.app_context().push()

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flaskblog import routes