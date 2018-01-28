from flask import Flask, render_template, request, Blueprint
from app.lib.db import DB

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SESSION_KEY']

db = DB()
db.connect(app.config['DB_HOST'], app.config['DB_USER'],
           app.config['DB_PASS'], app.config['DB_NAME'])

game_page = Blueprint('game', __name__,
        template_folder='templates')
from app.modules.account.login import login_page
app.register_blueprint(login_page)
# app.register_blueprint(game_page)

"""
@app.route("/")
def index():
    return render_template('index.html')
"""
