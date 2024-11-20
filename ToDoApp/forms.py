from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class RegisterForm(UserCreationForm):

    username = forms.CharField(
        required=True,
        min_length=3,
    )

    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password'
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password'
            }
        ),
        help_text='Use the same password as before',
        required=False,
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
