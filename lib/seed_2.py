import random
from faker import Faker

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Teams, Players, Coaches


if __name__ == '__main__':
    engine = create_engine('sqlite:///nba_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    team_name = 'Toronto Raptors'
    team = session.query(Teams).filter_by(name=team_name).first()
    if team:
        team.wins += 1
        session.commit()
        print(f"Team '{team_name}' has now {team.wins} wins.")
    else:
        print(f"Team '{team_name}' not found in the database.")
