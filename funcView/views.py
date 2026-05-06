from django.shortcuts import render
from rest_framework.decorators import api_view

@api_view(["GET", "POST", "PUT", "DELETE"])
def listData(request):
    pass
