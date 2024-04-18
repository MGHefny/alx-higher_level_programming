#!/usr/bin/python3
""" hbtn_0e_0_usa """
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    # connection database
    d = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], d=argv[3])

    c = d.cursor()
    c.execute("SELECT * FROM states")

    rows = c.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    c.close()
    d.close()
