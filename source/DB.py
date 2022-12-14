from MySQLdb import _mysql
from MySQLdb.constants import FIELD_TYPE


class Database:

    def __init__(self, host, port, user, passwd, database):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database

    def connect(self):
        pass

    def query(self):
        pass

    def retrieve_row(self):
        pass

    def disconnect(self):
        pass

class MySQL(Database):

    def __init__(self):
        Database.__init__(self, host="localhost", port=3306, user="root", passwd="Pa$$w0rd", database="new_schema")
        self.convert = {FIELD_TYPE.LONG: int}
        self.db = None
        self.query_return = ""
        self.connect()

    def connect(self):
        self.db = _mysql.connect(host=self.host, port=self.port, user=self.user,
                                 password=self.passwd, database=self.database,
                                 conv=self.convert)

    def query(self, text):
        self.db.query(text)
        self.query_return = self.db.store_result()

    # get returned data with "maxrows" parameter (default: all)
    def retrieve_row(self, row_number=0):
        return self.query_return.fetch_row(maxrows=row_number)
