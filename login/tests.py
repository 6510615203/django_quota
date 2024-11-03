from django.test import TestCase
from django.contrib.auth.models import User
from .models import Student, Subject, Enrollment


class EnrollmentTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="6510681000", password="passuser01")
        self.student = Student.objects.create(user=self.user, name="Somchai", surname="Rakthai", year=2, student_id=6510681000)
        self.subject = Subject.objects.create(code="CN331", name="Software Engineering", semester=1, year=2024, seats=30, status="AVAILABLE")

    def test_student(self):
        self.assertEqual(self.student.name, "Somchai")
        self.assertEqual(self.student.surname, "Rakthai")
        self.assertEqual(self.student.year, 2)
        self.assertEqual(self.student.student_id, 6510681000)
        self.assertEqual(str(self.student), "6510681000 : Somchai Rakthai")

    def test_subject(self):
        self.assertEqual(self.subject.code, "CN331")
        self.assertEqual(self.subject.name, "Software Engineering")
        self.assertEqual(self.subject.semester, 1)
        self.assertEqual(self.subject.year, 2024)
        self.assertEqual(self.subject.seats, 30)
        self.assertEqual(self.subject.status, "AVAILABLE")
        self.assertEqual(str(self.subject), "CN331 Software Engineering (1/2024)")

    def test_enrollment(self):
        enrollment = Enrollment.objects.create(student=self.student, subject=self.subject)
        self.assertEqual(enrollment.student, self.student)
        self.assertEqual(enrollment.subject, self.subject)
        self.assertEqual(str(enrollment), "6510681000 : Somchai Rakthai ขอโควต้าวิชา CN331 Software Engineering (1/2024)")
