# Task 2 — Filter by City
# Read students.csv and display only students from a given city.

students = []
file = open('students.csv', 'r')
for line in file:
    line = line.strip()
    fields = line.split(',')
    students.append(fields)
file.close()

city_to_find = input('Enter a city: ')

# Your code below — find all students from that city
for student in students:
    name = student[0]
    city = student[2]
    if city == city_to_find:
        print(f"{name} is from {city_to_find}.")
        
