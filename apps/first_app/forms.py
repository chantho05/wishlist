from django.forms import ModelForm
from django.contrib.auth.models import User

from django import forms

class RegistrationForm(ModelForm):
    first_name = forms.CharField(min_length=2)
    last_name = forms.CharField(min_length=2)
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
                'password': forms.PasswordInput()
        }

class SignInForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
                'password': forms.PasswordInput()
        }
