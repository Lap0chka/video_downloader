from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .forms import RegisterUserForm
from .models import User


class RegisterUser(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = RegisterUserForm
    success_url = 'user:login'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have registered successfully. Please log in.')
        # send_user_email(self.request)
        return response


class MyPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.filter(email=email).first()
        if not user:
            messages.error(self.request, 'This email is not registered. Try again')
            return redirect(reverse('password_reset'))
        return super().form_valid(form)
