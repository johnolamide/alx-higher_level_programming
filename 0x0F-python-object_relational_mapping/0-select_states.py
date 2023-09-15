#!/usr/bin/python3
""" Module contains script that lists all states from a database
"""
import MySQLdb


def list_states(username, password, database_name):
    """ function to list all states in a database
        Args:
            username (str): username
            password (str): password
            database_name (str): database name
    """
    try:
        conn = MySQLdb.connect(
            user=username,
            passwd=password,
            host='localhost',
            port=3306,
            db=database_name
        )
    except MySQLdb.Error:
       pass

    cur = conn.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    try:
        cur.execute(query)
    except MySQLdb.Error:
        conn.close()

    results = cur.fetchall()
    for rows in results:
        print(rows)

    cur.close()
    conn.close()


if __name__ == '__main__':
    import sys

    if (len(sys.argv) > 4):
        user = sys.argv[1]
        passwd = sys.argv[2]
        db = sys.argv[3]
        list_states(user, passwd, db)
    else:
        pass
