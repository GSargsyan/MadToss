from flask import Blueprint, render_template, request, session, redirect
from app import db
from app.lib.players import Player, Players, ValidationError
from app.lib.coin import Coins

login_page = Blueprint('login_page', __name__,
                       template_folder='templates')


class AccountHandler:

    @login_page.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')

        # if method == 'POST'
        username = request.form['login']
        password = request.form['password']

        player = Player(username=username, password=password)

        try:
            player.sign_in()
        except ValidationError as ve:
            return render_template('login.html', error=str(ve))

        # Create new coin and write its id in session
        session['cid'] = Coins.insert_new()

        return redirect('/home')

    @login_page.route('/register', methods=['POST'])
    def register():
        login = request.form['login']
        if Players.exists(login):
            return 'Error: Username is busy'
        player = Player(username=login,
                        password=request.form['password'])
        try:
            Players.register_player(player)
        except ValidationError as ve:
            return render_template('login.html', error=str(ve))
        return redirect('/')
