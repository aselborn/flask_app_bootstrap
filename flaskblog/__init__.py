from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '76b7dbec0285b9d18cee5f2902c4677f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # i projektbiblioteket.

app.app_context().push()

db = SQLAlchemy(app)

from flaskblog import routes