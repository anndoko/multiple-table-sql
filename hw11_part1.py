# 507/206 Homework 11 Part 1
import csv
import sqlite3 as sqlite

#### Part 1 ####
print('\n*********** PART 1 ***********')

# Creates a database called big10.sqlite
def create_tournament_db():
    try:
        conn = sqlite.connect('big10.sqlite')
        cur = conn.cursor()
    except:
        print("Failed. Please try again.")

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

    # Create table: Teams
    statement = '''
        CREATE TABLE 'Teams' (
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'Seed' INTEGER,
            'Name' TEXT,
            'ConfRecord' TEXT
        );
    '''
    try:
        cur.execute(statement)
    except:
        print("Failure. Please try again.")
    conn.commit()

    # Create table: Games
    statement = '''
        CREATE TABLE 'Games' (
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'Winner' INTEGER,
            'Loser' INTEGER,
            'WinnerScore' INTEGER,
            'LoserScore' INTEGER,
            'Round' INTEGER,
            'Time' TEXT
        );
    '''
    try:
        cur.execute(statement)
    except:
        print("Failure. Please try again.")
    conn.commit()

    # Create table: Rounds
    statement = '''
        CREATE TABLE 'Rounds' (
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'Name' TEXT,
            'Date' TEXT
        );
    '''
    try:
        cur.execute(statement)
    except:
        print("Failure. Please try again.")
    conn.commit()
    conn.close()

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
    # read data from CSV (teams.csv)
    with open("teams.csv", 'r') as csv_f:
        csv_data = csv.reader(csv_f)

        # This skips the first row of the CSV file.
        next(csv_data)

        for row in csv_data:
            (Seed, Name, ConfRecord) = row

            insert_statement = '''
                INSERT INTO Teams(Seed, Name, ConfRecord) VALUES (?, ?, ?);
            '''
            # execute and commit
            cur.execute(insert_statement, [Seed, Name, ConfRecord])
            conn.commit()


    # read data from CSV (games.csv)


    # read data from CSV (rounds.csv)
    with open("rounds.csv", 'r') as csv_f:
        csv_data = csv.reader(csv_f)

        # This skips the first row of the CSV file
        next(csv_data)

        for row in csv_data:
            (Name, Date) = row

            insert_statement = '''
                INSERT INTO Rounds(Name, Date) VALUES (?, ?);
            '''
            # execute and commit
            cur.execute(insert_statement, [Name, Date])
            conn.commit()


    # Close connection
    conn.close()

if __name__ == "__main__":
    create_tournament_db()
    print("Created big10 Database")
    populate_tournament_db()
    print("Populated big10 Database")
