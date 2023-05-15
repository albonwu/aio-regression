from rest_framework import serializers

from .models import Coordinate, Params

class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = "__all__"

class ParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Params
        fields = '__all__'