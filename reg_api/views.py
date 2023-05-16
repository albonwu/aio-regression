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
    serializer = CoordinateSerializer(coords, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def linear(request):
    model = LinearRegression()
    model.fit(X, y)

    temp = Params(model.coef_, model.intercept_)
    serializer = ParamsSerializer(temp)

    return Response(serializer.data)

@api_view(['GET'])
def quadratic(request):
    poly_features = PolynomialFeatures(degree=2)
    X_poly = poly_features.fit_transform(X)

    model = LinearRegression()
    model.fit(X_poly, y)

    coeffs = model.coef_

    for i in coeffs:
        i = 0 if i == None else i

    temp = QuadParams(coeffs[0], coeffs[1], coeffs[2])
    serializer = QuadParamsSerializer(temp)

    return Response(serializer.data)