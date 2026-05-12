from rest_framework import serializers
from classView.models import Citizen, FileUpload

class CitizenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Citizen
        fields = "__all__"

class FileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileUpload
        fields = "__all__"