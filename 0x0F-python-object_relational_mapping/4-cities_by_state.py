#!/usr/bin/python3
""" gets all states via python yee boi"""


def main(args):
    """ gets all state stuff"""
    if len(args) != 4:
        raise Exception("need 3 arguments!")
    db = MySQLdb.connect(host='localhost',
                         user=args[1],
                         passwd=args[2],
                         db=args[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.id = states.id
    ORDER BY cities.id ASC""")
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
