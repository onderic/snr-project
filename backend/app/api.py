from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import EnrollmentReadSerializer, EnrollmentWriteSerializer, PoolSpaceSerializer,TournamentSerializer,MpesaTransactionSerializer
from .models import Enrollment, MpesaTransaction, PoolSpace,Tournament
from rest_framework.permissions import AllowAny, IsAuthenticated
from geopy.distance import geodesic
from accounts.models import User
from .mpesa import LipaNaMpesa
from django.db.models import Sum
from django.utils.timezone import now
from rest_framework.response import Response
from .utils import get_totals  
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

import logging

# Set up logging
logger = logging.getLogger('app')

@api_view(['GET'])
@permission_classes([AllowAny])
def list_transactions(request):
    try:
        # Fetch all transactions
        transactions = MpesaTransaction.objects.all()

        # Serialize the data
        serializer = MpesaTransactionSerializer(transactions, many=True)

        # Log the request and response
        logger.debug("Fetching all transactions")
        logger.debug(f"Transactions found: {serializer.data}")

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        logger.error(f"Error occurred while fetching transactions: {str(e)}")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def pool_spaces(request):
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

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_pool_space(request, pk):
    try:
        pool_space = PoolSpace.objects.get(pk=pk)
    except PoolSpace.DoesNotExist:
        return Response({"error": "Pool space not found"}, status=status.HTTP_404_NOT_FOUND)

    pool_space.delete()
    return Response({"message": "Pool space deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


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
    else:
        serializer = PoolSpaceSerializer(pool_space, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)



@api_view(['POST'])
@authentication_classes([])
@permission_classes([]) 
def create_pool_space(request):
    print("Received request data:", request.data)
    
    serializer = PoolSpaceSerializer(data=request.data)
    if serializer.is_valid():
        pool_space = serializer.save()
        
        user_id = request.data.get('user')
    
        
        if user_id:
            try:
                user = User.objects.get(id=user_id)
             
                user.role = 'owner'
                user.save()
               
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except User.DoesNotExist:
                
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:

            return Response({'error': 'User ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_tournament(request):
    try:
        title = request.data.get('title')
        description = request.data.get('description', '')
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        enrollment_fee = request.data.get('enrollment_fee')
        organizer_id = request.data.get('organizer')

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
    user = User.objects.get(pk=user_id)
    events = Tournament.objects.filter(organizer=user).order_by('-created_at')
    serializer = TournamentSerializer(events, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def events(request):
    events = Tournament.objects.all().order_by('-created_at')[:10]
    serializer = TournamentSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_one_event(request, event_id): 
    try:
        event = Tournament.objects.select_related('pool_space').get(id=event_id)
    except Tournament.DoesNotExist:
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = TournamentSerializer(event)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enroll_event(request):
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
        enrollment = Enrollment.objects.get(id=id, user=request.user)
    except Enrollment.DoesNotExist:
        return Response({'error': 'Enrollment not found or already paid'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': 'An unexpected error occurred: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    phone_number = request.data.get('phone_number')
    amount = request.data.get('amount')

    if not phone_number or not amount:
        return Response({'error': 'Phone number and amount are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    if len(phone_number) != 10 or not (phone_number.startswith('01') or phone_number.startswith('07')):
        return Response({'error': 'Invalid Phone Number'}, status=status.HTTP_400_BAD_REQUEST)

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
        return JsonResponse(response, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({'error': 'An unexpected error occurred: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_transaction_status(request, checkout_request_id):
    try:
        transaction = MpesaTransaction.objects.get(checkout_request_id=checkout_request_id)
        
        return JsonResponse({
            'ResultCode': str(transaction.result_code) if transaction.result_code is not None else '',
            'ResultDesc': transaction.result_description if transaction.result_description is not None else ''
        })
    
    except MpesaTransaction.DoesNotExist:
        return JsonResponse({
            'ResultCode': '',
            'ResultDesc': ''
        })
    except:
        pass


@api_view(['POST'])
@permission_classes([AllowAny])
def mpesa_callback(request):
    try:
        callback_data = request.data
        body = callback_data.get('Body')

        if not body:
            return JsonResponse({'error': 'Body not found in request'}, status=400)

        stk_callback = body.get('stkCallback')

        merchant_request_id = stk_callback.get('MerchantRequestID')
        checkout_request_id = stk_callback.get('CheckoutRequestID')
        result_code = stk_callback.get('ResultCode')

        transaction = MpesaTransaction.objects.filter(checkout_request_id=checkout_request_id).first()

        if not transaction:
            return JsonResponse({'error': 'Transaction not found'}, status=404)

        if transaction.is_processed:
            return JsonResponse({'error': 'Transaction already processed'}, status=400)

        transaction.merchant_request_id = merchant_request_id
        transaction.checkout_request_id = checkout_request_id
        transaction.result_code = result_code
        transaction.result_description = stk_callback.get('ResultDesc')

        if result_code == 0:
            transaction.status = 'success'
            callback_metadata = stk_callback.get('CallbackMetadata', {}).get('Item', [])
            for item in callback_metadata:
                if item.get('Name') == 'Amount':
                    transaction.amount = item.get('Value')
                elif item.get('Name') == 'MpesaReceiptNumber':
                    transaction.mpesa_receipt_number = item.get('Value')
                elif item.get('Name') == 'TransactionDate':
                    transaction.transaction_date = item.get('Value')
                elif item.get('Name') == 'PhoneNumber':
                    transaction.phone_number = item.get('Value')
            enrollment = get_object_or_404(Enrollment, id=transaction.enrollment.id)
            enrollment.paid = True
            enrollment.save()
        else:
            transaction.status = 'failure'

        transaction.is_processed = True
        transaction.save()

        return JsonResponse({'status': 'success'}, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
 

def daily_revenue_graph(request):
    data = Enrollment.objects.filter(paid=True) \
        .select_related('tournament') \
        .values('enrolled_at') \
        .annotate(total_revenue=Sum('tournament__enrollment_fee')) \
        .order_by('enrolled_at')
    
    day_order = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }

    labels = []
    revenue_data = []

    # Extract and format the data
    day_revenue = {}
    for entry in data:
        enrolled_at = entry['enrolled_at']
        if enrolled_at:
            day_name = datetime.strptime(enrolled_at.strftime('%Y-%m-%d'), '%Y-%m-%d').strftime('%A')
            if day_name not in day_revenue:
                day_revenue[day_name] = 0.0
            day_revenue[day_name] += float(entry['total_revenue']) if entry['total_revenue'] is not None else 0.0
    sorted_days = sorted(day_revenue.keys(), key=lambda day: day_order[day])

    for day in sorted_days:
        labels.append(day)
        revenue_data.append(day_revenue[day])

    result = {
        'labels': labels,
        'data': revenue_data
    }

    return JsonResponse(result)



@api_view(['GET'])
@permission_classes([AllowAny])
def revenue_overview(request):
    totals = get_totals()
    response_data = {
        'daily_total': str(totals['daily_total']),
        'weekly_total': str(totals['weekly_total']),
        'monthly_total': str(totals['monthly_total']),
    }
    return JsonResponse(response_data)