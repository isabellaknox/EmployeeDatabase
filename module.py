import sqlite3
import csv
from sqlite3 import Error
from tabulate import tabulate
from datetime import datetime

backups = []
# Table Names
tables = {
    1: "associates",
    2: "fun_facts",
    3: "addresses",
    4: "events",
    5: "join_table"
}
# Variable values input for cmd string depending on table number
values = {
    1: "(?,?,?,?)",
    2: "(?,?,?,?)",
    3: "(?,?,?,?,?,?)",
    4: "(?,?,?,?,?)"
}
# Field corrections from user input
inputFields = {
    "id": "corpId",
    "first": "first_name",
    "last": "last_name",
    'hire': "hire_date",
    "title": "title",
    "desc": "desc",
    "street": "street",
    "city": "city",
    "state": "state",
    "zip": "zip",
    "date": "date",
    "time": "time"
}
# User input field options depending on table number
options = {
    1: "Options: 'first', 'last', 'hire', 'id''",
    2: "Options: 'title', 'desc', 'id'",
    3: "Options: 'street', 'city', 'state', 'zip', 'id'",
    4: "Options: 'title', 'desc', 'date', 'time',"
}

# goal: add the input csv file information to the database tables
# param conn: connection to database
# param tableNum: int representing the different tables
def addCSVFile(conn, tableNum):
    cursor = conn.cursor()
    fileName = 'src/data/{}.csv'.format(tables[tableNum])
    with open(fileName, 'r') as info:
        data = csv.reader(info)
        next(data)
        for row in data:
            if(tableNum != 1):
                row.insert(0, None)
            cursor.execute("INSERT INTO {} VALUES {}".format(tables[tableNum], values[tableNum]), row)
    # join_tables(cursor)
    conn.commit()

def join_tables(cursor):
    with open('src/data/join_table.csv', 'r') as info:
        data = csv.reader(info)
        next(data)
        cursor.executemany("INSERT INTO join_table VALUES (?,?)", data)
       
# goal: take the user input and add the information to the database tables
# param conn: connection to database
# param tableNum: int representing the different tables
def takeInput(conn, tableNum):
    cursor = conn.cursor()
    if(tableNum == 1):
        associateInput(cursor)
    elif(tableNum == 2):
        funFactInput(cursor)
    elif(tableNum == 3):
        addressInput(cursor)
    else:
        eventInput(cursor)
    conn.commit()

# goal: helper function to take the user input and add the information to the associates table
# param cursor: a cursor created by the connection to the database
def associateInput(cursor):
    first_name = input("Please input a first name:").strip()
    last_name = input("Please input a last name:").strip()
    corpId = input("Please input a corpId:").strip()
    hire_date = input("Please input a hire date:").strip()
    data = [corpId, first_name, last_name, hire_date]
    if(validateInput(data)):
        cursor.execute('''INSERT INTO associates (corpId, first_name, last_name, hire_date) VALUES(?,?,?,?)''', data)

# goal: helper function to take the user input and add the information to the fun_fact table
# param cursor: a cursor created by the connection to the database
def funFactInput(cursor):
    title = input("Please input a title:").strip()
    desc = input("Please input a description:").strip()
    corpId = input("Please input a corpId:").strip()
    data = [None, title, desc, corpId]
    if(validateInput(data)):
        cursor.execute('''INSERT INTO fun_facts (factId, title, desc, corpId) VALUES(?,?,?,?)''', data)

# goal: helper function to take the user input and add the information to the addresses table
# param cursor: a cursor created by the connection to the database
def addressInput(cursor):
    street = input("Please input a street:").strip()
    city = input("Please input a city:").strip()
    state = input("Please input a state:").strip()
    zipCode = input("Please input a zip code:").strip()
    corpId = input("Please input a corpId:").strip()
    data = [None, street, city, state, zipCode, corpId]
    if(validateInput(data)):
        cursor.execute('''INSERT INTO fun_facts (addressId, street, city, state, zip, corpId) VALUES(?,?,?,?,?,?)''', data)

# goal: helper function to take the user input and add the information to the events table
# param cursor: a cursor created by the connection to the database
def eventInput(cursor):
    title = input("Please input a title:").strip()
    desc = input("Please input a description:").strip()
    date = input("Please input a date:").strip()
    time = input("Please input a time:").strip()
    data = [None, title, desc, date, time]
    if(validateInput(data)):
        cursor.execute('''INSERT INTO fun_facts (eventId, title, desc, date, time) VALUES(?,?,?,?,?)''', data)

