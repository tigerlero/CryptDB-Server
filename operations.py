from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc

from structure import *

engine = create_engine("sqlite:///crypt.db")

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def insert(first_name,last_name, aes_enc, ore_enc, pai_enc):
    w = Wage(first_name=first_name, last_name=last_name, wage_aes=aes_enc, wage_ore=ore_enc)
    session.add(w)
    session.commit()
    return True

def getID(aes_enc):
    entry = session.query(Wage).filter_by(wage_aes=aes_enc).one()
    return entry.id

# Panos: Define a DELETE operation ( def delete(id) )