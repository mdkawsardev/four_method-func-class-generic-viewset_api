from rest_framework import serializers
from genericView.models import Animals

class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animals
        fields = "__all__"