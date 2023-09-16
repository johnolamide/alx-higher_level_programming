#!/usr/bin/python3
""" Module script to print the State Object with name from
    the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_id_with_name(user, passwd, db, state_name):
    """ Print State object containing name from the database
        Args:
            user (str): user name
            passwd (str): password
            db (str): database
            state_name (str): state name
    """
    host = 'localhost'
    port = 3306
    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                           .format(user, passwd, host, port, db),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (
        session.query(State)
        .filter(State.name == state_name)
        .first()
    )
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == '__main__':
    import sys

    if (len(sys.argv) == 5):
        user = sys.argv[1]
        passwd = sys.argv[2]
        db = sys.argv[3]
        state_name = sys.argv[4]
        print_id_with_name(user, passwd, db, state_name)
