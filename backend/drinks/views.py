from django.shortcuts import render
from rest_framework import generics
from .serializers import DrinkSerializer
from .models import Drinks


class CreateDrink(generics.CreateAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinkSerializer

class UpdateDrinks(generics.RetrieveUpdateAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinkSerializer
    lookup_field = 'pk'

class DeleteDrink(generics.DestroyAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinkSerializer
    lookup_field = 'pk'

class GetSingleDrink(generics.RetrieveAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinkSerializer
    lookup_field = 'pk'

class GetAllDrinks(generics.ListAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinkSerializer

