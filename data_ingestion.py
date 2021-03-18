import sqlite3

conn = sqlite3.connect('./StudentDB.sqlite')
mycursor = conn.cursor()

#import data from csv
with open(./students.csv) as inputfile:
    columns = inputfile.readline()
    rows = inputfile.readline()