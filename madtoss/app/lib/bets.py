
class Bet(DBTable):
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id', None)
