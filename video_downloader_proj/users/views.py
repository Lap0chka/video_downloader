from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import User


class MyLoginView(LoginView):
    model = User
    template_name = 'users/registration/login.html'
