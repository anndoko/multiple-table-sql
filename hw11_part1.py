# 507/206 Homework 11 Part 1
import csv
import sqlite3 as sqlite

#### Part 1 ####
print('\n*********** PART 1 ***********')

# Creates a database called big10.sqlite
def create_tournament_db():

    conn = sqlite.connect('big10.sqlite')
    cur = conn.cursor()

    # Code below provided for your convenience to clear out the big10 database
    # This is simply to assist in testing your code.  Feel free to comment it
    # out if you would prefer
    statement = '''
        DROP TABLE IF EXISTS 'Teams';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'Games';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'Rounds';
    '''
    cur.execute(statement)
    conn.commit()

    # Your code goes here

    conn.close()
    pass

# Populates big10.sqlite database using csv files
def populate_tournament_db():

    # Connect to big10 database
    conn = sqlite.connect('big10.sqlite')
    cur = conn.cursor()

    # HINTS:
    # Column order in teams.csv file: Seed,Name,ConfRecord
    # Column order in games.csv file: Winner,Loser,WinnerScore,LoserScore,Round,Time
    # Note: You must convert 'Winner' and 'Loser' to corresponding team ids from
    #       'Teams'table
    # Column order in rounds.csv file: Name,Date

    # Your code goes here

    # Close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tournament_db()
    print("Created big10 Database")
    populate_tournament_db()
    print("Populated big10 Database")
