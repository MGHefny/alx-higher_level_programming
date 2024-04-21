#!/usr/bin/python3
"""hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3], charset="utf8")
    current = connection.cursor()
    q = """
SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    q = q.format(argv[4])
    current.execute(q)
    qrow = current.fetchall()
    for r in qrow:
        print(r)
    current.close()
    connection.close()
