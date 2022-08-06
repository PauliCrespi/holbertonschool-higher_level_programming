#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    query = session.query(State, City).join(City).order_by(City.id).all()
    for info in query:
        print("{}: ({}) {}".format(info[0].name, info[1].id, info[1].name))
    session.close()
