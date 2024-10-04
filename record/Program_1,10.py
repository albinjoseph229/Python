# Initialize an empty list to store student dictionaries
students = []

# Number of students
N = int(input("Enter the number of students: "))

# Input student details
for _ in range(N):
    name = input("Enter student name: ")
    roll_no = input("Enter student roll number: ")
    total_mark = int(input("Enter student total marks: "))
    students.append({'name': name, 'roll_no': roll_no, 'total_mark': total_mark})

# Find the student with the highest total marks
top_student = max(students, key=lambda x: x['total_mark'])

# Print the details of the top student
print("\nStudent with the highest total marks:")
print(f"Name: {top_student['name']}")
print(f"Roll Number: {top_student['roll_no']}")
print(f"Total Marks: {top_student['total_mark']}")