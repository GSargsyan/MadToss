from app import db
from typing import Tuple, List

class DBTable:

    # table_name should be set by child class
    table_name = None

    def __init__(self, table_name):
        self.table = table_name

    def select(self, fields=['*'], joins=[], where='',
               group_by='', order_by='', limit='', offset=''):
        tail = ''
        if group_by != '':
            tail += "GROUP BY {}".format(group_by)
        if order_by != '':
            tail += "ORDER BY {}".format(order_by)
        if limit != '':
            tail += "LIMIT {}".format(limit)
        if offset != '':
            tail += "OFFSET {}".format(offset)
        where = where if where != '' else 1

        query = "SELECT {} FROM {} {} WHERE {} {}"\
                .format(",".join(fields), self.table, " ".join(joins),
                        where, tail)
        if limit == 1:
            return list(db.execute(query))[0]
        return db.execute(query)


    def insert(self, fields: List, values: Tuple):
        # TODO: the code below doesn't work
        query = "INSERT INTO {} ({}) VALUES (%s)".format(
                self.table, ", ".join(fields))
        print(query)
        return db.execute(query, values)

    def update(self, changes, where=[]):
        pass
