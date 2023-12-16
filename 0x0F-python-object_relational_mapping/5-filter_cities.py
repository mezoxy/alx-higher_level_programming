#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':

    cone = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3])

    cur = cone.cursor()
    target = sys.argv[4].split("'")[0]

    cur.execute("SELECT name FROM cities\
            WHERE state_id = (\
            SELECT id FROM states\
            WHERE name = %s)", (sys.argv[4],))

    rows = cur.fetchall()
    cities = ", ".join(city[0] for city in rows)
    print(cities)
