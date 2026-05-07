from django.urls import path
from genericView.views import *

urlpatterns = [
    path('userdata/', ListUser.as_view(), name='userdata'),
    path('userdata/<int:pk>/', UserDetail.as_view(), name='userdatadetail'),
]
