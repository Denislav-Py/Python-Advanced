# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N.
# On the following N lines, you will be receiving a student's name and grade.
# For each student print all his/her grades and finally his/her average grade,
# formatted to the second decimal point
# The order in which we print the result does not matter.

number_of_students = int(input())
students = {}

for _ in range(number_of_students):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    print(f"{student} -> {' '.join([f'{el:.2f}' for el in grades])} (avg: {avg_grade:.2f})")
