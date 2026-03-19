# Extension Task — Write Back to the File
# Read scores.csv, add a new student, write the updated list back.

# Read all results into memory
results = []
file = open('scores.csv', 'r')
for line in file:
    line = line.strip()
    fields = line.split(',')
    results.append(fields)
file.close()

# Add a new student
new_name  = input('Enter student name: ')
new_score = input('Enter their score: ')
results.append([new_name, new_score])

# Your code below — write the updated list back to scores.csv
# Each line should be:  name,score
with open('scores.csv', 'w') as file:
    for name, score in results:
        file.write(f'{name},{score}\n')