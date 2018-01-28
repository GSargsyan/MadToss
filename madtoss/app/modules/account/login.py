from flask import Blueprint, render_template, request, session
from app import db
from app.lib.players import Player, Players

login_page = Blueprint('login_page', __name__,
        template_folder='templates')

class AccountHandler:
    @login_page.route('/', methods=['POST'])
    def login():
        username = request.form['login']
        password = request.form['password']
        player = Players.get_player(username)
        if player is not None:
            session['username'] = player.username
        return render_template('index.html')

    @login_page.route('/register', methods=['POST'])
    def register():
        player = Player(username=request.form['login'],
                password=request.form['password'], balance=0.0001)
        Players.register_player(player)
        return render_template('index.html')

    @login_page.route('/', methods=['GET'])
    def index():
        return render_template('login.html')

    def validate_inputs():
        pass

    def validate_login():
        pass

    def validate_password():
        pass


    
