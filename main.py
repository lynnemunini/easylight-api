from flask import Blueprint, request, json, jsonify, Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import requests
from twilio.rest import Client
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tokens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLES

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    phoneNumber = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(100), unique=True)
    meterNumber = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
# db.create_all()

class Transaction(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    #Create Foreign Key, "users.id" the users refers to the tablename of User.
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    balance = db.Column(db.Integer)
# db.create_all()

# Home route
@app.route('/')
def home():
    return '<h1>Welcome to the API</h1>'

@app.route('/register', methods=['GET','POST'])
def register():
    d = {}
    if request.method == 'POST':
        phoneNumber = request.form['phoneNumber']
        mail = request.form['email']
        meterNumber = request.form['meterNumber']
        password = request.form.get('password')
        password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        email = User.query.filter_by(email=mail).first()
        if email is None:
            user = User(phoneNumber=phoneNumber, email=mail, meterNumber=meterNumber, password=password)
            db.session.add(user)
            db.session.commit()
            return jsonify(["Registration successful"])
        else:
            return jsonify(["User already exists"])


@app.route('/login', methods=["GET", "POST"])
def login():
    d = {}
    if request.method == 'POST':
        mail = request.form["email"]
        password = request.form["password"]
        # Check if the user exists
        login = User.query.filter_by(email=mail, password=password).first()
        password_match = check_password_hash(login.password, password)
        if password_match == False:
            return jsonify(["Wrong Credentials"])
        else:
            return jsonify([ "Login Successful"])

def sendSms():
    account_sid = os.environ.get('ACCOUNT_SID')
    auth_token = os.environ.get('AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Your meter has been charged $10.00',
        from_='+18309535162',
        to='+254790901668'
    )
    print(message.sid)

if __name__ == "__main__":
    # host='0.0.0.0', port=5000
    app.run(debug=True)