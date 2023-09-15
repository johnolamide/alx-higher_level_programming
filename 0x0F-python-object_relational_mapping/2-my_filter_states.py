#!/usr/bin/python3
""" Module contains script that lists all states
    with a specific state name from database hbtn_0e_0_usa
"""
import MySQLdb


def list_states_with_name(username, password, db_name, state_name):
    """ List states with state_name
        Args:
            username (str): username
            password (str): password
            db_name (str): database name
            state_name (str): state name to search
    """
    try:
        conn = MySQLdb.connect(
            user=username,
            passwd=password,
            host='localhost',
            port=3306,
            db=db_name
        )
    except MySQLdb.Error:
        pass

    cur = conn.cursor()
    query = """
    SELECT * FROM states
    WHERE name = '{}'
    ORDER BY states.id ASC
    """
    query = query.format(str(state_name))
    try:
        cur.execute(query)
        results = cur.fetchall()
        for rows in results:
            print(rows)
    except MySQLdb.Error:
        cur.close()
    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    import sys

    if (len(sys.argv) == 5):
        user = sys.argv[1]
        passwd = sys.argv[2]
        db = sys.argv[3]
        state = sys.argv[4]
        list_states_with_name(user, passwd, db, state)
