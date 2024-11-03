from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from login.models import Student, Subject, Enrollment

class ViewsTestCase(TestCase):

    def setUp(self):
        self.admin_user = User.objects.create_user(username="admin", password="adminpass331", is_superuser=True)
        self.student_user = User.objects.create_user(username="6510681000", password="passuser01")
        self.student = Student.objects.create(user=self.student_user, name="Somchai", surname="Rakthai", year=2, student_id=6510681000)
        self.subject = Subject.objects.create(code="CN331", name="Software Engineering", semester=1, year=2024, seats=30, status="AVAILABLE")
        self.client = Client()
    
    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html") 

    def test_admin_login_index_view(self):
        response = self.client.post(reverse("index"), {"username": "admin", "password": "adminpass331"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, "/admin/login/?next=/admin/")

    def test_student_login_index_view(self):
        response = self.client.post(reverse("index"), {"username": "6510681000", "password": "passuser01"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "quota")

    def test_invalid_login_index_view_post(self):
        response = self.client.post(reverse("index"), {"username": "6510681000", "password": "incorrestpass"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "Invalid credentials.")

    def test_quota_view(self):
        self.client.login(username="6510681000", password="passuser01")
        response = self.client.get(reverse("quota"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quota.html")
        self.assertIn("subject_list", response.context)
    
    def test_search_subject_in_quota_view(self):
        self.client.login(username="6510681000", password="passuser01")
        response = self.client.post(reverse("quota"), {"q": "CN331"})
        self.assertEqual(response.status_code, 200)
        subject_list = response.context["subject_list"]
        self.assertIn(self.subject, subject_list)

    def test_enroll_subject_in_quota_view(self):
        self.client.login(username="6510681000", password="passuser01")
        response = self.client.post(reverse("quota"), {"code": "CN331"})
        self.assertEqual(response.status_code, 200)
        enroll_subject = Enrollment.objects.filter(student=self.student, subject=self.subject).exists()
        self.assertTrue(enroll_subject)
        self.subject.refresh_from_db()
        self.assertEqual(self.subject.status, "REGISTERED")
        self.assertEqual(self.subject.seats, 29)

    def test_search_view(self):
        self.client.login(username="6510681000", password="passuser01")
        response = self.client.get(reverse("search"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "search.html")
        self.assertIn("subject_list", response.context)
    
    def test_search_subject_in_search_view(self):
        self.client.login(username="6510681000", password="passuser01")
        response = self.client.post(reverse("search"), {"q": "CN331"})
        self.assertEqual(response.status_code, 200)
        subject_list = response.context["subject_list"]
        self.assertIn(self.subject, subject_list)

    def test_result_view(self):
        self.client.login(username="6510681000", password="passuser01")
        response = self.client.get(reverse("result"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "result.html")
        self.assertIn("subject_list", response.context)

    def test_withdraw_in_result_view(self):
        self.client.login(username="6510681000", password="passuser01")
        Enrollment.objects.create(student=self.student, subject=self.subject)
        self.subject.status = "REGISTERED"
        self.subject.seats = 29
        self.subject.save()
        response = self.client.post(reverse("result"), {"code": "CN331"})
        self.assertEqual(response.status_code, 200)
        enroll_subject = Enrollment.objects.filter(student=self.student, subject=self.subject).exists()
        self.assertFalse(enroll_subject)
        self.subject.refresh_from_db()
        self.assertEqual(self.subject.status, "AVAILABLE")
        self.assertEqual(self.subject.seats, 30)

    