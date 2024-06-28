students = {}

for _ in range(int(input())):
    student_name, grade = input().split()

    if student_name not in students:
        students[student_name] = []
    students[student_name].append(float(grade))

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    grades_to_string = " ".join(map(lambda x: f'{x:.2f}', grades))
    print(f'{name} -> {grades_to_string} (avg: {average_grade:.2f})')


# numbers_of_students = int(input())
#
# students_and_grades = {}
#
# for _ in range(numbers_of_students):
#     name, grade = input().split()
#
#     if name not in students_and_grades:
#         students_and_grades[name] = []
#     students_and_grades[name].append(float(grade))
#
# for student_name, grades in students_and_grades.items():
#     average_grade = sum(grades) / len(grades)
#     grades_as_string = [f'{x:.2f}' for x in grades]
#
#     print(f'{student_name} -> {" ".join(grades_as_string)} (avg: {average_grade:.2f})')

