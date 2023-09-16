#!/usr/bin/python3
""" Module script to add new State Object to
    the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_state(user, passwd, db):
    """ Add new state Object to the database
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

    state = State(name="Louisiana")
    try:
        session.add(state)
        session.commit()
        print(state.id)
    except Exception:
        print("Error Occured")
    finally:
        session.close()


if __name__ == '__main__':
    import sys

    if (len(sys.argv) == 4):
        user = sys.argv[1]
        passwd = sys.argv[2]
        db = sys.argv[3]
        add_state(user, passwd, db)