# FIX THIS! VALIDATE DATA BASED ON TABLE
def validateInput(data):
    # first = data[0]
    # last = data[1]
    # corpId = data[2]
    # if(not corpId.startswith("a") or len(corpId) != 7 or not corpId[1:].isdigit()):
    #     print("\nInvalid corpId field...please try again")
    #     return False
    # if(not first.isalpha() or not last.isalpha()):
    #     return False
    return True

# goal: updates a specific field in the database tables with user input
# param conn: connection to database
# param tableNum: int representing the different tables
def update(conn, tableNum):
    cursor = conn.cursor()
    print(options[tableNum])
    field = input("""\nWhat is the field you would like to update? \n""")
    updatedField = input("\nWhat would you like to change it to?")
    if(tableNum != 4):
        corpId = input("\nWhat is the corpId of the field you would like to update?")
        string = 'UPDATE {} SET {} = ? WHERE corpId = ?'.format(tables[tableNum], inputFields[field])
        cursor.execute(string, (updatedField, corpId))
    else:
        eventId = input("\nWhat is the eventId of the field you would like to update?")
        string = 'UPDATE {} SET {} = ? WHERE eventId = ?'.format(tables[tableNum], inputFields[field])
        cursor.execute(string, (updatedField, eventId))
    conn.commit()

# goal: deletes a specific field/entire entry in the database tables with user input
# param conn: connection to database
# param tableNum: int representing the different tables  
def delete(conn, ans, tableNum):
    cursor = conn.cursor()
    if(ans == "entry"):
        corpId = input("\nWhat is the corpId of the entry you would like to delete?")
        string = 'DELETE FROM {} WHERE corpId = ?'.format(tables[tableNum])
        cursor.execute(string, (corpId,))
    else:
       print(options[tableNum])
       field = input("""\nWhat is the field you would like to delete?\n""")
       if(tableNum != 4):
           corpId = input("\nWhat is the corpId of the field you would like to delete?")
           string = 'UPDATE {} SET {} = ? WHERE corpId = ?'.format(tables[tableNum], inputFields[field])
           cursor.execute(string, ("", (corpId,)))
       else:
           eventId = input("\nWhat is the eventId of the field you would like to delete?")
           string = 'UPDATE {} SET {} = ? WHERE eventId = ?'.format(tables[tableNum], inputFields[field])
           cursor.execute(string, ("", (eventId,)))
    conn.commit()

# goal: displays the specified database table
# param conn: connection to database
# param tableNum: int representing the different tables
def printTable(conn, tableNum):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM {}".format(tables[tableNum]))
    rows = cursor.fetchall()
    print('\n')
    header = []
    if(tableNum == 1):
        header = ['Badge Id', 'First Name', 'Last Name', 'Hire Date']
    elif(tableNum == 2):
         header = ['Fact Id', 'Title', 'Description', 'Badge Id']
    elif(tableNum == 3):
         header = ['Address Id', 'Street', 'City', 'State', 'Zip Code', 'Badge Id']
    else:
        header = ['Event Id', 'Title', 'Description', 'Date', 'Time']
    print(tabulate(rows, headers=header, tablefmt="presto"))
    

# goal: empties the specified database table
# param conn: connection to database
# param tableNum: int representing the different tables
def emptyDB(conn, tableNum):
    c = conn.cursor()
    c.execute("DELETE FROM {};".format(tables[tableNum]))
    conn.commit()

# goal: create a backup of the database with a time stamp of the current time
# param dbConn: connection to original database
def backup(dbConn):
    try:
        now = datetime.now()
        time = now.strftime("%d-%m-%Y %H.%M.%S")
        fileName = 'src/db/db_backup_{}.db'.format(time)
        backups.append(fileName)
        conn = sqlite3.connect(fileName)
        c = conn.cursor()
        for cmd in dbConn.iterdump():
            c.execute(cmd)
        conn.close() 
    except Error as e:
        print(e)
        
# goal: restores the original database to the specified backup verson
# param dbConn: connection to original database
# param tableNum: int representing the different tables
def restore(dbConn):
    dbCursor = dbConn.cursor()
    print("Here is the list of backups:")
    for x in range(len(backups)):
        print('\n{}. {}'.format(x, backups[x]))
    ans = input("\nWhich backup # would you like to restore? ").strip()
    try:
        fileName = backups[int(ans)]
        conn = sqlite3.connect(fileName)
        for table in tables:
            dbCursor.execute("DROP TABLE IF EXISTS {}".format(tables[table]))
        for cmd in conn.iterdump():
            dbCursor.execute(cmd)
        conn.close()
    except Error as e:
        print(e)
        
def build_query(conn):
    pass
            
  
