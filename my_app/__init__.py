import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///folder.db'
app.secret_key = 'alice-odamtten'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from my_app.api.model import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from my_app.api.views import ehealth
app.register_blueprint(ehealth)

with app.app_context():
    db.create_all()