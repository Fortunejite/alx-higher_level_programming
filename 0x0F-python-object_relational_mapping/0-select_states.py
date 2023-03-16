#!/usr/bin/python3
import sys
import MySQLdb
"""
 lists all states from the database hbtn_0e_0_usa
 using mysqldb  and mysql as the sql
"""

db = MySQLdb.connect(
    host="localhost",
    user=sys.argv[1],
    passwd=sys.argv[2],
    port=3309,
    db=sys.argv[3]
)
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id;")
result = cursor.fetchall()
for row in result:
    print(row)
db.close()