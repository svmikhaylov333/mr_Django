from django.contrib.auth.forms import UserCreationForm

from users.models import User


class StyleFormMixin:
    pass


class UserRegisterForm(StyleFormMixin,UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']