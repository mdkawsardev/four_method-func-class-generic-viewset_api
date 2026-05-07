from django.shortcuts import render
from rest_framework import generics
from genericView.models import Animals
from genericView.serializers import AnimalSerializer

class ListUser(generics.ListCreateAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalSerializer
