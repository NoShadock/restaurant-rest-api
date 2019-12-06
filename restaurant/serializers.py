from rest_framework import serializers
from .models import MenuItem, Restaurant


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['url', 'id', 'name', 'street', 'code', 'city', 'country', 'address']


class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['url', 'id', 'restaurant', 'restaurant_id', 'name', 'price']
