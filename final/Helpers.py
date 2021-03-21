#Andy Anguiano

import sqlite3
import pandas as pd
from pandas import DataFrame

#connecting to the database
conn = sqlite3.connect('StudentDB.db')
mycursor = conn.cursor()

#preferences when using pandas dataframes
pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)

#getting data from csv and populating table
def dataIngestion():
    with open("students.csv") as inputFile:
        title = 0
        for line in inputFile:
            #first row is titles
            if title == 0:
                title += 1
                continue
            else:
                mycursor.execute('INSERT INTO Student(FirstName,LastName,Address,City,State,ZipCode,MobilePhoneNumber,Major,GPA) VALUES(?,?,?,?,?,?,?,?,?)',line.split(","))
                conn.commit()
                title += 1

#main options for the program
def options():
    while True:
        print("\n")
        print("Options: ")
        print("1. Display all students and their attributes.")
        print("2. Add a new student.")
        print("3. Update a students information.")
        print("4. Delete a Student")
        print("5. Search/Display students by Major, GPA, City, State or Advisor.")
        print("6. Exit Program")
        choice = input("Enter the number of the option you would like to execute: ")
        if choice == "1":
            print("\n")
            displayStudents()
        elif choice == "2":
            print("\n")
            addStudent()
        elif choice == "3":
            print("\n")
            updateStudent()
        elif choice == "4":
            print("\n")
            deleteStudent()
        elif choice == "5":
            print("\n")
            searchStudent()
        elif choice == "6":
            print("\n")
            print("Exiting")
            mycursor.execute('DELETE FROM Student')
            conn.commit()
            break
        else:
            print("\n")
            print("Invalid input. Try Again")
            print("\n")
            continue

#diplays all students information in a pandas dataframe
def displayStudents():
    mycursor.execute('SELECT * FROM Student')
    records = mycursor.fetchall()
    df = DataFrame(records, columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'Address', 'City', 'State', 'ZipCode', 'MobilePhoneNUmber',  'isDeleted'])
    print(df)

#adds a student to the table
def addStudent():
    nFirstName = input("First Name of the Student: ")
    nLastName = input("Last Name of the Student: ")
    #making sure decimals are in place
    while True:
        try:
            nGPA = float(input("GPA of the Student as decimal: "))
            break
        except ValueError:
            print("Try again in form of _.__: ")
    nMajor = input("Major: ")
    nFacultyAdvisor = input("Faculty Advisor: ")
    nAddress = input("Address: ")
    nCity = input("City: ")
    nState = input("State: ")
    #making sure zipcode is correct
    while True:
        try:
            nZipCode = int(input("ZipCode: "))
            break
        except ValueError:
            print("Try again with 5 digits: ")
    #making sure phone number is correct
    while True:
        try:
            nPhoneNumber = input("Mobile Phone Number: ")
            break
        except ValueError:
            print("Try again with only digits: ")
    #fix this
    mycursor.execute('INSERT INTO Student VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', (111,nFirstName,nLastName,nGPA,nMajor,nFacultyAdvisor,nAddress,nCity,nState,nZipCode,nPhoneNumber,0))
    conn.commit()
    print("Student Successfully Added.")

#update a students information
def updateStudent():
    nSID = input("ID of the student you would like to update: ")
    mycursor.excecute('SELECT * FROM Student WHERE StudentID = ?', (nSID))
    output = mycursor.fetchall()
    #checking if input is valid
    if output == []:
        print("Invalid Input. Please Try Again.")
        updateStudent()
    else:
        #updating specific attribute of given student
        print("The following are available to update:")
        print("1. Major")
        print("2. Advisor")
        print("3. Mobile Number")
        choice = input("Which corresponding number would you like to update:")
        if choice == "1":
            nMajor = input("Students New Major: ")
            mycursor.execute('UPDATE Student SET Major = ? WHERE studentID = ?', (nMajor,nSID))
            conn.commit()
            print("Information Successfully Updated")
        elif choice == "2":
            nAdvisor = input("Student New Advisor: ")
            mycursor.execute('UPDATE Student SET FacultyAdvisor = ? WHERE studentID = ?', (nAdvisor,nSID))
            conn.commit()
            print("Information Successfully Updated")
        elif choice == "3":
            while True:
                try:
                    nPhoneNumber = input("Students New Mobile Number: ")
                    break
                except ValueError:
                    print("Try again with only digits: ")
            mycursor.execute('UPDATE Student SET MobilePhoneNumber = ? WHERE studentID = ?', (nPhoneNumber,nSID))
            conn.commit()
            print("Information Successfully Updated")
        else:
            #recursion function if invalid input
            print("Invalid input. Try Again")
            updateStudent()

