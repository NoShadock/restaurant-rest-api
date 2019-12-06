from django.test import TestCase, Client
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

    def test_save_get(self):
        self.etienneGabon.save()
        bis = Restaurant.objects.get(name=self.etienneGabon.name)
        self.assertEqual(bis, self.etienneGabon)


class MenuItemModelTests(TestCase):
    def setUp(self):
        self.restaurant = Restaurant(name='some', street='1', code='2', city='Troies')
        self.restaurant.save()
        self.pasta = MenuItem(name='pasta', price=7.59, restaurant=self.restaurant)
        self.pizza = MenuItem(name='pizza', price=13, restaurant=self.restaurant)

    def test_str(self):
        self.assertEqual('pasta', str(self.pasta))

    def test_save_get(self):
        self.pasta.save()
        bis = MenuItem.objects.get(name=self.pasta.name)
        self.assertEqual(bis, self.pasta)


class ClientTests(TestCase):
    def setUp(self):
        self.fabriceGabon = Restaurant(name='Fabrice', street='234', code='XZ34', city='Paimpol', country='Gabon')
        self.etienneFrance = Restaurant(name='Etienne', street='6 rue Sala', code='56100', city='Vannes')
        self.save(Restaurant)
        self.pastaFabrice = MenuItem(name='pasta', price=7.59, restaurant=self.fabriceGabon)
        self.pizzaFabrice = MenuItem(name='pizza', price=13, restaurant=self.fabriceGabon)
        self.pastaEtienne = MenuItem(name='pasta', price=7.29, restaurant=self.etienneFrance)
        self.pizzaEtienne = MenuItem(name='pizza', price=2.56, restaurant=self.etienneFrance)
        self.save(MenuItem)
        # Every test needs a client.
        self.client = Client()

    def save(self, filter_type):
        for v in vars(self):
            if isinstance(getattr(self, v), filter_type):
                getattr(self, v).save()

    def test_get_restaurant(self):
        r = self.client.get('/restaurants/')
        self.assertEqual(200, r.status_code)
