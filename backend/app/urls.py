
from django.urls import path
from . import api

urlpatterns = [
    path('create-pool/', api.create_pool_space, name='create-pool'),
    path('pools/', api.pool_spaces, name='pools'),
]