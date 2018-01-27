import psycopg2


class DB:
    def __init__(self):
        pass

    def connect(self, host, user, password, dbname):
        conn_str = " host='{}' dbname='{}' user='{}' \
                password='{}'".format(host, dbname, user, password)
        self.conn = psycopg2.connect(conn_str)

    def execute(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        return cur.fetchall()


class DBTable:

    def __init__(self, table_name):
        self.table = table_name

    def select(self, fields=['*'], joins={}, where=[],
               group_by='', order_by='', limit='', offset=''):
        pass

    def insert(self, fields, values):
        pass

    def update(self, changes, where=[]):
        pass
