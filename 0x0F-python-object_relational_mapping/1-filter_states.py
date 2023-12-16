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
    target = 'N%'

    cur.execute("""SELECT * FROM states
            WHERE NAME LIKE %s""", (target,))

    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)

    cur.close()
    db.close()
