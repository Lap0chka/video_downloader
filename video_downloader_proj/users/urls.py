from django.contrib.auth.decorators import login_required
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls
from . import views

urlpatterns = [
    path("password_reset/", views.MyPasswordResetView.as_view(), name='password_reset'),
    path("", include("django.contrib.auth.urls")),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('send_email/', views.send_user_email, name='send_email'),
    path('confirm_email/<str:token>', views.confirm_email, name='confirm_email')

]
