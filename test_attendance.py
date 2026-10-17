
import unittest


# Sample attendance function for testing
def mark_attendance(student_id, present):
    if student_id and present:
        return "Attendance Marked"
    return "Attendance Not Marked"


# Automated attendance test cases
class TestAttendance(unittest.TestCase):

    def test_mark_present(self):
        result = mark_attendance("STU101", True)
        self.assertEqual(result, "Attendance Marked")

    def test_empty_student_id(self):
        result = mark_attendance("", True)
        self.assertEqual(result, "Attendance Not Marked")


if __name__ == "__main__":
    unittest.main()
