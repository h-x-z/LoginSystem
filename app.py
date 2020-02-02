from flask import Flask
from routes.login import login_b
from routes.register import register_b
from routes.main import main_b
from routes.logout import logout_b
import routes.auth as auth

app = Flask(__name__)

app.register_blueprint(main_b)
app.register_blueprint(login_b)
app.register_blueprint(register_b)
app.register_blueprint(logout_b)

app.secret_key = auth.sesskey
app.run(debug=True)

