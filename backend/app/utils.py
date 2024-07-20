# utils.py

from django.db.models import Sum
from django.utils.timezone import now
from datetime import timedelta
from .models import MpesaTransaction

def get_totals():
    current_date = now()
    
    # Daily total
    start_of_day = current_date.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = current_date.replace(hour=23, minute=59, second=59, microsecond=999999)
    daily_total = MpesaTransaction.objects.filter(
        created_at__range=[start_of_day, end_of_day]
    ).aggregate(total_amount=Sum('amount'))['total_amount']
    
    # Weekly total
    start_of_week = current_date - timedelta(days=current_date.weekday())  # Monday of the current week
    end_of_week = start_of_week + timedelta(days=6, hours=23, minutes=59, seconds=59, microseconds=999999)
    weekly_total = MpesaTransaction.objects.filter(
        created_at__range=[start_of_week, end_of_week]
    ).aggregate(total_amount=Sum('amount'))['total_amount']
    
    # Monthly total
    start_of_month = current_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    end_of_month = (start_of_month.replace(month=start_of_month.month + 1) - timedelta(days=1)).replace(hour=23, minute=59, second=59, microsecond=999999)
    monthly_total = MpesaTransaction.objects.filter(
        created_at__range=[start_of_month, end_of_month]
    ).aggregate(total_amount=Sum('amount'))['total_amount']
    
    return {
        'daily_total': daily_total or 0,
        'weekly_total': weekly_total or 0,
        'monthly_total': monthly_total or 0
    }
