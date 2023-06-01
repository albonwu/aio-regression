from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .serializers import CoordinateSerializer
from .models import Coordinate

@api_view(['POST'])
def post(request):
    serializer = CoordinateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PATCH'])
def patch(request, pk):
    try:
        obj = Coordinate.objects.get(pk = pk)
    except Coordinate.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    serializer = CoordinateSerializer(obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data, status=status.HTTP_200_OK)