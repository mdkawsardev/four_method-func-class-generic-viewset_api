from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from funcView.serializers import StudentsSerializer
from funcView.models import Students

@api_view(["GET", "POST"])
def listData(request, format=None):
    if request.method == "GET":
        obj = Students.objects.all()
        serializer = StudentsSerializer(obj, many=True)
        return Response({"Message": "OK", "Data": serializer.data})
    elif request.method == "POST":
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"New data added": serializer.data})

@api_view(["GET", "PUT", "DELETE"])
def UpdateRetrieveDelete(request, pk):
    try:
        queryset = Students.objects.get(id=pk)
    except Students.DoesNotExist:
        return Response("Something went wrong!")
    if request.method == "GET":
        serializer = StudentsSerializer(queryset)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = StudentsSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        queryset.delete()
        return Response({"Data deletion": "Success"})
