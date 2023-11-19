#!/usr/bin/python3
"""Lists all states from the databaaase hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"
    port = 3306

    db = MySQLdb.connect(user=username, host=host,
                         port=port, password=password, database=db_name)
    cur = db.cursor()
    exe = "SELECT * FROM states ORDER BY id"
    cur.execute(exe)
    results = cur.fetchall()
    for row in results:
        print(row)
