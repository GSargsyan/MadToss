from datetime import datetime
from decimal import Decimal, ROUND_DOWN
from app import db
from app.lib.coins import CoinSides


class Bet:
    def __init__(self, id=0, player_id=0, coin_id=0, amount='',
                 date=None, outcome=None, chance='', bet_on=None):
        self.id = id
        self.player_id = player_id
        self.coin_id = coin_id
        self.amount = Decimal(amount)
        self.date = date
        self.outcome = outcome
        self.chance = Decimal(chance)
        self.bet_on = bet_on

    def balance_change(self):
        """ Calculates and returns the change of balance,
        rouding to 12 digits
        """
        return (((self.amount * Decimal(100) / self.chance) - (Decimal(0.0088) * \
            self.amount) - self.amount)  if self.outcome == self.bet_on\
            else self.amount * Decimal(-1)).quantize(Decimal('1.000000000000'),
                    rounding=ROUND_DOWN)


class Bets:
    __fields = (
        'player_id',
        'coin_id',
        'amount',
        'outcome',
        'chance',
        'bet_on')

    def __init__(self):
        pass

    @staticmethod
    def insert(bet: Bet):
        """ Inserts new bet in db and returns its id """
        return db.insert('bets', Bets.__fields,
                         tuple(val for (key, val) in bet.__dict__.items() if key in Bets.__fields), 'id')

    @staticmethod
    def new(res, params, pid, cid):
        """ Creates new bet based on args.
        Takes care of the types and win/lost decision

        Parameters
        ----------
        res: int
            Toss Result: a number between 0 and 100
        params: int
            Dict containing chance, betOn and amount
        pid: int
            Player id who made the bet
        cid: int
            Coin id by which the bet is made
        """
        if res <= params['chance']:  # Player won
            if params['betOn'] == 'H':
                outcome = CoinSides.HEADS.value
            else:  # == 'T'
                outcome = CoinSides.TAILS.value
        else:                       # Player lost
            if params['betOn'] == 'H':
                outcome = CoinSides.TAILS.value
            else:  # == 'T'
                outcome = CoinSides.HEADS.value
        return Bet(player_id=pid, coin_id=cid, amount=params['amount'],
                   date=datetime.now(), outcome=outcome, chance=params['chance'],
                   bet_on=params['betOn'])
