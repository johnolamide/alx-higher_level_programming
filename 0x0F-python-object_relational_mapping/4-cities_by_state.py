#!/usr/bin/python3
""" Module contains script that lists all cities
    from database hbtn_0e_4_usa
"""
import MySQLdb


def list_cities(username, password, db_name):
    """ List all cities
        Args:
            username (str): username
            password (str): password
            db_name (str): database name
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
    SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    try:
        cur.execute(query)
    except MySQLdb.Error:
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
        list_cities(user, passwd, db)
