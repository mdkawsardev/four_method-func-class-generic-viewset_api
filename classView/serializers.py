from rest_framework import serializers
from classView.models import Citizen

class CitizenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Citizen
        fields = "__all__"