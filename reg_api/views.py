import numpy as np

from rest_framework.decorators import api_view
from rest_framework.response import Response

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from .serializers import CoordinateSerializer, ParamsSerializer, QuadParamsSerializer
from .models import Coordinate, Params, QuadParams

coords = Coordinate.objects.all()
X = []
y = []

for coord in coords:
    X.append([coord.x])
    y.append(coord.y)

@api_view(['GET'])
def points(request):
    coords = Coordinate.objects.all()
    serializer = CoordinateSerializer(coords, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def linear(request):
    model = LinearRegression().fit(X, y)

    temp = Params()
    temp.m = model.coef_[0]
    temp.b = model.intercept_

    serializer = ParamsSerializer(temp)

    return Response(serializer.data)

@api_view(['GET'])
def quadratic(request):
    npX = np.array(X).reshape(-1, 1)
    npy = np.array(y)

    poly_features = PolynomialFeatures(degree=2)
    X_poly = poly_features.fit_transform(npX)

    model = LinearRegression().fit(X_poly, npy)

    coeffs = model.coef_
    c = model.intercept_

    temp = QuadParams()
    temp.a = coeffs[2]
    temp.b = coeffs[1]
    temp.c = c
    serializer = QuadParamsSerializer(temp)

    return Response(serializer.data)