#delete a student
def deleteStudent():
    nSID = input("ID of the student to delete: ")
    mycursor.execute('SELECT * FROM Student WHERE StudentID = ?', (nSID))
    output = mycursor.fetchall()
    #check if input valid
    if output == []:
        print("Invalid Input. Please Try Again.")
        deleteStudent()
    else:
        mycursor.execute('UPDATE Student SET isDeleted = ? WHERE studentID = ?', (1,nSID))
    conn.commit()
    print("Student Successfully Deleted")

#filter through students
def searchStudent():
    print("Which below would you like to filter the Students by.")
    print("1. Major")
    print("2. GPA")
    print("3. City")
    print("4. State")
    print("5. Faculty Advisor")
    while True:
        choice = input("Which corresponding number would you like to filter by: ")
        if choice == "1":
            #show list of distinct majors
            mycursor.execute('SELECT DISTINCT Major FROM Student')
            output = mycursor.fetchall()
            df = DataFrame(output, columns=['Majors'])
            print(df)
            filterChoice = input("Major you would like to see: ")
            mycursor.execute('SELECT * FROM Student WHERE Major = ?', (filterChoice,))
            output = mycursor.fetchall()
            #check if input valid
            if output == []:
                print("Invalid Input. Please Try Again.")
                searchStudent()
                break
            else:
                df = DataFrame(output, columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'Address','City', 'State', 'ZipCode', 'MobilePhoneNUmber', 'isDeleted'])
                print(df)
                break
        elif choice == "2":
            filterChoice = input("GPA you would like to see: ")
            mycursor.execute('SELECT * FROM Student WHERE GPA = ?', (filterChoice,))
            output = mycursor.fetchall()
            # check if input valid
            if output == []:
                print("Invalid Input. Please Try Again.")
                searchStudent()
                break
            else:
                df = DataFrame(output, columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'Address','City', 'State', 'ZipCode', 'MobilePhoneNUmber', 'isDeleted'])
                print(df)
                break
        elif choice == "3":
            # show list of distinct cities
            mycursor.execute('SELECT DISTINCT City FROM Student')
            output = mycursor.fetchall()
            df = DataFrame(output, columns=['Cities'])
            print(df)
            filterChoice = input("City you would like to see: ")
            mycursor.execute('SELECT * FROM Student WHERE City = ?', (filterChoice,))
            output = mycursor.fetchall()
            # check if input valid
            if output == []:
                print("Invalid Input. Please Try Again.")
                searchStudent()
                break
            else:
                df = DataFrame(output, columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'Address','City', 'State', 'ZipCode', 'MobilePhoneNUmber', 'isDeleted'])
                print(df)
                break
        elif choice == "4":
            # show list of distinct states
            mycursor.execute('SELECT DISTINCT State FROM Student')
            output = mycursor.fetchall()
            df = DataFrame(output, columns=['States'])
            print(df)
            filterChoice = input("State you would like to see: ")
            mycursor.execute('SELECT * FROM Student WHERE State = ?', (filterChoice,))
            output = mycursor.fetchall()
            # check if input valid
            if output == []:
                print("Invalid Input. Please Try Again.")
                searchStudent()
                break
            else:
                df = DataFrame(output, columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'Address','City', 'State', 'ZipCode', 'MobilePhoneNUmber', 'isDeleted'])
                print(df)
                break
        elif choice == "5":
            mycursor.execute('SELECT DISTINCT FacultyAdvisor FROM Student')
            output = mycursor.fetchall()
            df = DataFrame(output, columns=['Advisors'])
            print(df)
            filterChoice = input("Faculty Advisor you would like to see: ")
            mycursor.execute('SELECT * FROM Student WHERE FacultyAdvisor = ?', (filterChoice,))
            output = mycursor.fetchall()
            # check if input valid
            if output == []:
                print("Invalid Input. Please Try Again.")
                searchStudent()
                break
            else:
                df = DataFrame(output, columns=['StudentId', 'FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor', 'Address','City', 'State', 'ZipCode', 'MobilePhoneNUmber', 'isDeleted'])
                print(df)
                break
        else:
            print("Invalid Input. Please Try Again.")
            searchStudent()
            break

