from flask import Blueprint, render_template, redirect, session
import jwt
import routes.auth as auth

main_b = Blueprint('main', __name__)


@main_b.route('/', methods=['POST', 'GET'])
def main():
    if auth.loggedin():
        token = session.get('token')
        account = jwt.decode(token, auth.key, algorithms=['HS256'])
        user = auth.User.query.filter_by(username=account['username']).first()
        return render_template('main.html', username=user.username)
    return redirect('/login')
