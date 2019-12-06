from django.test import TestCase
from .models import Restaurant, MenuItem


class RestaurantModelTests(TestCase):
    def setUp(self):
        self.etienneGabon = Restaurant(name='Etienne', street='6 rue Sala', code='56100', city='Vannes', country='Gabon')
        self.eFrance = Restaurant(name='E2', street='6 rue Sala', code='56100', city='Vannes')
        self.eCodeVannes = Restaurant(name='E3', street='', code='56100', city='Vannes')
        self.eVannes = Restaurant(name='E4', street='', code='', city='Vannes')
        self.eCode = Restaurant(name='E4', street='', code='56100', city='')

    def test_validate_address(self):
        self.assertEqual('6 rue Sala, 56100 Vannes, Gabon', self.etienneGabon.address)
        self.assertEqual('6 rue Sala, 56100 Vannes, France', self.eFrance.address)
        self.assertEqual('56100 Vannes, France', self.eCodeVannes.address)
        self.assertEqual('Vannes, France', self.eVannes.address)
        self.assertEqual('56100, France', self.eCode.address)

    def test_str(self):
        self.assertEqual('Etienne', str(self.etienneGabon))


class MenuItemModelTests(TestCase):
    def setUp(self):
        self.restaurant = Restaurant(name='some', street='1', code='2', city='Troies')
        self.pasta = MenuItem(name='pasta', price=7.59, restaurant=self.restaurant)
        self.pizza = MenuItem(name='pizza', price=13, restaurant=self.restaurant)

    def test_str(self):
        self.assertEqual('pasta', str(self.pasta))
