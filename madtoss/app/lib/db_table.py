import json
from typing import Tuple, List, Dict

from app import db


class DBTable:

    def _select(self, table, fields=['*'], joins=[], where='',
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

        result = db.execute(query).fetchall()
        if result is None:
            return None
        if limit == 1:
            if len(result) > 0:
                return result[0]
        return result

    def _insert(self, table, fields: List, values: Tuple, returning=None):
        query = "INSERT INTO {} ({}) VALUES %s{}".format(
                table, ", ".join(str(f) for f in fields),
                " RETURNING " + returning if returning is not None
            else "")
        return db.execute(query, (values,)).fetchone()[0]

    def _update(self, table, changes: Dict, where=''):
        query = "UPDATE {} SET {} WHERE {}".format(
                table, ', '.join(["{}={}".format(k, v)
                                  for k, v in changes.items()]),
                where if where else '1')

        db.execute(query)
