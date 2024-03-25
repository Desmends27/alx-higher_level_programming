#!/usr/bin/python3
"""Lists all the states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    username = argv[1]
    pasw = argv[2]
    db = argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=username, password=pasw, db=db, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    result = cur.fetchall()
    for row in result:
        print(f"{row}")
        cur.close
        conn.close
