from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .serializers import CoordinateSerializer

@api_view(['POST'])
def add(request):
    serializer = CoordinateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)