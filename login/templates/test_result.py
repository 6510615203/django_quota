from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from login.models import Student, Subject

class ResultTemplateTest(TestCase):

    def setUp(self):
        # สร้างผู้ใช้, นักเรียน, และวิชาทดสอบ
        self.user = User.objects.create_user(username='6510615096', password='usertest1')
        self.student = Student.objects.create(user=self.user, name='Nutpupicha', surname='Arungornpasuruk', year=3)

        # สร้างวิชาทดสอบ
        self.subject1 = Subject.objects.create(code='CN101', name='Introduction to Computer Programming', semester=1, year=2567, seats=50, status='REGISTERED')
        self.subject2 = Subject.objects.create(code='CN102', name='Introduction to Computer Programming Lab', semester=1, year=2567, seats=0, status='AVAILABLE')

    def test_result_template_renders_correctly(self):
        # ล็อกอินด้วยผู้ใช้ทดสอบ
        self.client.login(username='6510615096', password='usertest1')

        # เรียกหน้า result
        response = self.client.get(reverse('login/templates/result.html'))

        # ตรวจสอบว่า response status code เป็น 200
        self.assertEqual(response.status_code, 200)

        # ตรวจสอบว่าข้อมูลของผู้ใช้แสดงอยู่ในหน้า HTML
        self.assertContains(response, "ข้อมูลผู้ขอโควต้า : 65110615096 Nutpupicha Arungornpasuruk ชั้นปีที่ 3")

    def test_result_template_displays_subject_list(self):
        # ล็อกอินด้วยผู้ใช้ทดสอบ
        self.client.login(username='6510615096', password='usertest1')

        # เรียกหน้า result
        response = self.client.get(reverse('login/templates/result.html'))

        # ตรวจสอบว่ามีตารางวิชาปรากฏใน HTML และมีวิชาที่สร้างใน setUp
        self.assertContains(response, "รหัสวิชา")
        self.assertContains(response, "ชื่อวิชา")
        self.assertContains(response, "ภาคการศึกษา")
        self.assertContains(response, "ปีการศึกษา")
        self.assertContains(response, "จำนวนที่นั่ง")
        self.assertContains(response, "สถานะ")
        self.assertContains(response, "ยกเลิกการขอโควต้า")

        # ตรวจสอบรายละเอียดของวิชาในตาราง
        self.assertContains(response, "CN101")
        self.assertContains(response, "Introduction to Computer Programming")
        self.assertContains(response, "REGISTERED")

        self.assertContains(response, "CN102")
        self.assertContains(response, "Introduction to Computer Programming Lab")
        self.assertContains(response, "AVAILABLE")

    def test_result_template_displays_withdraw_button_for_registered_subject(self):
        # ล็อกอินด้วยผู้ใช้ทดสอบ
        self.client.login(username='6510615096', password='usertest1')

        # เรียกหน้า result
        response = self.client.get(reverse('login/templates/result.html'))

        # ตรวจสอบว่ามีปุ่ม withdraw ปรากฏในวิชาที่สถานะเป็น "REGISTERED"
        self.assertContains(response, 'button type="submit" class="btn btn-primary">withdraw</button>')

    def test_result_template_has_css_and_title(self):
        # ล็อกอินด้วยผู้ใช้ทดสอบ
        self.client.login(username='6510615096', password='usertest1')

        # เรียกหน้า result
        response = self.client.get(reverse('login/templates/result.html'))

        # ตรวจสอบว่ามีการโหลด CSS และมี title ของหน้า
        self.assertContains(response, "/static/css/resultstyle.css")
        self.assertContains(response, "<title>ผลการขอโควต้า</title>")
