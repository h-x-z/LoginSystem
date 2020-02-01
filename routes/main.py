from flask import Blueprint, render_template, redirect, request, session
import jwt
import routes.auth as auth

main_b = Blueprint('main', __name__)


@main_b.route('/', methods=['POST'])
def main():
    token = session['token']
    account = jwt.decode(token, auth.key, algorithms=['HS256'])
    user = auth.User.query.filter_by(username=account.username).first()
    if user.username == account.username and user.password == account.password:
        return render_template('main.html', username=user.username)
    else:
        return redirect('/login')
