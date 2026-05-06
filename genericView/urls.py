from django.urls import path
from genericView.views import *

urlpatterns = [
    path('userdata/', ListUser.as_view(), name='userdata')
]
