from django.shortcuts import render
from rest_framework import viewsets
from viewsetView.serializers import FruitSerializer
from viewsetView.models import Fruits

class UserViewset(viewsets.ModelViewSet):
    queryset = Fruits.objects.all()
    serializer_class = FruitSerializer
