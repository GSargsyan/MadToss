import psycopg2
import psycopg2.extras


class Postgres(object):

    __insert = "INSERT INTO %s(%s) VALUES (%s)%s"
    __update = "UPDATE %s SET %s WHERE %s"
    __select = "SELECT %s FROM %s %s WHERE %s %s"
    __select_count = "SELECT SUM(src.count) as count FROM (%s) as src"
    __delete = "DELETE FROM %s WHERE %s"
    debug = False

    def __init__(self, host, user, pwd, dbname):
        # try:
        self.host = host
        self.user = user
        self.pwd = pwd
        self.dbname = dbname
        self.transaction = False
        self.conn = psycopg2.connect(
            "dbname='{}' user='{}' host='{}' password='{}'".format(
                self.dbname, self.user, self.host, self.pwd))

        super().__init__()
        # except:
        #    print "DB yokhen!"

    def reconnect(self):
        self.conn.close()
        self.conn = psycopg2.connect(
            "dbname='{}' user='{}' host='{}' password='{}'".format(
                self.dbname, self.user, self.host, self.pwd))

    def execute(self, query, args={}):
        # reconnect to database if connection is closed
        if self.conn.closed != 0:
            self.reconnect()

        # create cursor
        self.cur = self.conn.cursor(
            cursor_factory=psycopg2.extras.NamedTupleCursor)

        if (self.debug):
            print("\n---Begin query---\n{0}\n---End query---\n".format(
                self.cur.mogrify(query, args)))
        try:
            self.cur.execute(query, args)
            if not self.transaction:
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise Exception(e)
        return self.cur

    def commit(self):
        if self.transaction:
            self.conn.commit()
            self.transaction = False

    def rollback(self):
        self.conn.rollback()
        self.transaction = False

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cur.close()
            self.cur = None

    def select(self, fields, table, where, args={}, joins=[],
               group_by='', order_by='', limit=-1, offset=-1):
        query_tail = []
        if len(group_by) > 0:
            query_tail.append('GROUP BY %s' % group_by)
        if len(order_by) > 0:
            query_tail.append('ORDER BY %s' % order_by)
        if limit > 0:
            query_tail.append('LIMIT %(limit)s')
            args['limit'] = limit
        if offset > 0:
            query_tail.append('OFFSET %(offset)s')
            args['offset'] = offset

        return self.execute(self.__select % (', '.join(fields),
                                             table, ' '.join(joins), where,
                                             " " . join(query_tail)), args)

    def find(self, fields, table, where=True, args={}, joins=[],
             group_by='', order_by='', limit=-1, offset=-1):
        res = self.select(fields=fields, table=table, where=where, args=args,
                          joins=joins, group_by=group_by, order_by=order_by,
                          limit=limit, offset=offset)
        return res.fetchone() if res else None

    def all(self, fields, table, where=True, args={}, joins=[],
            group_by='', order_by='', limit=-1, offset=-1):
        res = self.select(fields=fields, table=table, where=where, args=args,
                          joins=joins, group_by=group_by, order_by=order_by,
                          limit=limit, offset=offset)
        return res.fetchall() if res else None

    def insert(self, table, values, ret=''):
        fields = {key: "%%(%s)s" % key for key in values}
        query = self.__insert % (table, ", " . join(fields.keys()),
                                 ", " . join(fields.values()),
                                 ' RETURNING %s' % ret if ret else '')
        return self.execute(query, values)

    def update(self, table, values, where, args={}):
        fields = ["%s=%%(%s)s" % (key, key) for key in values]
        values = {**values, **args}
        query = self.__update % \
            (table, ", " . join(fields), where)
        return self.execute(query, values)

    def delete(self, table, where, args={}):
        return self.execute(self.__delete % (table, where), args)
