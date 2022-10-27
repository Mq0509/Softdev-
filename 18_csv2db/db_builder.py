# DEM PUMPKINS: Diana Akhmedova, Emily Ortiz, May Qiu
# SoftDev
# K18 -- (Python+SQLite)3: A Mare Widge Made in Hebben
# 2022-10-25
# time spent: 2 hrs

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

c.execute("DROP TABLE if exists students")
c.execute("CREATE TABLE students(name TEXT, age INTEGER, id INTEGER)")

with open("students.csv", newline='') as csvfile:
  students_reader = csv.reader(csvfile, delimiter=",")
  for row in students_reader:
    name = row[0]
    age = row[1]
    id = row[2]
    command = f"INSERT into students VALUES('{name}', '{age}', '{id}')"
    c.execute(command)

c.execute("DROP TABLE if exists courses")
c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)")

with open("courses.csv", newline='') as csvfile:
  courses_reader = csv.reader(csvfile, delimiter=",")
  for row in courses_reader:
    code = row[0]
    mark = row[1]
    id = row[2]
    command = f"INSERT into courses VALUES('{code}', '{mark}', '{id}')"
    c.execute(command)

db.commit() #save changes

print("about to print students database")
ex = c.execute("SELECT * FROM students")
fetch = ex.fetchall()
print(fetch)

print("\nabout to print courses database")
ex = c.execute("SELECT * from courses")
fetch = ex.fetchall()
print(fetch)

db.close()  #close database

# drop tables (CHECK OUT LATER)
# allows you to edit a table existing already/checks if it's there already
