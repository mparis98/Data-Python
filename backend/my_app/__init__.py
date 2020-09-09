from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root%@localhost/company'
db = SQLAlchemy(app)

from my_app.company.views import company
app.register_blueprint(company)

db.create_all()