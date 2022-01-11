# Django
from django.test import TestCase

# Local Apps
from elements.models import Element

class ListTestCase(TestCase):
    def setUp(self):
        Element.objects.create(content=1, order=1)
        Element.objects.create(content=2, order=2)
        Element.objects.create(content=3, order=3)
        Element.objects.create(content=4, order=4)
        Element.objects.create(content=5, order=5)

    def test_home(self):
        request = self.client.get(f'/elements/')
        self.assertEqual(request.status_code, 200)

    def test_add_end(self):
        self.client.get(f'/elements/add/end/{6}/')
        self.assertEqual(Element.objects.all().last().content, 6)

    def test_index(self):
        request = self.client.get(f'/elements/index/{4}/')
        self.assertEqual(request.status_code, 200)

    def test_add_beginning(self):
        self.client.get(f'/elements/add/beginning/{7}/')
        self.assertEqual(Element.objects.all().order_by("order")[0].content, 7)
    

    def test_add_before(self):
        self.client.get(f'/elements/add/before/{1}/{10}/')
        self.assertEqual(Element.objects.all().order_by("order")[0].content, 10)

    def test_add_after(self):
        self.client.get(f'/elements/add/after/{1}/{10}/')
        self.assertEqual(Element.objects.all().order_by("order")[1].content, 10)
