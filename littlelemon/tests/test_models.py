from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_itew(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        itemstr = item.__str__()
        self.assertEqual(itemstr, "IceCream : 80")