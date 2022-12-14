# user_guide: https://github.com/PyMySQL/mysqlclient/blob/main/doc/user_guide.rst
from MySQLdb import _mysql
from MySQLdb.constants import FIELD_TYPE

# if you want MYSQLdb converts returned data for you: (otherwise they'll all be strings)
my_conv = {FIELD_TYPE.LONG: int}

# connection string
db = _mysql.connect(host="localhost", port=3306, user="root",
                    password="Pa$$w0rd", database="new_schema",
                    conv=my_conv)

db.query("Select * from route_info")

## returns the entire result set to the client immediately. If your result set is really large, this could be a problem.
## One way around this is to add a LIMIT clause to your query, to limit the number of rows returned.
r1 = db.store_result()

## ...or...

## which keeps the result set in the server and sends it row-by-row when you fetch.
## This does, however, tie up server resources, and it ties up the connection
## You cannot do any more queries until you have fetched all the rows.
# r = db.use_result()


print(f"r1 = {r1.fetch_row()}")


max_route_id = 5
db.query(f"SELECT * FROM route_info WHERE route_id < {max_route_id}")
r2 = db.store_result()
print(f"r2 = {r2.fetch_row()}")