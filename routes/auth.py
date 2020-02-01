from flask import Flask
from flask_sqlalchemy import SQLAlchemy

key = 'oghC/Vqm+TCKtaJMrEx0JQ=='

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username} created>'
