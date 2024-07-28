from django.db import models
from accounts.models import User
from datetime import timezone
import uuid

class PoolSpace(models.Model):
    title = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=50, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    user = models.OneToOneField(User, related_name='pool_space', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='inactive')

    def __str__(self):
        return self.title

class Tournament(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, related_name='organized_tournaments', on_delete=models.CASCADE)
    pool_space = models.ForeignKey(PoolSpace, related_name='tournaments', on_delete=models.CASCADE)
    attendees = models.ManyToManyField(User, related_name='tournaments_attending', blank=True)
    enrollment_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=[('upcoming', 'Upcoming'), ('ongoing', 'Ongoing'), ('past', 'Past')], default='upcoming')

    @property
    def attendees_count(self):
        return self.attendees.count()

    def __str__(self):
        return self.title
  

class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.name} - {self.tournament.title}"
    

class Tag(models.Model):
    name = models.CharField(max_length=100)
    tournaments = models.ManyToManyField(Tournament, related_name='tags')

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.name} on {self.tournament.title}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.name} about {self.tournament.title}"


class MpesaTransaction(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    merchant_request_id = models.CharField(max_length=100, unique=True,)
    checkout_request_id = models.CharField(max_length=100, unique=True,)
    result_code = models.IntegerField(null=True, blank=True)
    result_description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    mpesa_receipt_number = models.CharField(max_length=50, null=True, blank=True)
    transaction_date = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    is_processed = models.BooleanField(default=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"M-Pesa Transaction - {self.checkout_request_id}"


