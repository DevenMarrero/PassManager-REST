from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import sqlalchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

#SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'