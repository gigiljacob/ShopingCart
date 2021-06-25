from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignInForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,)
    last_name = forms.CharField(max_length=30, required=True,)
    phone_number = forms.CharField(widget=forms.NumberInput, required=True)
    email = forms.EmailField(widget=forms.EmailInput, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone_number',
                  'email', 'password1', 'password2')

