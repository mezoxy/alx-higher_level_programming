#!/usr/bin/python3
"""Module 7-model_state_fetch_all"""


from sqlalchemy import String, Integer, Column, create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    eng = create_engine(url, echo=False)
    Session = sessionmaker(bind=eng)
    session = Session()

    lst = session.query(State).order_by(State.id).first()
    if lst:
        print("{}: {}".format(lst.id, lst.name))
    else:
        print("Nothing")

    session.close()
