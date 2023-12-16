#!/usr/bin/python3
"""module: 2-my_filter_states"""


import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
            )

    cur = db.cursor()
    com = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(
            sys.argv[4])
    cur.execute(com)

    rows = cur.fetchall()
    for row in rows:
        print(row)
