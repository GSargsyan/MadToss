from app.lib.db_table import DBTable
from app import app
from passlib.hash import pbkdf2_sha256
from flask import session
import re


class Player(DBTable):

    def __init__(self, id=0, username='', password='', balance=0):
        self.username = username
        self.__id = id
        self.__password = password
        self.balance = 0
        self.is_signed_in = False

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
        elif not re.match("^[A-Za-z0-9_]*$]", self.username):
            raise ValidationError('Invalid characters')

    def validate_password(self):
        pass

    def sign_in(self):
        self.validate_username()
        self = Players().get_player(self.username)
        if self is not None:
            session['username'] = self.username


class Players(DBTable):

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
    def get_player(username):
        """ Returns player object with the specified username if exists """
        result = Players().select(where="username='{}'".format(username),
                limit=1)

        if not result:
            return None
        print(result.id)
        return Player(result.id, result.username, result.password)

    @staticmethod
    def register_player(player):
        if type(player) != Player:
            raise Exception('Invalid type supplied')

        fields = ('username', 'balance')
        values = (player.username, player.balance)
        if hasattr(player, 'password'):
            fields = fields + ('password')
            values = values + (player.password)

        return Players().insert(fields, values)


class ValidationError(Exception):
    pass
