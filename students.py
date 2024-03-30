import csv

# students = []
#
# with open('students.csv') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({
#             'name': row["name"],
#             'house': row['home']
#         })
#
# for student in sorted(students, key=lambda x: x['name']):
#     print(f"{student['name']} is in {student['house']} house.")

# name = input("What is your name? ")
# home = input("What house are you in? ")
#
# with open('students.csv', 'a') as file:
#     writer = csv.DictWriter(file, fieldnames=['name', 'home'])
#     writer.writerow({'name': name, 'home': home})

class Student:
    def __init__(self, name):
        self.name = name

stu = Student('hieu')
print(stu.name)