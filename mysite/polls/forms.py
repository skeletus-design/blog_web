from django.contrib.auth.models import User
from django.auth.contrib.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

class Meta:
    model=User
    fields = ['name', 'last_name', 'email', 'password1', 'password2']