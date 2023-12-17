#!/usr/bin/python3
"""module: 12-model_state_update_id_2"""


from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine as eng
import sys
from sqlalchemy.orm import sessionmaker as se

if __name__ == '__main__':

    conect = eng('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = se(bind=conect)
    session = Session()

    StatAndCity = session.query(City, State.name).filter(
            City.state_id == State.id).all()

    for city, state in StatAndCity:
        print("{}: ({}) {}".format(state, city.id, city.name))

    session.close()
