from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from login.models import Student, Subject, Enrollment

class ViewTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.student = Student.objects.create(user=self.user, name="Test", surname="User", year=1)
        
        # Create a test subject
        self.subject = Subject.objects.create(code='SUB001', name='Test Subject', seats=10, status='AVAILABLE')

    def test_index_view_post_valid_credentials(self):
        response = self.client.post(reverse('index'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, reverse('quota'))

    def test_index_view_post_invalid_credentials(self):
        response = self.client.post(reverse('index'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, "Invalid credentials.")

    def test_quota_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('quota'))
        self.assertTemplateUsed(response, 'quota.html')
        self.assertContains(response, 'Test Subject')

    def test_quota_view_post_enrollment(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('quota'), {'code': 'SUB001'})
        self.assertRedirects(response, reverse('quota'))
        enrollment = Enrollment.objects.get(student=self.student, subject=self.subject)
        self.assertIsNotNone(enrollment)
        self.assertEqual(self.subject.seats, 9)  # Assuming one seat is taken

    def test_search_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('search'))
        self.assertTemplateUsed(response, 'search.html')

    def test_search_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('search'), {'q': 'SUB001'})
        self.assertTemplateUsed(response, 'search.html')
        self.assertContains(response, 'Test Subject')

    def test_result_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('result'))
        self.assertTemplateUsed(response, 'result.html')

    def test_result_view_post_unenrollment(self):
        self.client.login(username='testuser', password='testpassword')
        # First, enroll the student in the subject
        Enrollment.objects.create(student=self.student, subject=self.subject)
        self.subject.seats -= 1
        self.subject.status = 'REGISTERED'
        self.subject.save()

        # Then, post to unenroll
        response = self.client.post(reverse('result'), {'code': 'SUB001'})
        self.assertRedirects(response, reverse('result'))

        # Check if enrollment was removed and seats increased
        enrollment = Enrollment.objects.filter(student=self.student, subject=self.subject).first()
        self.assertIsNone(enrollment)
        self.assertEqual(self.subject.seats, 10)  # One seat should be freed
