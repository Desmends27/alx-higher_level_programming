#!/usr/bin/python3
""" Takes a state as argument and lists all the cities of that state """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           password=argv[2], db=argv[3])
    cur = conn.cursor()

    cur.execute("SELECT cities.name FROM cities JOIN states \
                ON cities.state_id = states.id \
                WHERE states.name LIKE %s ORDER BY \
                cities.id ASC", ('%' + argv[4] + '%',))
    result = cur.fetchall()
    print(", ".join(city[0] for city in result))
    cur.close()
    conn.close()
