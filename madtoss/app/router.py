from flask import Blueprint, render_template, session
from app.lib.players import Player, Players

main_router = Blueprint('main_router', __name__,
        template_folder='templates')

@main_router.route('/home')
def init_game():
    if 'pid' not in session:
        redirect('/')

    player = Players().get_player(id=session['pid'])
    return render_template('index.html', balance=player.balance)
