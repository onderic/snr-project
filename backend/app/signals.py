from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Enrollment

@receiver(post_save, sender=Enrollment)
def update_tournament_attendees(sender, instance, created, **kwargs):
    if created:
        instance.tournament.attendees.add(instance.user)