from django.test import TestCase
from restaurant.models import Menu

class MenuTestCase(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80.00, Inventory=100)
        expected_result = "IceCream : 80.00"
        actual_result = str(item)
        self.assertEqual(actual_result, expected_result)
