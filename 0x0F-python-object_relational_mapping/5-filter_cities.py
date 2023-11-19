#!/usr/bin/python3
"""Lists all states from the databaaase hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], host="localhost",
                         port=3306, password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    state_name = sys.argv[4]
    exe = """SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    HAVING BINARY states.name = %s
    ORDER BY cities.id"""
    cur.execute(exe, (state_name,))
    results = cur.fetchall()
    cities = tuple(row[1] for row in results)
    cities = ', '.join(cities)
    print(cities)
