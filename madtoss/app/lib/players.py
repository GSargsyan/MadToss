import re

from flask import session

from app.lib.coin import Coin
from app import app, db
from passlib.hash import pbkdf2_sha256


class Player:

    def __init__(self, id=0, username='', password='', balance=0):
        self.username = username
        self.id = id
        self.__password = password
        self.balance = balance

    def __password_matches(self, pwd_to_check):
        # rounds = app.config['PASS_ROUNDS']
        # hash = pbkdf2_sha256.encrypt("password", rounds=rounds)
        return pbkdf2_sha256.verify(pwd_to_check, self.__password)

    def validate_username(self):
        if not hasattr(self, 'username') or\
                self.username == '':
            raise ValidationError('No username')
        elif len(self.username) > 16:
            raise ValidationError('Login cannot be more than 16 chars')
        elif len(self.username) < 6:
            raise ValidationError('Login cannot be less than 6 chars')
        elif not re.match("^[A-Za-z0-9_]*$", self.username):
            raise ValidationError('Invalid characters')

    def validate_password(self):
        pass

    def sign_in(self):
        """ Validates inputs and signes the player in session
        if something goes wrong invalidates self to None
        """
        self.validate_username()
        self = Players.get_player(username=self.username)

        if self is not None:
            session['pid'] = self.id
        else:
            raise ValidationError('Username doesnt exist')


class Players:

    __initial_balance = app.config['INITIAL_BALANCE']

    def __init__(self):
        pass

    @staticmethod
    def exists(username):
        res = db.select('players', where="username='{}'".
                                format(username), limit=1)
        return hasattr(res, 'id')

    @staticmethod
    def get_player(id=0, username=''):
        where = "id='{}'".format(id) if id != 0\
                else "username='{}'".format(username)
        result = db.select('players', where=where, limit=1)
        if not result:
            return None
        return Player(result.id, result.username,
                      result.password, result.balance)

    @staticmethod
    def register_player(player):
        """ Registeres the player in DB if valid and signs in """
        if not isinstance(player, Player):
            raise Exception('Invalid type supplied')
        if Players.exists(player.username):
            raise ValidationError('Username ' + player.username + ' exists')

        fields = ('username', 'balance')
        values = (player.username, Players.__initial_balance)
        if hasattr(player, 'password'):
            fields = fields + ('password')
            values = values + (player.password)

        db.insert('players', fields, values)
        registered = Players.get_player(username=player.username)
        registered.sign_in()


class ValidationError(Exception):
    pass
