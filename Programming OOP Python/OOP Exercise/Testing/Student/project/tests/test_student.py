# from Testing.Student.project.project.student import Student
from project.student import Student
import unittest

class StudentTest(unittest.TestCase):
    def setUp(self):
        self.student = Student('A')

    def test_init(self):
        self.assertEqual(self.student.name, 'A')
        self.assertEqual(self.student.courses, {})

    def test_adding_course_if_not_in_dict(self):
        res = self.student.enroll('math',[3,3],'Z')
        self.assertEqual(res, 'Course has been added.')
        self.assertEqual(self.student.courses, {'math': []})

    def test_adding_course_if_in_dict(self):
        self.student.courses = {'math':[3,3], 'BEL':[6,6]}
        res = self.student.enroll('math',[4], 'Z')
        self.assertEqual(res, 'Course already added. Notes have been updated.')

    def test_adding_course_and_notes_if_in_dictY(self):
        self.student.courses = {}
        res = self.student.enroll('math', [4], 'Y')
        self.assertEqual(res, 'Course and course notes have been added.')

    def test_adding_course_and_notes_if_in_dict(self):
        self.student.courses = {}
        res = self.student.enroll('math', [4], '')
        self.assertEqual(res, 'Course and course notes have been added.')

    def test_add_notes_if_course_in_dict(self):
        self.student.courses = {'math': [3, 3], 'BEL': [6, 6]}
        res = self.student.add_notes('math', 4)
        self.assertEqual(res, 'Notes have been updated')
        self.assertEqual(self.student.courses, {'math': [3, 3,4], 'BEL': [6, 6]})

    def test_raise_exception_adding_notes_if_course_not_in_dict(self):
        with self.assertRaises(Exception) as exc:
            self.student.add_notes('music', 3)
        self.assertEqual(str(exc.exception), 'Cannot add notes. Course not found.')

    def test_leave_course_if_in_dict(self):
        self.student.courses = {'math': [3, 3], 'BEL': [6, 6]}
        res = self.student.leave_course('math')
        self.assertEqual(res, 'Course has been removed')

    def test_leave_course_if_not_in_dict(self):
        with self.assertRaises(Exception) as exc:
            self.student.leave_course('music')
        self.assertEqual(str(exc.exception), 'Cannot remove course. Course not found.')


if __name__ == '__main__':
    unittest.main()