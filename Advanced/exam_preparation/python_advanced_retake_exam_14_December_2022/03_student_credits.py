def students_credits(*data):
    achieved_credits = 0
    credits_goal = 240
    student_credits = {}

    def points_converter_to_credits(course_credits, max_points_, achieved_points):
        constant = course_credits / max_points_
        achieved_credit = constant * achieved_points

        return achieved_credit

    for row in data:
        course_name, credits_, max_points, student_points = row.split('-')

        credits_from_course = points_converter_to_credits(int(credits_), int(max_points), int(student_points))
        student_credits[course_name] = credits_from_course
        achieved_credits += credits_from_course

    sorted_student_credits = sorted(student_credits.items(), key=lambda x: -x[1])

    result = []

    if achieved_credits >= credits_goal:
        result.append(f'Diyan gets a diploma with {achieved_credits:.1f} credits.')
    else:
        result.append(f'Diyan needs {(credits_goal - achieved_credits):.1f} credits more for a diploma.')

    for course, curr_credit in sorted_student_credits:
        result.append(f'{course} - {curr_credit:.1f}')

    return '\n'.join(result)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
