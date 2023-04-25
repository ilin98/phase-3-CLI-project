#!/user/bin/env python3

import random
from faker import Faker

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Teams, Players, Coaches


if __name__ == '__main__':
    engine = create_engine('sqlite:///nba_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Teams).delete()
    session.query(Players).delete()
    session.query(Coaches).delete()

    fake = Faker()

    team_names = {
        "atlantic": ["Boston Celtics", "Brooklyn Nets", "New York Knicks", "Philadelphia 76ers", "Toronto Raptors"],
        "central": ["Chicago Bulls", "Cleveland Cavaliers", "Detroit Pistons", "Indiana Pacers", "Milwaukee Bucks"],
        "southeast": ["Atlanta Hawks", "Charlotte Hornets", "Miami Heat", "Orlando Magic", "Washington Wizards"],
        "northwest": ["Denver Nuggets", "Minnesota Timberwolves", "Oklahoma City Thunder", "Portland Trail Blazers", "Utah Jazz"],
        "pacific": ["Golden State Warriors", "Los Angeles Clippers", "Los Angeles Lakers", "Phoenix Suns", "Sacramento Kings"],
        "southwest": ["Dallas Mavericks", "Houston Rockets", "Memphis Grizzlies", "New Orleans Pelicans", "San Antonio Spurs"]
    }

    all_teams = []

    for division, teams in team_names.items():
        for team in teams:
            if team in team_names["atlantic"]:
                individual_team = Teams(
                    name=team,
                    conference="East",
                    division="Atlantic",
                    wins=0,
                    losses=0
                )
            elif team in team_names["central"]:
                individual_team = Teams(
                    name=team,
                    conference="East",
                    division="Central",
                    wins=0,
                    losses=0
                )
            elif team in team_names["southeast"]:
                individual_team = Teams(
                    name=team,
                    conference="East",
                    division="Southeast",
                    wins=0,
                    losses=0
                )
            elif team in team_names["northwest"]:
                individual_team = Teams(
                    name=team,
                    conference="West",
                    division="Northwest",
                    wins=0,
                    losses=0
                )
            elif team in team_names["pacific"]:
                individual_team = Teams(
                    name=team,
                    conference="West",
                    division="Pacific",
                    wins=0,
                    losses=0
                )
            else:
                individual_team = Teams(
                    name=team,
                    conference="West",
                    division="Southwest",
                    wins=0,
                    losses=0
                )

            session.add(individual_team)
            session.commit()

            all_teams.append(individual_team)

    coaches = []
    for team in all_teams:
        coach = Coaches(
            name=fake.name(),
            age=random.randint(30, 70),
            team_id=team.id
        )

        session.add(coach)
        session.commit()
        coaches.append(coach)

    positions = ['PG', 'SG', 'SF', 'PF', 'C']

    all_players = []
    for team in all_teams:
        for position in positions:
            player = Players(
                name=fake.name_male(),
                age=random.randint(19, 40),
                position=position,
                team_id=team.id
            )

            session.add(player)
            session.commit()
            all_players.append(player)
