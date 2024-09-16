# accounts/urls.py
from django.urls import path
from .views import signUpView

urlpatterns = [
    path('signUp/', signUpView.as_view(), name='signUp'),
]