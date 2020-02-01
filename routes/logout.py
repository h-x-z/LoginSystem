from flask import Blueprint, redirect, session

logout_b = Blueprint('logout', __name__)

@logout_b.route('/logout')
def logout():
    session.pop('token', None)
    return redirect('/login')
