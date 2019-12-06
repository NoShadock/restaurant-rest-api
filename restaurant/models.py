from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=1000)
    code = models.CharField('Post code', max_length=5)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='France')

    @property
    def address(self):
        attrs = [self.street, self.code, self.city, self.country]
        notempty = [s for s in attrs if s]
        return ', '.join(notempty)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
