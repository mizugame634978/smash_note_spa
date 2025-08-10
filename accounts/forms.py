from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (

            "email",


        )

class LoginFrom(AuthenticationForm):

    class Meta:
        model = User
