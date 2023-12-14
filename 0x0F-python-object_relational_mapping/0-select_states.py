#!/usr/bin/python3

import sys
from MySQLdb import _mysql

if __name__ == '__main__':
    db = _mysql.connect(host = "localhost",
            user = sys.argv[1],
            password = sys.argv[2],
            database = sys.argv[3])

    db.query("""SELECT * FROM states""")
