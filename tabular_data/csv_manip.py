import csv

with open('Group1 Student.csv', mode='w') as csv_file:
    fieldnames = ['Group', 'student_name', 'department', 'Age']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Group':'1', 'student_name': 'Sara', 'department': 'CPS2', 'Age': '27'})
    writer.writerow({'Group':'1', 'student_name': 'Randika', 'department': 'CPS2', 'Age': '27'})
    writer.writerow({'Group':'1', 'student_name': 'Siva', 'department': 'CPS2', 'Age': '25'})
    writer.writerow({'Group':'1', 'student_name': 'Mez', 'department': 'CPS2', 'Age': '27'})
    writer.writerow({'Group':'1', 'student_name': 'Ignas', 'department': 'CPS2', 'Age': '26'})
    writer.writerow({'Group':'1', 'student_name': 'Abduwahab', 'department': 'CPS2', 'Age': '27'})