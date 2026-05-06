from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from funcView.serializers import StudentsSerializer
from funcView.models import Students

@api_view(["GET", "POST"])
def listData(request):
    if request.method == "GET":
        obj = Students.objects.all()
        serializer = StudentsSerializer(obj, many=True)
        return Response({"Message": "OK", "Data": serializer.data})
    elif request.method == "POST":
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"New data added": serializer.data})

