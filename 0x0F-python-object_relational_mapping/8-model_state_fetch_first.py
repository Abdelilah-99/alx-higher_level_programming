#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

import sys

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    LH = "localhost"
    Session = sessionmaker()
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@{LH}/{sys.argv[3]}',
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()

    if query := session.query(State).order_by(State.id).first():
        print("{}: {}".format(query.id, query.name))
    else:
        print('Nothing')
