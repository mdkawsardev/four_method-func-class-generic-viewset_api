from rest_framework import serializers
from viewsetView.models import Fruits

class FruitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fruits
        fields = "__all__"