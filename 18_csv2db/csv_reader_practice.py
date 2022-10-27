import csv

with open("students.csv", newline='') as csvfile: # open() as __ SAME NAME BELOW
    students_reader = csv.reader(csvfile, delimiter=",") # csv.reader(__, )
    for row in students_reader:
        print('|'.join(row))