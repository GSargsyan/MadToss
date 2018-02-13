from datetime import datetime
from decimal import Decimal
from app import db
from app.lib.coins import CoinSides


class Bet:
    def __init__(self, id=None, player_id=None, coin_id=None, amount=None,
                 date=None, outcome=None, chance=None, bet_on=None):
        self.id = id
        self.player_id = player_id
        self.coin_id = coin_id
        self.amount = amount
        self.date = date
        self.outcome = outcome
        self.chance = chance
        self.bet_on = bet_on

    def balance_change(self):
        """ Calculates and returns the change of balance """
        return self.amount * (Decimal(100) / self.chance) - Decimal(0.0088) * \
            self.amount if self.outcome == self.bet_on else self.amount * -1


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
        amount = Decimal(params['amount'])
        chance = Decimal(params['chance'])
        return Bet(player_id=pid, coin_id=cid, amount=amount,
                   date=datetime.now(), outcome=outcome, chance=chance,
                   bet_on=params['betOn'])
