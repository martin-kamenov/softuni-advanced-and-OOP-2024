def softuni_students(*students_data, **courses_data):
    courses = {}
    invalid_students = set()

    for id_course, username in students_data:
        if id_course not in courses_data:
            invalid_students.add(username)
        else:
            course_name = courses_data[id_course]
            courses[username] = course_name

    sorted_students = sorted(courses.items())

    result = []

    for student, course in sorted_students:
        result.append(f'*** A student with the username {student} has successfully finished the course {course}!')

    if invalid_students:
        invalid_message = f'!!! Invalid course students: {", ".join(sorted(invalid_students))}'
        result.append(invalid_message)

    return '\n'.join(result)


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))

print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced and OOP',
))

print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced and OOP',
))
