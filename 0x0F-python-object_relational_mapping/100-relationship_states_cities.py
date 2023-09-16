#!/usr/bin/python3
""" Module contains script that creates
    State "California" and City "San Francisco"
    from database hbtn_0e_100_usa
"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_object(user, passwd, db):
    """ create City and State objects from database
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

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    san_francisco = City(name="San Francisco")

    try:
        california.cities.append(san_francisco)
        session.add(california)
        session.commit()
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
        create_object(user, passwd, db)
