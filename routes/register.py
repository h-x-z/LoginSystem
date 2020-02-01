from flask import Blueprint, render_template, redirect, request, session
import jwt
import routes.auth as auth

register_b = Blueprint('register', __name__)


@register_b.route('/register', methods=['POST', 'GET'])
def register():
    if auth.loggedin():
        return redirect('/')
    if request.method == 'POST':
        q_username = request.form['username']
        q_password = request.form['password']
        user = auth.User.query.filter_by(username=q_username).first()
        if user is None:
            if len(q_password) < 8:
                return render_template('register.html', error=2, olduser=q_username)
            new_user = auth.User(username=q_username, password=q_password)
            auth.db.session.add(new_user)
            auth.db.session.commit()
            token = jwt.encode({'username': q_username, 'password': q_password}, auth.key, algorithm='HS256')
            session['token'] = token
            return redirect('/')
        if user.username == q_password:
            return render_template('register.html', error=1)
    return render_template('register.html')
