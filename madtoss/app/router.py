from flask import Blueprint, render_template

main_router = Blueprint('main_router', __name__,
        template_folder='templates')

@main_router.route('/home')
def init_game():
    return render_template('index.html', balance=14)
