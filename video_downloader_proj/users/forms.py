from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already used")
        return cleaned_data
