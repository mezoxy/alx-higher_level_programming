#!/usr/bin/python3
"""module: 9-model_state_filter_a"""


from model_state import Base, State
from sqlalchemy import create_engine as eng
import sys
from sqlalchemy.orm import sessionmaker as se

if __name__ == '__main__':

    conect = eng('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = se(bind=conect)
    session = Session()

    state = State(name='Louisiana')
    session.add(state)
    session.commit()

    print(state.id)

    session.close()
