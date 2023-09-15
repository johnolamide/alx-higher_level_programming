#!/usr/bin/python3
""" Module contains script that lists all states with a name
    starting with N from database hbtn_0e_0_usa
"""
import MySQLdb


def list_states_with_name(username, password, db_name):
    """ List states with name startig with N
        Args:
            username (str): username
            password (str): password
            db_name (name): database name
    """
    try:
        conn = MySQLdb.connect(
            user=username,
            passwd=password,
            host='localhost',
            port=3306,
            db=db_name
        )
    except MySQL.Error:
        pass

    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    try:
        cur.execute(query)
    except MySQL.Error:
        cur.close()

    results = cur.fetchall()
    for rows in results:
        print(rows)

    cur.close()
    conn.close()


if __name__ == '__main__':
    import sys

    if (len(sys.argv) == 4):
        user = sys.argv[1]
        passwd = sys.argv[2]
        db = sys.argv[3]
        list_states_with_name(user, passwd, db)
