import uuid

from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages

from .tasks import send_email_verification
from .forms import RegisterUserForm
from .models import User


class RegisterUser(CreateView):
    """
    A view class that handles the registration of a new user by extending Django's CreateView.
    Upon successful registration, it displays a success message, sends a verification email, and redirects to the login page.

    Methods:
        form_valid(self, form): Overrides the form_valid method to display a success message, send a verification email, and redirect to the login page.
    """
    model = User
    template_name = 'users/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have registered successfully. Please log in.')
        user = form.instance
        send_user_email(self.request, user)
        return response


def send_user_email(request, user):
    """
    Sends an email verification link to the user for confirming their email address asynchronously.

    Returns:
    None
    """
    token = uuid.uuid4().hex
    base_url = request.build_absolute_uri(reverse_lazy('confirm_email', args=[token]))
    send_email_verification.delay(user.username, user.email, base_url, token)
    message = 'Email has been sent successfully'
    messages.success(request, message)


def confirm_email(reqeust, token):
    """
    Confirm the user's email address based on the provided token.

    Returns:
        HttpResponseRedirect: Redirects to the appropriate page based on the confirmation status.
    """
    redis_key = settings.MYVARRIABLE_USER_CONFIRMATION_KEY.format(token=token)
    user_info = cache.get(redis_key) or {}

    if user_info:
        username = user_info.get("user_name")
        user = get_object_or_404(User, username=username)
        user.is_email_verification = True
        user.save()
        messages.success(reqeust, 'You have confirm your email successfully.')
        return redirect(to=reverse_lazy('downloader:index'))
    else:
        return redirect(to=reverse_lazy('user:login'))


class MyPasswordResetView(PasswordResetView):
    """
    Custom password reset view that extends Django's PasswordResetView.
    On successful form submission, it checks if the provided email is registered in the User model.
    If the email is not registered, it displays an error message and redirects to the password reset page.
    Otherwise, it proceeds with the default behavior of Django's PasswordResetView.

    Methods:
        form_valid(self, form): Overrides the form_valid method of PasswordResetView.
                                Checks if the email is registered and displays an error message if not.
                                Returns the super class's form_valid method if the email is registered.
    """
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.filter(email=email).first()
        if not user:
            messages.error(self.request, 'This email is not registered. Try again')
            return redirect(reverse('password_reset'))
        return super().form_valid(form)
