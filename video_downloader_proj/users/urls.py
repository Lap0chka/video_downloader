from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
