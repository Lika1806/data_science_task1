passing_grade = 75
additional_tutoring_grade = 85
student_grades = {
    "Alice": 88,
    "Bob": 76,
    "Charlie": 90,
    "Diana": 85,
    "Evan": 92,
    "Fiona": 79,
    "George": 95
}

grades = list(student_grades.values())
max_grade = max(grades)
min_grade = min(grades)
failed = []
passed=[]
first_students = []
last_students = []
additional_tutoring = []
grade_sum=0
for student, grade in student_grades.items():
    grade_sum+=grade
    #finding student(s) with the highest grade
    if grade == max_grade:
        first_students.append(student)
    #finding student(s) with the lowest grade
    elif grade == min_grade:
        last_students.append(student)
    #finding passed students
    if grade>=passing_grade:
        passed.append(student)
    #finding failed students
    else:
        failed.append(student)
    #finding students that need suggestions
    if grade < additional_tutoring_grade:
        additional_tutoring.append(student)

average_grade = grade_sum / len(student_grades)
#part1
print(f"GRADE SUMMARY")
print(f"the average grade for the class:        {average_grade:.2f}")
print(f"student(s) with the highest grade:      {first_students}")
print(f"student(s) with the lowest grade:       {last_students}")
print(f"GRADE DISTRIBUTION")
print(f"Students that passed:   {passed}")
print(f"Students that failed:   {failed}")
print(f"IMPROVEMENT SUGGESTIONS")
for student in additional_tutoring:
    print(f'- Dear {student}, you\'ve got {student_grades[student]} points in exam, consider attending additional tutoring sessions.')
print(f"HERE ARE ALL STUDENTS AND ALL GRADES")
max_length = max(len(name) for name in student_grades.keys())
for student, grade in student_grades.items():
    print(f"{student.ljust(max_length)}: {'=' * int(grade//5)}")
