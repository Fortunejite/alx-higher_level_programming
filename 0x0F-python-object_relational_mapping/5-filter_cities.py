#!/usr/bin/python3
""" gets all states via python yee boi"""


def main(args):
    """ gets all state stuff"""
    if len(args) != 5:
        raise Exception("need 4 arguments!")
    db = MySQLdb.connect(host='localhost',
                         user=args[1],
                         passwd=args[2],
                         db=args[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id AND states.name = %s
    ORDER BY cities.id ASC""", (args[4],))
    states = cur.fetchall()
    for i in states:
        if states.index(i) == len(states) - 1:
            for state in i:
                print(str(state))
                break;
        for state in i:
            print(str(state), end=", ") 


if __name__ == "__main__":
    import sys
    import MySQLdb
    main(sys.argv)
