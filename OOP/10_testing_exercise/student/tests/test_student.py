from unittest import TestCase, main
from project.student import Student


class StudentTests(TestCase):

    def setUp(self):
        self.student = Student('Test1')
        self.student_with_courses = Student('Tests2', {'math': ['algebra']})

    def test_correct_init(self):
        self.assertEqual('Test1', self.student.name)
        self.assertEqual('Tests2', self.student_with_courses.name)

        self.assertEqual({}, self.student.courses)
        self.assertEqual({'math': ['algebra']}, self.student_with_courses.courses)

    def test_enroll_in_the_same_course_append_new_courses(self):
        result = self.student_with_courses.enroll('math', ['geometry', 'x + y = z'])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({'math': ['algebra', 'geometry', 'x + y = z']}, self.student_with_courses.courses)

    def test_enroll_without_third_param_add_notes_to_the_course(self):
        result = self.student.enroll('math', ['algebra'])

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'math': ['algebra']}, self.student.courses)

    def test_enroll_with_third_param_Y_add_notes_to_the_course(self):
        result = self.student.enroll('math', ['algebra'], 'Y')

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'math': ['algebra']}, self.student.courses)

    def test_enroll_with_third_param_N_add_notes_to_the_course(self):
        result = self.student.enroll('math', ['algebra'], 'n')

        self.assertEqual("Course has been added.", result)
        self.assertEqual({'math': []}, self.student.courses)

    def test_add_notes_to_existing_course_expect_success(self):
        result = self.student_with_courses.add_notes('math', 'geometry')

        self.assertEqual("Notes have been updated", result)
        self.assertEqual({'math': ['algebra', 'geometry']}, self.student_with_courses.courses)

    def test_add_notes_to_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('math', 'algebra')

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_to_existing_course_expect_success(self):
        result = self.student_with_courses.leave_course('math')

        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student_with_courses.courses)

    def test_leave_course_to_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('math')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == '__main__':
    main()