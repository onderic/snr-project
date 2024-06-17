from django.db import models
from accounts.models import User
from datetime import timezone

class PoolSpace(models.Model):
    title = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    user = models.ForeignKey(User, related_name='owned_pool_spaces', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='inactive')

    def __str__(self):
        return self.title

class Tournament(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, related_name='organized_tournaments', on_delete=models.CASCADE)
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
