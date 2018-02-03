from django.forms import ModelForm
from django.contrib.auth.models import User

from django import forms

class RegistrationForm(ModelForm):
    name = forms.CharField(min_length=2)
    username = forms.CharField(min_length=2)
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['name', 'username', 'password']
        widgets = {
                'password': forms.PasswordInput()
        }

class SignInForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
                'password': forms.PasswordInput()
        }
