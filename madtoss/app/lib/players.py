from app.lib.db_table import DBTable
from passlib.hash import pbkdf2_sha256

class Player(DBTable):

    def __init__(self, id=0, username='', password='', balance=0):
        self.username = username
        self.__id = id
        self.__password = password
        self.balance = 0

    def check_pass(self, pwd_to_check):
        # hash = pbkdf2_sha256.encrypt("password", rounds=rounds)
        return pbkdf2_sha256.verify(pwd_to_check, self.__password)


class Players(DBTable):

    @classmethod
    def __init__(self):
        self.table_name = 'players'
        super().__init__(self, self.table_name)

    @staticmethod
    def exists(username):
        pass

    @staticmethod
    def get_player(username):
        """ Returns player object with the specified username if exists """
        result = Players().select(where="username='{}'".format(username),
                limit=1)

        if not result:
            return None

        return Player(result['id'], result['username'], result['password'])

    @staticmethod
    def register_player(player):
        print(type(player))
        if type(player) != Player:
            raise Exception('Invalid type supplied')

        fields = ('username', 'balance')
        values = (player.username, player.balance)
        if hasattr(player, 'password'):
            fields = fields + ('password')
            values = values + (player.password)

        return Players().insert(fields, values)
        

    @staticmethod
    def login_player(player):
        pass
