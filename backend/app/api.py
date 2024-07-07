from datetime import datetime
import json
import time
import uuid
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .forms import PoolForm
from .serializers import EnrollmentReadSerializer, EnrollmentWriteSerializer, PoolSpaceSerializer,TournamentSerializer
from .models import Enrollment, MpesaTransaction, PoolSpace,Tournament
from rest_framework.permissions import AllowAny, IsAuthenticated
from math import radians, cos, sin, sqrt, atan2
from geopy.distance import geodesic
from accounts.models import User
from .mpesa import LipaNaMpesa


@api_view(['GET'])
@permission_classes([AllowAny])
def pool_spaces(request):
    time.sleep(2)
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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_pool_spaces(request):
    try:
        pool_spaces = PoolSpace.objects.filter(user=request.user)
        serializer = PoolSpaceSerializer(pool_spaces, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_pool_spaces(request):
    pool_spaces = PoolSpace.objects.all()
    serializer = PoolSpaceSerializer(pool_spaces, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_pool_space(request, pk):
    try:
        pool_space = PoolSpace.objects.get(pk=pk)
    except PoolSpace.DoesNotExist:
        return Response({"error": "PoolSpace not found"}, status=404)
    
    serializer = PoolSpaceSerializer(pool_space)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_pool_space(request, pk):
    try:
        pool_space = PoolSpace.objects.get(pk=pk)
    except PoolSpace.DoesNotExist:
        return Response({"error": "PoolSpace not found"}, status=404)
    
    if request.method == 'PUT':
        serializer = PoolSpaceSerializer(pool_space, data=request.data)
    else:  # PATCH request
        serializer = PoolSpaceSerializer(pool_space, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)



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



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_tournament(request):
    try:
        # Extract data from request payload
        title = request.data.get('title')
        description = request.data.get('description', '')
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        enrollment_fee = request.data.get('enrollment_fee')
        organizer_id = request.data.get('organizer')

        # Validate organizer exists
        organizer = get_object_or_404(User, id=organizer_id)
    
        pool_space = get_object_or_404(PoolSpace, user=organizer)
    
        tournament_data = {
            'title': title,
            'description': description,
            'start_time': start_time,
            'end_time': end_time,
            'enrollment_fee': enrollment_fee,
            'organizer': str(organizer.id), 
            'pool_space': str(pool_space.id)
        }
        serializer = TournamentSerializer(data=tournament_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['PUT'])
@authentication_classes([])
@permission_classes([])
def update_tournament(request, pk):
    try:
        tournament = get_object_or_404(Tournament, pk=pk)
        data = request.data
        serializer = TournamentSerializer(tournament, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
@authentication_classes([])
@permission_classes([])
def delete_tournament(request, pk):
    try:
        tournament = get_object_or_404(Tournament, pk=pk)
        tournament.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def owner_event(request,user_id):
    time.sleep(2)
    user = User.objects.get(pk=user_id)
    events = Tournament.objects.filter(organizer=user).order_by('-created_at')
    serializer = TournamentSerializer(events, many=True)

    return Response(serializer.data)

# puplic
@api_view(['GET'])
@permission_classes([AllowAny])
def events(request):
    time.sleep(2)
    events = Tournament.objects.all().order_by('-created_at')[:10]
    serializer = TournamentSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_one_event(request, event_id):
    time.sleep(2)  # Delay for testing purposes
    try:
        event = Tournament.objects.select_related('pool_space').get(id=event_id)
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
    time.sleep(2)
    user = request.user
    enrollments = Enrollment.objects.filter(user=user)
    serializer = EnrollmentReadSerializer(enrollments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def pay_enrollment_fee(request, id):
    try:
        enrollment = Enrollment.objects.get(id=id, user=request.user)
        # enrollment = Enrollment.objects.get(id=id, user=request.user, paid=False)
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
        response = mpesa.stk_push(payload)
        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['POST'])
@permission_classes([AllowAny])
def mpesa_callback(request):
    try:
        data = json.loads(request.body)
        stk_callback = data.get('Body', {}).get('stkCallback', {})

        print("callback data", stk_callback)

        merchant_request_id = stk_callback.get('MerchantRequestID')
        checkout_request_id = stk_callback.get('CheckoutRequestID')
        result_code = stk_callback.get('ResultCode')
        result_description = stk_callback.get('ResultDesc')

        callback_metadata = stk_callback.get('CallbackMetadata', {}).get('Item', [])
        amount = next((item['Value'] for item in callback_metadata if item['Name'] == 'Amount'), None)
        mpesa_receipt_number = next((item['Value'] for item in callback_metadata if item['Name'] == 'MpesaReceiptNumber'), None)
        transaction_date = next((item['Value'] for item in callback_metadata if item['Name'] == 'TransactionDate'), None)
        phone_number = next((item['Value'] for item in callback_metadata if item['Name'] == 'PhoneNumber'), None)

        transaction = MpesaTransaction.objects.filter(merchant_request_id=merchant_request_id).first()

        if transaction:
            if transaction.is_processed:
                return Response({'error': 'Transaction has already been processed'}, status=status.HTTP_400_BAD_REQUEST)
            transaction.checkout_request_id = checkout_request_id
            transaction.result_code = result_code
            transaction.result_description = result_description
            transaction.amount = amount
            transaction.mpesa_receipt_number = mpesa_receipt_number
            transaction.transaction_date = transaction_date
            transaction.phone_number = phone_number
            transaction.is_processed = True
            transaction.save()

            # Update the enrollment status to paid
            if result_code == 0:
                enrollment = transaction.enrollment
                enrollment.paid = True
                enrollment.save()

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        # Handle exceptions gracefully
        print(f"Error processing M-Pesa callback: {str(e)}")
        return Response({'error': 'Error processing callback'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)