from hashlib import sha256

from app import app, db
from app.lib.helpers import random_alphanum, digits_from_str


class Coins:
    __fields = ('server_seed', 'server_seed_hash', 'client_seed', 'nonce')

    def __init__(self):
        pass

    @staticmethod
    def insert_new():
        """ Inserts new coin into coins and returns the id """
        ss = random_alphanum(length=app.config['SERVER_SEED_LENGTH'])
        ss_hash = sha256(ss.encode()).hexdigest()
        cs = random_alphanum(length=app.config['CLIENT_SEED_LENGTH'])
        nonce = 0
        values = (ss, ss_hash, cs, nonce)
        return db.insert('coins', Coins.__fields, values, 'id')

    @staticmethod
    def get_coin(id):
        where = "id='{}'".format(id)
        res = db.select('coins', where=where, limit=1)
        if not res:
            return None
        return Coin(res.id, res.server_seed,
                    res.server_seed_hash, res.client_seed, res.nonce)


class Coin:
    def __init__(self, id=None, ss=None,
                 ss_hash=None, cs=None, nonce=None):
        """ Full field names are in Coins.__fields.
            In this class variable names are abreviated,
            If either server_seed or client seed changes
            new Coin should be registered.
        """
        self.id = id
        self.ss = ss
        self.cs = cs
        self.nonce = nonce

    def toss(self):
        """ Uses self.seeds and self,nonce to generate random num from 0-100 """
        while True:
            # TODO: something is wrong in this loop
            to_hash = (self.ss + self.cs + str(self.nonce)).encode()
            hashout = sha256(to_hash).hexdigest()
            out = digits_from_str(hashout, length=4)
            if out:
                # Cast from  ['2', '3', '4', '5'] to 23.45
                return ''.join(out[:2]) + '.' + ''.join(out[2:])
        return None

    def inc_nonce(self):
        """ Increment nonce by 1 in DB """
        db.update('coins', {'nonce': 'nonce+1'}, 'id={}'.format(self.id))
