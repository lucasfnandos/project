from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from project.helper import usd, contact, comp_id


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SECRET_KEY'] = ''

UPLOAD_FOLDER = 'project/static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

login_manager = LoginManager(app)

app.jinja_env.filters["usd"] = usd
app.add_template_filter(contact)
app.add_template_filter(comp_id)

from project import routes



