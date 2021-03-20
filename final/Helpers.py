import sqlite3
import pandas as pd
from pandas import DataFrame

conn = sqlite3.connect('./StudentDB.db')
mycursor = conn.cursor()


    #mycursor.execute('SELECT * FROM Students')

    #myrecords = mycursor.fetchall()

    #print(myrecords)

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
        choice = input("Enter the number of the option you would like to excecute: ")
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
            break
        else:
            print("\n")
            print("Invalid input. Try Again")
            print("\n")
            continue


def displayStudents():
    print("Made it")
    #mycursor.excecute('SELECT * Major FROM Students')
    #records = mycursor.fetchall())
    #df = pd.DataFrame(records)
    #print(df)

def addStudent():
    nFirstName = input("First Name of the Student: ")
    nLastName = input("Last Name of the Student: ")
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
    while True:
        try:
            nZipCode = int(input("ZipCode: "))
            break
        except ValueError:
            print("Try again with 5 digits: ")
    while True:
        try:
            nPhoneNumber = int(input("Mobile Phone Number: "))
            break
        except ValueError:
            print("Try again with only digits: ")

    #mycursor.excecute('INSERT INTO Students VALUES (?,?,?,?,?,?,?,?,?,?,?)', (nFirstName,nLastName,nGPA,nMajor,nFacultyAdvisor,nAddress,nCity,nState,nZipCode,nPhoneNumber,0))
    print("Student Sucsesfully Added.")

def updateStudent():
    nSID = input("ID of the student you would like to update: ")
    print("The following are available to update:")
    print("1. Major")
    print("2. Advisor")
    print("3. Mobile Number")
    choice = input("Which corresponding number would you like to update:")
    if choice == "1":
        nMajor = input("Students New Major: ")
        #update dataset
        print("Information Succesfully Updated")
    elif choice == "2":
        nAdvisor = input("Student New Advisor: ")
        # update dataset
        print("Information Succesfully Updated")
    elif choice == "3":
        while True:
            try:
                nPhoneNumber = int(input("Students New Mobile Number: "))
                break
            except ValueError:
                print("Try again with only digits: ")
        #update dataset
        print("Information Succesfully Updated")
    else:
        print("Invalid input. Try Again")
        updateStudent()

def deleteStudent():
    nSID = input("ID of the student to delete: ")
    # mycursor.excecute('SELECT * FROM Students WHERE StudentID = ?', (nSID))
    # output = mycursor.fetchall()
    # if output == []:
        # print("Invalid Input. Please Try Again.")
        #deleteStudent()
    # else:
        #set Isdelete to 1
        # break
    print("Student Succesfully Deleted")

def searchStudent():
    print("Which below would you like to filter the Students by.")
    print("1. Major")
    print("2. GPA")
    print("3. City")
    print("4. State")
    print("5. Advisor")
    while True:
        choice = input("Which corresponding number would you like to filter by: ")
        if choice == "1":
            #mycursor.excecute('SELECT DISTINCT Major FROM Students')
            #print(mycursor.fetchall())
            filterChoice = input("Major would you like to see: ")
            #mycursor.excecute('SELECT * FROM Students WHERE Major = ?', (filterChoice))
            #output = mycursor.fetchall()
            #if output == []:
                #print("Invalid Input. Please Try Again.")
                #searchStudent()
           # else:
                #print(output)
                #break

