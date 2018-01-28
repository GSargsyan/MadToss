import psycopg2
import psycopg2.extras


class DB:
    def __init__(self):
        pass

    def connect(self, host, user, password, dbname):
        conn_str = "host='{}' dbname='{}' user='{}' \
                password='{}'".format(host, dbname, user, password)
        self.conn = psycopg2.connect(conn_str)

    def execute(self, query, args):
        self.cur = self.conn.cursor(
            cursor_factory=psycopg2.extras.DictCursor)
        self.cur.execute(query, args)
        self.conn.commit()
        return self.cur
