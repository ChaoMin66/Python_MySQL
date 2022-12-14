from source import DB

mysqldb = DB.MySQL()
mysqldb.query("Select * from route_info")


result_all = mysqldb.retrieve_row()
print(f"All rows: {result_all}\n")


mysqldb.query("Select * from route_info")
i = 1
result_single = mysqldb.retrieve_row(1)
while result_single:
    print(f"Row[{i}]: {result_single}")
    result_single = mysqldb.retrieve_row()
    i += 1
