#!/usr/bin/python3
""" Module contains script that lists all cities
    having a specific state name from database hbtn_0e_4_usa
"""
import MySQLdb


def list_cities_with_name(username, password, db_name, state):
    """ List all cities
        Args:
            username (str): username
            password (str): password
            db_name (str): database name
            state (str): state name
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
    SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC)
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    """

    try:
        cur.execute(query, (state,))
    except MySQLdb.Error:
        cur.close()

    results = cur.fetchone()
    if results:
        cities = results[0]
        print(cities.replace(",", ", "))

    cur.close()
    conn.close()


if __name__ == '__main__':
    import sys

    if (len(sys.argv) == 5):
        user = sys.argv[1]
        passwd = sys.argv[2]
        db = sys.argv[3]
        state = sys.argv[4]
        list_cities_with_name(user, passwd, db, state)
