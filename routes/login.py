from flask import Blueprint, render_template, redirect, request, session
import jwt
import routes.auth as auth

login_b = Blueprint('login', __name__)

@login_b.route('/login', methods=['POST', 'GET'])
def login():
    if auth.loggedin():
        return redirect('/')
    if request.method == 'POST':
        q_username = request.form['username']
        q_password = request.form['password']
        user = auth.User.query.filter_by(username=q_username).first()
        if user is None:
            return render_template('login.html', error=1, users = auth.User.query.all())
        if auth.validatePassword(q_password, q_username):
            session['token'] = auth.generateToken(q_username)
            return redirect('/')
        else:
            return render_template('login.html', error=2, olduser=q_username, users=auth.User.query.all())
    else:
        return render_template('login.html', users = auth.User.query.all())