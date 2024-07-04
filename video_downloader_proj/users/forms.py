from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import User


class RegisterUserForm(UserCreationForm):
    """
    A form that extends UserCreationForm to register a new user with additional validation for email uniqueness.

    Attributes:
        Meta (class): Inner class that defines metadata options for the form, including the model and fields to be included.

    Methods:
        clean(self): Custom validation method to check if the provided email is already in use by another user.
    """

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already used")
        return cleaned_data
