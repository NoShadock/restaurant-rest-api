from .models import MenuItem, Restaurant
from .serializers import MenuItemSerializer, RestaurantSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Model
import random


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows restaurants to be viewed or edited.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    @action(methods=['get'], detail=False)
    def random(self, request):
        try:
            ids = list(map(lambda x: x.id, Restaurant.objects.all()))
            rand_id = ids[random.randint(0, len(ids) - 1)]
            serializer = RestaurantSerializer(Restaurant.objects.get(id=rand_id),
                                              context={'request': request}, many=False)
            return Response(serializer.data)

        except IndexError:
            raise Model.DoesNotExist()

    @action(methods=['get', 'post', 'put', 'delete'], detail=True)
    def menu(self, request, pk=None):
        queryset = MenuItem.objects.filter(restaurant_id=pk)
        serializer = MenuItemSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)


class MenuItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menuitems to be viewed or edited.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
