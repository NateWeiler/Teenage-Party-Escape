from flask import Flask # glorious framework
# from flask_sqlalchemy import SQLAlchemy # database time in SQLite

app = Flask(__name__)
app.config.from_object('config')
app.static_folder = 'static'
# db = SQLAlchemy(app)

from app import views #, models
