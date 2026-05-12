from django.urls import path
from classView.views import *
urlpatterns = [
    path('alldata/', All_data_list.as_view(), name='alldata'),
    path('alldata/<int:pk>/', All_data_detail.as_view(), name='alldatai'),
    path('media/', ListFiles.as_view(), name='media'),
]
