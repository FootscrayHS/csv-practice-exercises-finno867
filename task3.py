# Task 3 — Read a Different File and Use a Provided Function
# Read scores.csv and display each student's name, score, and grade.

# This function has been provided for you — do not change it
def get_grade(score):
    score = int(score)
    if score >= 80:
        return 'Distinction'
    elif score >= 60:
        return 'Credit'
    elif score >= 40:
        return 'Pass'
    else:
        return 'Fail'


results = []
file = open('scores.csv', 'r')
for line in file:
    line = line.strip()
    fields = line.split(',')
    results.append(fields)
file.close()

# Your code below — loop through results and display each student's grade
# Use get_grade(score) to get the grade string — e.g. get_grade(results[0][1])
for result in results:
    name = result[0]
    score = result[1]
    grade = get_grade(score)
    print(f'{name:<7} {score:<2}%  {grade}')