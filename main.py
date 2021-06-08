from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

app.config["SECRET_KEY"] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'


class UsersModel(db.Model):
    '''Model of db Table for Users'''
    __tablename__ = "users"
    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String, nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)
    passwords = db.relationship('PasswordsModel', backref='user')

class PasswordsModel(db.Model):
    '''Model of db Table for Passwords'''
    __tablename__ = "passwords"
    passwordID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('usersmodel.userID'), nullable=False)
    account = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.Text, nullable=False)
    salt = db.Column(db.LargeBinary, nullable=False)
    note = db.Column(db.Text, nullable=True)

db.create_all() # Create if not exists


user_put_args = reqparse.RequestParser()
user_put_args.add_argument("username", type=str, help="Username is required", required=True)
user_put_args.add_argument("firstname", type=str, help="Firstname is required", required=True)
user_put_args.add_argument("password", type=str, help="Password is required", required=True)
user_put_args.add_argument("isAdmin", type=bool, help="isAdmin (bool) is required", required=True)

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("username", type=str)
user_update_args.add_argument("firstname", type=str)
user_update_args.add_argument("password", type=str)
user_update_args.add_argument("isAdmin", type=bool)

class Users(Resource):
    def get(self, user_id=None): # Get user
        if (not user_id):
            return {"Data": "Get all"}
        
        return {"Data": "Get One"}

    def post(self, user_id=None): # Create user
        pass

    def patch(self, user_id=None): # Change 
        pass

    def delete(self, user_id=None):
        if(not user_id):
            abort(400, message="A User ID is Required")
            
        return {"Data": "User Deleted"}

api.add_resource(Users, "/user", "/user/<int:user_id>")

password_put_args = reqparse.RequestParser()
password_put_args.add_argument("account", type=str, help="Name of the acount is required", required=True)
password_put_args.add_argument("username", type=str, help="Username is required", required=True)
password_put_args.add_argument("password", type=str, help="Password is required", required=True)
password_put_args.add_argument("note", type=str, help="Optional note", required=False)

password_update_args = reqparse.RequestParser()
password_update_args.add_argument("account", type=str)
password_update_args.add_argument("username", type=str)
password_update_args.add_argument("password", type=str)
password_update_args.add_argument("note", type=str)

class Passwords(Resource):

    def get(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass

api.add_resource(Passwords, "/passwords")

if __name__ == "__main__":
    app.run(debug=True)



