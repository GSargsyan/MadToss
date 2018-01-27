from passlib.hash import pbkdf2_sha256

class Player(DBTable):
    def __init__(self):
        pass

    def check_pass(self):
        hash = pbkdf2_sha256.encrypt("password", rounds=rounds)
        return pbkdf2_sha256.verify("password", hash)

class Players(DBTable):
    @staticmethod
    def exists(username):
        pass

    @staticmethod
    def get_player(username):
        pass
