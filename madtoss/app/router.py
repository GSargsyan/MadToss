from flask import Blueprint, render_template, session, redirect, request
from app.lib.players import Players
from app.lib.coin import Coins

main_router = Blueprint('main_router', __name__,
                        template_folder='templates')


@main_router.route('/')
def index():
    # session.clear()
    if 'pid' not in session:
        return redirect('/login')
    else:
        return redirect('/home')


@main_router.route('/home', methods=['GET'])
def init_game():
    if 'pid' not in session:
        redirect('/')

    player = Players.get_player(id=session['pid'])
    return render_template('index.html', balance=player.balance)


@main_router.route('/toss', methods=['POST'])
def toss():
    if 'pid' not in session:
        return False
    player = Players.get_player(id=session['pid'])

    coin = Coins.get_coin(session['cid'])
    outcome = coin.toss()
    coin.inc_nonce()
    return outcome
