from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Wage(Base):
    __tablename__="wages"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    wage_aes = Column(Text, nullable=False)
    wage_ore = Column(Text)
    wage_pai = Column(Text)


if __name__ == "__main__":
    engine = create_engine("sqlite:///crypt.db")

    Base.metadata.create_all(engine)
    print "Database init successful"