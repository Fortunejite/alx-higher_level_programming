#!/usr/bin/python3
import sys
import MySQLdb
"""
 lists all states from the database hbtn_0e_0_usa
 using mysqldb  and mysql as the sql
"""

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        port=3309,
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
