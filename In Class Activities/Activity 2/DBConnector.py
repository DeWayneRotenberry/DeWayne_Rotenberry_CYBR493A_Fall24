"""
This class is used to connect your python to your cybr DB using the credentials used in the class.
You will need to install the imported packages (refer to lecture 2 slides).
You may also install it directly from here.
"""

# Package to connect to PostgreSQL
import psycopg2

# Ignore this for now
# import psycopg2-binary


class MyDB(object):
    _db_connection = None
    _db_cur = None

    def __init__(self):
        # Ensure you are using your credentials here.
        # No need to change if you followed the instructions in the class/ slides.

        self._db_connection = psycopg2.connect(host='localhost', user='cyberUser', password='c-4-9-3-A',
                                               dbname='cybrDB',port='5432')
        self._db_connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        first_return = self._db_cur.execute(query, params)
        try:
            return_me = self._db_cur.fetchall()
        except Exception:
            return_me = first_return
        return return_me

    def __del__(self):
        if self._db_connection is not None:
            self._db_connection.close()
