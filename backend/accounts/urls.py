from django.urls import path
from rest_framework_simplejwt.views import (  
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import views as auth_views

from . import api

urlpatterns = [
    path('user/', api.user, name='user'),
    path('register/', api.register_user, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
