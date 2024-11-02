from django.test import TestCase
from .models import Student, Subject, Enrollment

class StudentTestCase(TestCase):
    def setUp(self):
        # creat student account
        student1 = Student.objects.create(user="6510615096", name="Nutpupicha", surname="Arungornpasuruk", year="3", student_id="6510615096")
        student2 = Student.objects.create(user="6510615203", name="Ponthipa", surname="Teerapravet", year="3", student_id="6510615203")

        self.student = Student.objects.create(student1,student2)

    def test_student_creation(self):
        self.assertEqual(self.student.user, "6510615096","6510615203")
        self.assertEqual(self.student.name, "Nutpupicha","Ponthipa")
        self.assertEqual(self.student.surname, "Arungornpasuruk","Teerapravet")
        self.assertEqual(self.student.year, "3","3")
        self.assertEqual(self.student.student_id, "6510615096","6510615203")

class SubjectTestCase(TestCase):
    def setUp(self):
        # creat subject
        self.subject = Subject.objects.create(code="CN101", name="Introduction to Computer Programming", semester="1", year="2567", seats=50)

    def test_subject_creation(self):
        self.assertEqual(self.subject.code, "CN101")
        self.assertEqual(self.subject.name, "Introduction to Computer Programming")
        self.assertEqual(self.subject.semester, "1")
        self.assertEqual(self.subject.year, "2567")
        self.assertEqual(self.subject.seats, 50)