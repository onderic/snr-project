import time
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .forms import PoolForm
from .serializers import EnrollmentReadSerializer, EnrollmentWriteSerializer, PoolSpaceSerializer,TournamentSerializer
from .models import Enrollment, PoolSpace,Tournament
from rest_framework.permissions import AllowAny, IsAuthenticated
from math import radians, cos, sin, sqrt, atan2
from geopy.distance import geodesic
from accounts.models import User
from .mpesa import LipaNaMpesa


@api_view(['GET'])
@permission_classes([AllowAny])
def pool_spaces(request):
    time.sleep(1)
    user_lat = request.query_params.get('latitude')
    user_lng = request.query_params.get('longitude')

    if not user_lat or not user_lng:
        return Response({"error": "User coordinates are required"}, status=400)

    try:
        user_location = (float(user_lat), float(user_lng))
    except ValueError:
        return Response({"error": "Invalid coordinates"}, status=400)

    pool_spaces = PoolSpace.objects.all()
    
    pool_spaces_with_distance = []
    for pool_space in pool_spaces:
        pool_space_location = (pool_space.latitude, pool_space.longitude)
        distance = geodesic(user_location, pool_space_location).km
        pool_spaces_with_distance.append((pool_space, distance))
    
    pool_spaces_with_distance.sort(key=lambda x: x[1])

    sorted_pool_spaces = [pool_space for pool_space, distance in pool_spaces_with_distance]
    
    serializer = PoolSpaceSerializer(sorted_pool_spaces, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_pool_space(request):
    # time.sleep(1)
    serializer = PoolSpaceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# tournaments
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_tournament(request):
    serializer = TournamentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def owner_event(request,user_id):
    user = User.objects.get(pk=user_id)
    events = Tournament.objects.filter(organizer=user).order_by('-created_at')
    serializer = TournamentSerializer(events, many=True)

    return Response(serializer.data)

# puplic
@api_view(['GET'])
@permission_classes([AllowAny])
def events(request):
    # time.sleep(1)
    events = Tournament.objects.all().order_by('-created_at')[:10]
    serializer = TournamentSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_one_event(request, event_id):
    try:
        event = Tournament.objects.get(id=event_id)
    except Tournament.DoesNotExist:
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = TournamentSerializer(event)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enroll_event(request):
    time.sleep(1)
    serializer = EnrollmentWriteSerializer(data=request.data)
    
    if serializer.is_valid():
        user = request.user
        tournament = serializer.validated_data['tournament']

        if Enrollment.objects.filter(user=user, tournament=tournament).exists():
            return Response({'error': 'You already enrolled in this tournament'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_enrollments(request):
    user = request.user
    enrollments = Enrollment.objects.filter(user=user)
    serializer = EnrollmentReadSerializer(enrollments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def pay_enrollment_fee(request, id):
    try:
        enrollment = Enrollment.objects.get(id=id, user=request.user, paid=False)
    except Enrollment.DoesNotExist:
        return Response({'error': 'Enrollment not found or already paid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    phone_number = request.data.get('phone_number')
    amount = request.data.get('amount')

    if not phone_number or not amount:
        return Response({'error': 'Phone number and amount are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    if phone_number.startswith('0'):
        phone_number = '254' + phone_number[1:]
    
    payload = {
        'enrollment_id': id,
        'phone_number': phone_number,
        'amount': amount
    }

    mpesa = LipaNaMpesa()

    try:
        response = mpesa.make_stk_push(payload)
        # enrollment.paid = True
        # enrollment.save()
        
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)