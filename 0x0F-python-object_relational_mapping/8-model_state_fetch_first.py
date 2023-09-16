#!/usr/bin/python3
""" Module script to print the first State Object from
    the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_first_state(user, passwd, db):
    """ Print first State object from the database
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

    state = session.query(State).order_by(State.id).first()
    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print("Nothing")

    session.close()


if __name__ == '__main__':
    import sys

    if (len(sys.argv) == 4):
        user = sys.argv[1]
        passwd = sys.argv[2]
        db = sys.argv[3]
        print_first_state(user, passwd, db)
