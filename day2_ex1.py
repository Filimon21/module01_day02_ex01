student_name = "Abel"
age = 22
course = "Software Engineering"
completed_assignments = 8
total_assignment = 10

completion = (completed_assignments / total_assignment) * 100
more_than_70 = completion > 70

print("Student:", student_name)
print("Age:", age)
print("Course:", course)
print("Completion:", completion, "%")
print("Completed more than 70%:", more_than_70)