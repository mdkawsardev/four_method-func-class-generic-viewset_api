from django.urls import path
from funcView.views import *
urlpatterns = [
    path('data/', listData, name='data'),
    path('data/<int:pk>/', UpdateRetrieveDelete, name='data'),
]
