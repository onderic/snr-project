import time
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .forms import PoolForm
from .serializer import PoolSpaceSerializer
from .models import PoolSpace
from rest_framework.permissions import AllowAny




@api_view(['GET'])
@permission_classes([AllowAny])
def pool_spaces(request):
    pool_spaces = PoolSpace.objects.filter(status='active')
    serializer = PoolSpaceSerializer(pool_spaces, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_pool_space(request):
    time.sleep(5)
    serializer = PoolSpaceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)