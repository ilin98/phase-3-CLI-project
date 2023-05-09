import sqlite3

conn = sqlite3.connect('nba_db.db')
c = conn.cursor()

def search():
    search = input('What would you like to search? ')
    return search

def get_lineup():
    while True:
        team = input('Which team? (type "back" to go back to search) ')

        if team == 'back':
            return False

        c.execute("SELECT id FROM Teams WHERE name LIKE?", ('%' + team + '%',))
        team_id = c.fetchone()

        if team_id is None:
            print(f"No team named '{team}' was found.")

        else:
            c.execute("SELECT name, position FROM Players WHERE team_id=?", team_id)
            players = c.fetchall()

            c.execute("SELECT name FROM Teams WHERE id=?", team_id)
            team_name = c.fetchone()[0]

            print(f"The following players are on the {team_name}:")
            for player in players:
                print(f"{player[0]}, {player[1]}")
            return True


# def get_all_position():
#     position = input('Which position? ')
#     return position

# def get_standings():
#     standings = ''
#     return standings

# def print_info(name, age, color):
#     print(f'Your name is {name}.')
#     print(f'You are {age} years old.')
#     print(f'Your favorite color is {color}.')
