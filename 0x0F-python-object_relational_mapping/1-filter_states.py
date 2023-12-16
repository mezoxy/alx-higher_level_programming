#!/usr/bin/python3
"""module: 1-filter_states"""


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

    cur.execute("""SELECT * FROM states""")

    rows = cur.fetchall()

    for row in rows:
        if row[1][0] == 'N':
            print(row)

