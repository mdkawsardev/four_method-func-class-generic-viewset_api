from django.urls import path
from classView.views import *
urlpatterns = [
    path('alldata/', All_data.as_view(), name='alldata')
]
