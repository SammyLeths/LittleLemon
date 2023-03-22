from django.test import TestCase, RequestFactory
from restaurant.models import MenuItem
from restaurant.views import MenuItemsView

class MenuViewTest(TestCase):
    def setUp(self):
        menu_item = MenuItem.objects.create(title="Coffe", price=80, inventory=100)
        return super().setUp()

    def test_getall(self):
        request = RequestFactory().get('/restaurant/menu-items/')
        view = MenuItemsView()
        view.setup(request)

        context = str(view.get_queryset())
        self.assertIn('Coffe : 80.00', context)