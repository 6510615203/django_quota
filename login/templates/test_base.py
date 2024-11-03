from django.test import TestCase
from django.urls import reverse
from django.template.loader import render_to_string

class BaseTemplateTest(TestCase):

    def test_base_template_renders_correctly(self):
        # ทำการเรียกหน้าใดหน้าหนึ่งที่ใช้ base.html
        response = self.client.get(reverse('login/templates/quota.html'))

        # ตรวจสอบว่า response status code เป็น 200 (แสดงผลได้ปกติ)
        self.assertEqual(response.status_code, 200)

        # ตรวจสอบว่ามีองค์ประกอบต่างๆ ที่ต้องการใน HTML
        self.assertContains(response, "ระบบขอโควต้ารายวิชา")
        self.assertContains(response, "ค้นหารายวิชา")
        self.assertContains(response, "ขอโควต้า")
        self.assertContains(response, "ผลการขอโควต้า")
        self.assertContains(response, "Logout")

    def test_base_template_includes_fonts_and_styles(self):
        # ทำการเรียกหน้าเว็บที่ใช้ base.html
        response = self.client.get(reverse('login/templates/quota.html'))

        # ตรวจสอบว่ามีการโหลดฟอนต์จาก Google Fonts และมีไฟล์ CSS ที่ต้องการ
        self.assertContains(response, "https://fonts.googleapis.com/css2?family=Kanit")
        self.assertContains(response, "https://fonts.googleapis.com/css2?family=Mitr")
        self.assertContains(response, "/static/css/basestyle.css")

    def test_navigation_links_in_base_template(self):
        # ตรวจสอบลิงก์ใน navigation bar
        response = self.client.get(reverse('login/templates/quota.html'))

        # ตรวจสอบลิงก์สำหรับการค้นหา
        self.assertContains(response, 'href="/search"')
        self.assertContains(response, 'href="/quota"')
        self.assertContains(response, 'href="/result"')
        self.assertContains(response, 'href="/"')  # Logout

    def test_base_template_has_icon_images(self):
        # ตรวจสอบการแสดงผลของรูปภาพไอคอน
        response = self.client.get(reverse('login/templates/quota.html'))

        # ตรวจสอบไอคอนแต่ละตัว
        self.assertContains(response, 'src="/static/css/search.png"')
        self.assertContains(response, 'src="/static/css/register-icon-1024x1024-hi8iv4nr.png"')
        self.assertContains(response, 'src="/static/css/registration-3.png"')
        self.assertContains(response, 'src="/static/css/logout-1-icon-2048x2048-dsthju9g.png"')
