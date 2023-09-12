from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from models import Teams, Players, Coaches

engine = create_engine('sqlite:///nba_db.db')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

def search():
    search = input('What would you like to search? ')
    return search

def get_lineup():
    while True:
        team_name = input('Which team? (type "back" to go back to search) ')

        if team_name == 'back':
            return False

        selected_team = session.query(Teams).filter(Teams.name.ilike(f'%{team_name}%')).first()

        if selected_team is None:
            print(f"No team named '{team_name}' was found.")

        else:
            players = session.query(Players.name, Players.position).filter(Players.team_id == selected_team.id).all()

            print(f"The following players are on the {selected_team.name}:")
            for player in players:
                print(f"{player.name}, {player.position}")
            return True


def get_all_position():
    while True:
        position = input('Which position? (type "back" to go back to search) ')

        if position == 'back':
            return False

        players = session.query(Players.name, Teams.name)\
            .join(Teams, Players.team_id == Teams.id)\
            .filter(Players.position.ilike(f'%{position}%'))\
            .all()

        if not players:
            print(f"No position named '{position}' was found.\nChoose one of the following: PG, SG, SF, PF, C.")
        else:
            print(f"The following players play {position}:")
            for player in players:
                print(f"{player[0]} ({player[1]})")
            return True


def get_standings():
    divisions = ["Atlantic", "Central", "Southeast", "Northwest", "Pacific", "Southwest"]
    div_teams = {division: [] for division in divisions}

    for division in divisions:
        teams = session.query(Teams).filter(Teams.division == division).order_by(Teams.wins.desc()).all()
        div_teams[division] = teams

    for division in divisions:
        print(f"       {division} Division")
        for team in div_teams[division]:
            print(f"{team.name:<25}{team.wins} - {team.losses}")


def update_record():
    while True:
        result = input("Did the team win or lose? (type 'back' to go back to search) ")

        if result == 'back':
            return False

        if result.lower() == 'win':
            team = input("Who won? ")
            column = 'wins'
        elif result.lower() == 'lose':
            team = input("Who lost? ")
            column = 'losses'
        else:
            print("Invalid action. Please enter 'win' or 'lose'.")
            continue

        selected_team = session.query(Teams).filter(Teams.name.ilike(f'%{team}%')).first()

        if not selected_team:
            print(f"No team named '{team}' was found.")
        else:
            if column == 'wins':
                selected_team.wins += 1
            else:
                selected_team.losses += 1

            print(f"The {selected_team.name} are now {selected_team.wins} - {selected_team.losses}.")

            session.commit()
            return True
