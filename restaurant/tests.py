from django.test import TestCase
from .models import Restaurant


class RestaurantModelTests(TestCase):
    def setUp(self):
        self.r1 = Restaurant(name='Etienne', street='6 rue Sala', code='56100', city='Vannes', country='Gabon')
        self.r2 = Restaurant(name='E2', street='6 rue Sala', code='56100', city='Vannes')
        self.r3 = Restaurant(name='E3', street='', code='56100', city='Vannes')
        self.r4 = Restaurant(name='E4', street='', code='', city='Vannes')
        self.r5 = Restaurant(name='E4', street='', code='56100', city='')

    def test_validate_address(self):
        self.assertEqual('6 rue Sala, 56100 Vannes, Gabon', self.r1.address)
        self.assertEqual('6 rue Sala, 56100 Vannes, France', self.r2.address)
        self.assertEqual('56100 Vannes, France', self.r3.address)
        self.assertEqual('Vannes, France', self.r4.address)
        self.assertEqual('56100, France', self.r5.address)
