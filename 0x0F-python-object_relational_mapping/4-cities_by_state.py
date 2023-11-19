#!/usr/bin/python3
"""Lists all states from the databaaase hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], host="localhost",
                         port=3306, password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    exe = """SELECT cities.id, cities.name, state.name
	FROM cities AS cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id"""
    cur.execute(exe)
    results = cur.fetchall()
    for row in results:
        print(row)
