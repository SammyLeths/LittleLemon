from django.test import TestCase
from restaurant.models import MenuItem

class MenuTest(TestCase):
    def test_get_itew(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        itemstr = item.__str__()
        self.assertEqual(itemstr, "IceCream : 80")