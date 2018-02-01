from flask import Flask, render_template,\
        request, Blueprint, session, redirect
from app.lib.db import DB

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config['SESSION_KEY']

db = DB()
db.connect(app.config['DB_HOST'], app.config['DB_USER'],
           app.config['DB_PASS'], app.config['DB_NAME'])

from app.modules.account.account_handler import login_page
from app.router import main_router
app.register_blueprint(login_page)
app.register_blueprint(main_router)

@app.route("/")
def init():
    if 'pid' in session:
        return redirect('/home')
    return redirect('/login')
