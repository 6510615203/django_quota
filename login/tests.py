from django.test import TestCase
from django.contrib.auth.models import User
from .models import Student, Subject, Enrollment

class StudentTestCase(TestCase):
    def setUp(self):
        # creat user account
        user1 = User.objects.create(username="6510615096", password="usertest1")
        user2 = User.objects.create(username="6510615203", password="usertest2")
        # creat instance student
        student1 = Student.objects.create(user=user1, name="Nutpupicha", surname="Arungornpasuruk", year="3", student_id="6510615096")
        student2 = Student.objects.create(user=user2, name="Ponthipa", surname="Teerapravet", year="3", student_id="6510615203")
        self.student = Student.objects.create(student1,student2)

    def test_student_creation(self):
        self.assertEqual(self.student.name, "Nutpupicha","Ponthipa")
        self.assertEqual(self.student.surname, "Arungornpasuruk","Teerapravet")
        self.assertEqual(self.student.year, "3","3")
        self.assertEqual(self.student.student_id, "6510615096","6510615203")
        #self.assertEqual(str(self.student), "6510615096 : Nutpupicha Arungornpasuruk", "6510615203 : Ponthipa Teerapravet")

class SubjectTestCase(TestCase):
    def setUp(self):
        # creat subject
        self.subject = Subject.objects.create(code="CN101", name="Introduction to Computer Programming", semester=1, year=2567, seats=50, status="AVAILABLE")

    def test_subject_creation(self):
        self.assertEqual(self.subject.code, "CN101")
        self.assertEqual(self.subject.name, "Introduction to Computer Programming")
        self.assertEqual(self.subject.semester, 1)
        self.assertEqual(self.subject.year, 2567)
        self.assertEqual(self.subject.seats, 50)
        self.assertEqual(self.subject.status, "AVAILABLE")
        #self.assertEqual(str(self.subject), "CN101 Introduction to Computer Programming (1/2567)")

class EnrollmentTestCase(TestCase):
    def setUp(self):
        # creat user, student, subject
        # creat user account
        user1 = User.objects.create(username="6510615096", password="usertest1")
        user2 = User.objects.create(username="6510615203", password="usertest2")
        # creat instance student
        student1 = Student.objects.create(user=user1, name="Nutpupicha", surname="Arungornpasuruk", year="3", student_id="6510615096")
        student2 = Student.objects.create(user=user2, name="Ponthipa", surname="Teerapravet", year="3", student_id="6510615203")
        self.student = Student.objects.create(student1,student2)
        # creat subject
        self.subject = Subject.objects.create(code="CN101", name="Introduction to Computer Programming", semester=1, year=2567, seats=50, status="AVAILABLE")

        # creat enrollment instance
        self.enrollment = Enrollment.objects.create(student=self.student, subject=self.subject)

    def test_enrollment__creation(self):
        self.assertEqual(self.enrollment.student, self.student)
        self.assertEqual(self.enrollment.subject, self.subject)
        #self.assertEqual(str(self.enrollment), f"{self.student} ขอโควต้าวิชา {self.subject}")