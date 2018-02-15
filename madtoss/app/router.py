import json
from datetime import datetime

from flask import Blueprint, render_template, session, redirect, request
from app.lib.players import Players
from app.lib.coins import Coins, CoinSides
from app.lib.bets import Bet, Bets

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
    # TODO: whatever comes from front-end maybe not what we expect
    if 'pid' not in session:
        return False
    player = Players.get_player(id=session['pid'])

    coin = Coins.get_coin(session['cid'])
    toss_res = coin.toss() # 0 - 100 random number
    coin.inc_nonce()       # increment nonce of the coin by 1

    params = request.json
    bet = Bets.new(toss_res, params, player.id, coin.id)
    Bets.insert(bet)
    b_change = bet.balance_change()
    print(b_change)
    player.commit_bet(bet, b_change)

    # Get new, updated player
    player = Players.get_player(id=player.id)

    response = json.dumps({'outcome': bet.outcome,
        'newBalance': str(player.balance)})
    return response
