from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
import jwt

key = 'oghC/Vqm+TCKtaJMrEx0JQ=='
sesskey = 'LzbUPcyF3uRpyaNhjNA+tQ=='

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

def loggedin():
    if session.get('token') is not None:
        token = session.get('token')
        account = jwt.decode(token, key, algorithms=['HS256'])
        user = User.query.filter_by(username=account['username']).first()
        if user.username == account['username'] and user.password == account['password']:
            return True
    return False
