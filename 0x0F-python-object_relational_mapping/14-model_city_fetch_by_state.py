#!/usr/bin/python3
""" Module contains script that prints City objects
    from database hbtn_0e_14_usa
"""
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_state(user, passwd, db):
    """ prints all City objects from database
        Args:
            user (str): name of user
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

    try:
        cities = (
            session.query(City)
            .order_by(City.id).all()
        )

        for city in cities:
            state_name = (
                session.query(State.name)
                .filter_by(id=city.state_id).first()[0]
            )
            print("{}: ({}) {}".format(state_name, city.id, city.name))
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
        fetch_state(user, passwd, db)
