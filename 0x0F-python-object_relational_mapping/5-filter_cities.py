#!/usr/bin/python3
import MySQLdb
from sys import argv
if __name__ == "__main__":
    user=argv[1]
    passwd=argv[2]
    db=argv[3]
    name=argv[4]
    conn = MySQLdb.connect(host="localhost", user=user,
                           passwd=passwd, db=db,
                           port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states\
                ON  cities.state_id = states.id\
                WHERE states.name LIKE %s",
                ("%" + name + "%",))
    res = cur.fetchall()
    print(", ".join(city[0] for city in res))
    cur.close()
    conn.close()
