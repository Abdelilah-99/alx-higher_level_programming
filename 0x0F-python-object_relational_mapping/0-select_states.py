#!/usr/bin/python3
import sys
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], host="localhost", db=sys.argv[3], port=3306)
    cur = db.cursor()
    exe = "SELECT * FROM states ORDER BY id"
    cur.execute(exe)
    results = cur.fetchall()
    for row in results:
        print(row)
