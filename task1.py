# Task 1 — Display All Students
# Read students.csv and display each student's details.

students = []
file = open('students.csv', 'r')
for line in file:
    line = line.strip()
    fields = line.split(',')
    students.append(fields)
file.close()

# Your code below — use the students list
for student in students:
    print(f"{student[0]} is {student[1]} years old and lives in {student[2]}.")