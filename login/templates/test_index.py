from django.test import TestCase
from django.urls import reverse

class IndexTemplateTest(TestCase):

    def test_index_template_renders_correctly(self):
        # ทำการเรียกหน้า index (หน้า login)
        response = self.client.get(reverse('login/templates/index.html'))  # แทน 'index' ด้วยชื่อ URL ของหน้า login

        # ตรวจสอบว่า response status code เป็น 200 (แสดงผลได้ปกติ)
        self.assertEqual(response.status_code, 200)

        # ตรวจสอบว่า HTML มีข้อความ "ระบบขอโควต้ารายวิชา" และ "เข้าสู่ระบบ"
        self.assertContains(response, "ระบบขอโควต้ารายวิชา")
        self.assertContains(response, "เข้าสู่ระบบ")

    def test_index_template_has_required_fields(self):
        # ตรวจสอบว่าฟอร์ม login มีฟิลด์ Username และ Password
        response = self.client.get(reverse('login/templates/index.html'))

        # ตรวจสอบว่า HTML มีฟิลด์ Username และ Password
        self.assertContains(response, 'name="username"')
        self.assertContains(response, 'name="password"')

    def test_index_template_has_csrf_token(self):
        # ตรวจสอบว่าฟอร์มมี csrf token
        response = self.client.get(reverse('login/templates/index.html'))

        # ตรวจสอบว่า HTML มี {% csrf_token %}
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_index_template_has_css_and_fonts(self):
        # ตรวจสอบว่าเทมเพลตโหลด CSS และฟอนต์ที่ต้องการ
        response = self.client.get(reverse('login/templates/index.html'))

        # ตรวจสอบว่ามีการโหลดไฟล์ CSS loginstyle.css
        self.assertContains(response, "/static/css/loginstyle.css")

        # ตรวจสอบการโหลดฟอนต์จาก Google Fonts
        self.assertContains(response, "https://fonts.googleapis.com/css2?family=Kanit")
        self.assertContains(response, "https://fonts.googleapis.com/css2?family=Mitr")
