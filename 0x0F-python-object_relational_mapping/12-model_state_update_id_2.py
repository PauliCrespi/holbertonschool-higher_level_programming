#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    try:
        query = session.query(State).filter(State.id.like('2'))
        for state in query:
            state.name = 'New Mexico'
        session.commit()
    except SQLAlchemyError as e:
        print("Not found")
    finally:
        session.close()
