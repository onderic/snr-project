
from django.urls import path
from . import api

urlpatterns = [
    path('create-pool/', api.create_pool_space, name='create-pool'),
    path('pools/', api.pool_spaces, name='pools'),

    # tournaments
    path('tournaments_create/', api.create_tournament, name='tournaments_create'),
    path('owner_events/<uuid:user_id>/', api.owner_event),
    path('events/', api.events),
    path('events/<int:event_id>/', api.get_one_event),
    path('enroll_event/', api.enroll_event, name='enroll_event'),
    path('user-enrollments/', api.user_enrollments, name='user-enrollments'),
]