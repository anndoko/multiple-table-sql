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
    # Your code goes here
    pass

# Prints all of the round names a team won (sorted from lowest round id to
# highest round id) and the corresponding scores
# Params: team_name (ie. “Michigan”)
# Returns: nothing
# Note: You must use only one SQL statement in this function.
def print_winning_rounds_for_team(team_name):
    # Your code goes here
    pass

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
    # Your code goes here
    pass

# Update the date for the specified round and the times for each of the games
# in that round
# Params: round_id (ex. 1), date (ie. “03-05-18”), time (ie. “5:30pm”)
# Returns: Success string (detailed in spec)
# Note: All of these games will be updated to the same time.
# You may use multiple SQL statements in this function as well.
def update_schedule_for_round(round_id, date, time):
    # Your code goes here
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