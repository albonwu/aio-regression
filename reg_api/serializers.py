from rest_framework import serializers

from .models import Coordinate, Params, QuadParams

class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = "__all__"

class ParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Params
        fields = '__all__'

class QuadParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuadParams
        fields = '__all__'