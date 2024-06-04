from django.test import TestCase
from restaurant.models import Menu



class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="Noodles", Price=80.00, Inventory=100)
        Menu.objects.create(Title="Pasta", Price=200.00, Inventory=50)
        Menu.objects.create(Title="Lassi", Price=15.00, Inventory=150)

    def test_get_all(self):
        item1 = Menu.objects.get(Title="Noodles")
        item2 = Menu.objects.get(Title="Pasta")
        item3 = Menu.objects.get(Title="Lassi")
        self.assertEqual(item1.Price, 80.00)
        self.assertEqual(item2.Price, 200.00)
        self.assertEqual(item3.Price, 15.00)
        
