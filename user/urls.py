from django.urls import path
from user.views import (
    registration_view,
    CustomAuthToken
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'user'

urlpatterns = [
    path('register', registration_view, name='register'),
    path('login', CustomAuthToken.as_view(), name='login'),
]