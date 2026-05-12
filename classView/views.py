from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from classView.models import Citizen, FileUpload
from classView.serializers import CitizenSerializer, FileUploadSerializer

class All_data_list(APIView):
    def get(self, request, format=None):
        queryset = Citizen.objects.all()
        serializer = CitizenSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CitizenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class All_data_detail(APIView):
    def obj(self, pk):
        try:
            return Citizen.objects.get(id=pk)
        except Citizen.DoesNotExist:
            return Response("Record not found!")
        
    def get(self, request, pk, format=None):
        queryset = self.obj(pk)
        serializer = CitizenSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.obj(pk)
        serializer = CitizenSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        queryset = self.obj(pk)
        queryset.delete()
        return Response({"Data deletion": "Success"})


#File handling
class ListFiles(APIView):
    def get(self, request):
        queryset = FileUpload.objects.all()
        serializer = FileUploadSerializer(queryset, many=True)
        return Response({"File": serializer.data})