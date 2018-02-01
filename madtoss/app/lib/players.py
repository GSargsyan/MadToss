from app.lib.db_table import DBTable
from app import app
from passlib.hash import pbkdf2_sha256
from flask import session
import re


class Player(DBTable):

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
        if self is not None:
            session['pid'] = self.id
        else:
            raise ValidationError('Username doesnt exist')


class Players(DBTable):
    __initial_balance = app.config['INITIAL_BALANCE']

    @classmethod
    def __init__(self):
        self.table_name = 'players'
        super().__init__(self, self.table_name)

    @staticmethod
    def exists(username):
        res = Players().select(where="username='{}'".
                format(username), limit=1)
        return hasattr(res, 'id')

    @staticmethod
    def get_player(id=0, username=''):
        where = "id='{}'".format(id) if id != 0\
                else "username='{}'".format(username)
        result = Players().select(where=where, limit=1)
        if not result:
            return None
        return Player(result.id, result.username, result.password, result.balance)

    @staticmethod
    def register_player(player):
        """ Registeres the player in DB if valid and signs in """
        if type(player) != Player:
            raise Exception('Invalid type supplied')
        if Players.exists(player.username):
            raise ValidationError('Username ' + player.username + ' exists')

        fields = ('username', 'balance')
        values = (player.username, Players.__initial_balance)
        if hasattr(player, 'password'):
            fields = fields + ('password')
            values = values + (player.password)

        Players().insert(fields, values)
        registered = Players.get_player(username=player.username)
        registered.sign_in()


class ValidationError(Exception):
    pass
