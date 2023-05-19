from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CoordinateSerializer
from .models import Coordinate

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