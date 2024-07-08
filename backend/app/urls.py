
from django.urls import path
from . import api

urlpatterns = [
    path('create-pool/', api.create_pool_space, name='create-pool'),
    path('pools/', api.pool_spaces, name='pools'),
    path('pool-spaces/', api.list_pool_spaces, name='list_pool_spaces'),
    path('pool-spaces/<int:pk>/', api.retrieve_pool_space, name='retrieve_pool_space'),
    path('pool-spaces/<int:pk>/update/', api.update_pool_space, name='update_pool_space'),
    path('user-pool-spaces/', api.get_user_pool_spaces, name='get_user_pool_spaces'),
    path('delete-pool/<int:pk>/', api.delete_pool_space, name='delete_pool_space'),

    # tournaments
    path('tournaments_create/', api.create_tournament, name='tournaments_create'),
    path('owner_events/<uuid:user_id>/', api.owner_event),
    path('events/', api.events),
    path('events/<int:event_id>/', api.get_one_event),
    path('enroll_event/', api.enroll_event, name='enroll_event'),
    path('user-enrollments/', api.user_enrollments, name='user-enrollments'),

    path('tournaments_update/<int:pk>/', api.update_tournament, name='update_tournament'),
    path('tournaments_delete/<int:pk>/', api.delete_tournament, name='delete_tournament'),

    # mpesa
    path('pay-enrollment-fee/<uuid:id>/', api.pay_enrollment_fee, name='pay_enrollment_fee'),
    path('mpesa-callback/', api.mpesa_callback, name='mpesa-callback'),
]