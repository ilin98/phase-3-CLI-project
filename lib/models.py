from sqlalchemy import func
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Teams(Base):
    __tablename__ = 'teams'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    conference = Column(String())
    division = Column(String())
    wins = Column(Integer())
    losses = Column(Integer())

    def __repr__(self):
        return f'{self.name}, {self.conference}, {self.division} Division, ' + \
            f'record = {self.wins} - {self.losses}'
