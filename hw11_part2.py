# 507/206 Homework 11 Part 2
import sqlite3 as sqlite

#### Part 2 ####
print('\n*********** PART 2 ***********')

# Params: game_id (ie. 1)
# Returns: A string formatted as follows with the game’s information:
# {Round Name}: ({Winner Seed}) {Winner} defeated ({Loser Seed}) {Loser}
# {Winner Score}-{Loser Score}
# Note: You must use only one SQL statement in this function.
def get_info_for_game(game_id):
    # connect db
    conn = sqlite.connect("big10.sqlite")
    cur = conn.cursor()

    # form the statement
    statement = '''
        SELECT r.Name, wt.Seed, wt.Name, g.WinnerScore, lt.Seed, lt.Name, g.LoserScore
        FROM Rounds AS r
            JOIN Games AS g ON r.Id = g.Round
            JOIN Teams AS wt ON g.Winner = wt.Id
            JOIN Teams AS lt ON g.Loser = lt.Id
        WHERE r.Id = {}
    '''.format(game_id)

    # excute the statement
    output = ""
    rows = cur.execute(statement).fetchall()
    for row in rows:
        (RoundName, WinnerSeed, Winner, WinnerScore, LoserSeed, Loser, LoserScore) = row
        output += "\n{}: ({}) {} defeated ({}) {}\n{}-{}\n".format(RoundName, WinnerSeed, Winner, LoserSeed, Loser, WinnerScore, LoserScore)
    conn.commit()
    return output

# Prints all of the round names a team won (sorted from lowest round id to
# highest round id) and the corresponding scores
# Params: team_name (ie. “Michigan”)
# Returns: nothing
# Note: You must use only one SQL statement in this function.
def print_winning_rounds_for_team(team_name):
    # connect db
    conn = sqlite.connect("big10.sqlite")
    cur = conn.cursor()

    # form the statement
    statement = '''
        SELECT wt.Name, r.Name, g.WinnerScore, g.LoserScore
        FROM Games AS g
        	JOIN Rounds AS r ON g.Round = r.Id
        	JOIN Teams AS wt ON g.Winner = wt.Id
        	JOIN Teams AS it ON g.Loser = it.Id
        WHERE wt.Name = "{}"
    '''.format(team_name)

    # excute the statement
    output = ""
    rows = cur.execute(statement).fetchall()
    for row in rows:
        (TeamName, RoundName, WinnerScore, LoserScore) = row
        output += "\n{} Won:\n{}: {}-{}\n".format(TeamName, RoundName, WinnerScore, LoserScore)
    print(output)
    conn.commit()

# Update the database to include the following Championship game information:
#   Round Name: “Championship”
#   Round Date: “03-04-18”
#   Winner: “Michigan”
#   Loser: “Purdue”
#   WinnerScore: 75
#   LoserScore: 66
#   Time: “4:30pm”
# Params: None
# Returns: Success string (detailed in spec)
# Note: You will need to update the ‘Games’ and ‘Rounds’ tables with the above
# data.  You are permitted to use multiple SQL statements in this function.
def add_championship_info():
    pass

# Update the date for the specified round and the times for each of the games
# in that round
# Params: round_id (ex. 1), date (ie. “03-05-18”), time (ie. “5:30pm”)
# Returns: Success string (detailed in spec)
# Note: All of these games will be updated to the same time.
# You may use multiple SQL statements in this function as well.
def update_schedule_for_round(round_id, date, time):
    pass

if __name__ == "__main__":
    game_info = get_info_for_game(1)
    print(game_info)
    print("-"*15)

    print_winning_rounds_for_team("Purdue")
    print("-"*15)

    status = add_championship_info()
    print(status)
    print("-"*15)

    status2 = update_schedule_for_round(5,'03-05-18','12:00pm')
    print(status2)
    print("-"*15)
