import time
from django.http import JsonResponse
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import User
from .forms import signUpForm
from .serializer import UserSerializer,ChangePasswordSerializer,PublicUserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def user(request):
    time.sleep(2)
    return JsonResponse({
        'id': request.user.id,
        'username': request.user.username,
        'role': request.user.role,
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def register_user(request):
    data = request.data
    form = signUpForm(data)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')

        if User.objects.filter(email=email).exists():
            return Response({'message': 'error', 'error': 'Email is already taken'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(username=username).exists():
            return Response({'message': 'error', 'error': 'Username is already taken'}, status=status.HTTP_400_BAD_REQUEST)

        form.save()
        return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
    else:
        errors = form.errors
        return Response({'message': 'error', 'errors': errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def get_user_data(request, pk):
    try:
        user = User.objects.get(pk=pk)

        if request.method == "GET":
            serializer = UserSerializer(user)
            return Response(serializer.data)
        
        elif request.method == "PATCH":
            user_avater = request.Files.get('user_avatar')

            if user_avater:
                user.user_avatar = user_avater
                user.save()
                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return Response({'message': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)
    except user.DoesNotExist:
        return Response({'message': 'User not found'},status=status.HTTP_404_NOT_FOUND)