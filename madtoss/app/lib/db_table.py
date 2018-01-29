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

        result = db.execute(query).fetchall()
        if result is None:
            return None
        if limit == 1:
            if len(result) > 0:
                return result[0]
        return result


    def insert(self, fields: List, values: Tuple):
        # TODO: the code below doesn't work

        query = "INSERT INTO {} ({}) VALUES %s".format(
                self.table, ", ".join(str(f) for f in fields))
        return db.execute(query, (values,))

    def update(self, changes, where=[]):
        pass
