import psycopg2
import psycopg2.extras
from typing import Tuple, List, Dict


class DB:
    def __init__(self):
        pass

    def connect(self, host, user, password, dbname):
        conn_str = "host='{}' dbname='{}' user='{}' \
                password='{}'".format(host, dbname, user, password)
        self.conn = psycopg2.connect(conn_str)

    def execute(self, query, args=''):
        self.cur = self.conn.cursor(
            cursor_factory=psycopg2.extras.NamedTupleCursor)
        self.cur.execute(query, args)
        self.conn.commit()
        return self.cur

    def select(self, table, fields=['*'], joins=[], where='',
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

        query = "SELECT {} FROM {} {} WHERE {} {}"\
                .format(",".join(fields), table, " ".join(joins),
                        where if where else '1', tail)

        result = self.execute(query).fetchall()
        if result is None:
            return None
        if limit == 1:
            if len(result) > 0:
                return result[0]
        return result

    def insert(self, table, fields: List, values: Tuple, returning=None):
        query = "INSERT INTO {} ({}) VALUES %s{}".format(
                table, ", ".join(str(f) for f in fields),
                " RETURNING " + returning if returning is not None
            else "")
        return self.execute(query, (values,)).fetchone()[0]

    def update(self, table, changes: Dict, where=''):
        query = "UPDATE {} SET {} WHERE {}".format(
                table, ', '.join(["{}={}".format(k, v)
                                  for k, v in changes.items()]),
                where if where else '1')

        self.execute(query)
