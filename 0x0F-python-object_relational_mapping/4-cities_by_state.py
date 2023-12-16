#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':

    con = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3])

    cur = con.cursor()
    cur.execute(
        "SELECT c.id, c.name, s.name\
        FROM cities AS c\
        JOIN states As s\
        ON c.state_id = s.id")

    for row in cur.fetchall():
        print(row)
