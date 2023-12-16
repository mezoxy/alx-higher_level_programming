#!/usr/bin/python3
"""module: 12-model_state_update_id_2"""


import re
from model_state import Base, State
from sqlalchemy import create_engine as eng
import sys
from sqlalchemy.orm import sessionmaker as se

if __name__ == '__main__':

    conect = eng('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = se(bind=conect)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))

    for state in states:
        session.delete(state)

    session.commit()

    session.close()
