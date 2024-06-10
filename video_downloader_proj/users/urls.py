from django.contrib.auth.decorators import login_required
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls
from . import views

app_name = 'user'

urlpatterns = [
    path("password_reset/", views.MyPasswordResetView.as_view(), name='password_reset'),
    path("", include("django.contrib.auth.urls")),
    path('register/', login_required(views.RegisterUser.as_view()), name='register'),

]
