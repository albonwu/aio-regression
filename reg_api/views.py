from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sklearn.linear_model import LinearRegression

from .serializers import CoordinateSerializer, ParamsSerializer
from .models import Coordinate, Params

@api_view(['GET'])
def points(request):
    coords = Coordinate.objects.all()
    serializer = CoordinateSerializer(coords, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def linear(request):
    coords = Coordinate.objects.all()
    X = []
    y = []

    for coord in coords:
        X.append([coord.x])
        y.append(coord.y)

    model = LinearRegression()
    model.fit(X, y)

    temp = Params(model.coef_, model.intercept_)
    serializer = ParamsSerializer(temp)

    return Response(serializer.data)