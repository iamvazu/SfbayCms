#main.py

from flask import *
from flask_sqlalchemy import SQLAlchemy

import os, sys

print ('test')

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
