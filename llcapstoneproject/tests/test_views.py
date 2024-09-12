from django.test import TestCase, RequestFactory
from django.urls import reverse
from restaurant.models import MenuItem

class MenuViewTest(TestCase):
    
    def setUp(self):
        item1 = MenuItem.objects.create(title = "Icecream", price = 80, inventory = 100)
        item1.save()
        
        item2 = MenuItem.objects.create(title = "Chocolate", price = 180, inventory = 100)
        item2.save()
        
    #def test_getall(self):
        # response = self.client.get(reverse('menu-items'))
        # self.assertEqual(response.status_code, 200)