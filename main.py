from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tokens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    phone_no = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    meter_no = db.Column(db.String(1000), nullable=False)
    password = db.Column(db.String(100))

db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
