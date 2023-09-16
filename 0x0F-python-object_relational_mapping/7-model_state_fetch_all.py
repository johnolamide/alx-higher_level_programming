#!/usr/bin/python3
""" Module script to list all State Objects from
    the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states(user, passwd, db):
    """ List all State objects from the database
        Args:
            user (str): user name
            passwd (str): password
            db (str): database
    """
    host = 'localhost'
    port = 3306
    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                           .format(user, passwd, host, port, db),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))

    session.close()


if __name__ == '__main__':
    import sys

    if (len(sys.argv) == 4):
        user = sys.argv[1]
        passwd = sys.argv[2]
        db = sys.argv[3]
        list_states(user, passwd, db)
