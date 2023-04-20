from sqlalchemy import func
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Teams(Base):
    __tablename__ = 'teams'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    conference = Column(String())
    division = Column(String())
    wins = Column(Integer())
    losses = Column(Integer())

    players = relationship('Players', backref=backref('teams'))
    coaches = relationship('Coaches', backref=backref('teams'))

    def __repr__(self):
        return f'{self.name}, {self.conference}, {self.division} Division, ' + \
            f'record = {self.wins} - {self.losses}'

class Players(Base):
    __tablename__ = 'players'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    position = Column(String())

    team_id = Column(Integer(), ForeignKey('teams.id'))

    def __repr__(self):
        return f'{self.name}, {self.position}, ' + \
            f'age: {self.age}'

class Coaches(Base):
    __tablename__ = 'coaches'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())

    team_id = Column(Integer(), ForeignKey('teams.id'))

    def __repr__(self):
        return f'{self.name}, {self.age}'
