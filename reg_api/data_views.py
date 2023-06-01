from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CoordinateSerializer
from .models import Coordinate

@api_view(['GET'])
def points(request):
    coords = Coordinate.objects.all()
    serializer = CoordinateSerializer(coords, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def point(request, pk):
    coord = Coordinate.objects.get(pk = pk)
    serializer = CoordinateSerializer(coord)
    return Response(serializer.data)