from flask import Flask, render_template
from app.lib.db import DB

app = Flask(__name__)
app.config.from_object('config')

db = DB()
db.connect(app.config['DB_HOST'], app.config['DB_USER'],
           app.config['DB_PASS'], app.config['DB_NAME'])


 
@app.route("/")
def hello():
    return render_template('index.html')
