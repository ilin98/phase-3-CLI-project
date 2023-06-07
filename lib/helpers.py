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


def get_all_position():
    while True:
        position = input('Which position? (type "back" to go back to search) ')

        if position == 'back':
            return False

        c.execute("""
            SELECT Players.name, Teams.name
            FROM Players
            JOIN Teams ON Players.team_id = Teams.id
            WHERE Players.position LIKE ?
        """, ('%' + position + '%',))
        players = c.fetchall()

        if not players:
            print(f"No position named '{position}' was found.\nChoose one of the following: PG, SG, SF, PF, C.")

        else:
            print(f"The following players play {position}:")
            for player in players:
                print(f"{player[0]} ({player[1]})")
            return True


def get_standings():
    divisions = ["Atlantic", "Central", "Southeast", "Northwest", "Pacific", "Southwest"]
    div_teams = {}

    for division in divisions:
        c.execute('SELECT name, wins, losses FROM Teams WHERE division=?', (division,))
        div_teams[division] = c.fetchall()

    atlantic = sorted(div_teams["Atlantic"], key=lambda x: x[1], reverse=True)
    central = sorted(div_teams["Central"], key=lambda x: x[1], reverse=True)
    southeast = sorted(div_teams["Southeast"], key=lambda x: x[1], reverse=True)
    northwest = sorted(div_teams["Northwest"], key=lambda x: x[1], reverse=True)
    pacific = sorted(div_teams["Pacific"], key=lambda x: x[1], reverse=True)
    southwest = sorted(div_teams["Southwest"], key=lambda x: x[1], reverse=True)

    print("       Atlantic Division")
    for team in atlantic:
        print(f"{team[0]:<25}{team[1]:>2} - {team[2]:<2}")
    print("       Central Division")
    for team in central:
        print(f"{team[0]:<25}{team[1]:>2} - {team[2]:<2}")
    print("       Southeast Division")
    for team in southeast:
        print(f"{team[0]:<25}{team[1]:>2} - {team[2]:<2}")
    print("       Northwest Division")
    for team in northwest:
        print(f"{team[0]:<25}{team[1]:>2} - {team[2]:<2}")
    print("       Pacific Division")
    for team in pacific:
        print(f"{team[0]:<25}{team[1]:>2} - {team[2]:<2}")
    print("       Southwest Division")
    for team in southwest:
        print(f"{team[0]:<25}{team[1]:>2} - {team[2]:<2}")

def add_win():
    while True:
        team = input('Who won? (type "back" to go back to search) ')

        if team == 'back':
            return False

        c.execute("SELECT name, wins, losses FROM Teams WHERE name LIKE ?", ('%' + team + '%',))
        selected_team = c.fetchone()

        if not selected_team:
            print(f"No team named '{team}' was found.")
        else:
            team_name, wins, losses = selected_team

            c.execute("UPDATE Teams SET wins = ? WHERE name = ?", (wins + 1, team_name))
            conn.commit()

            print(f"The {team_name} are now {wins + 1} - {losses}.")
            return True
