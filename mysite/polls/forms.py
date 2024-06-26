
from django import forms
from django_registration.forms import RegistrationForm
from django.contrib.auth.models import User


# class SignInForm(forms.Form):
#     login = forms.CharField(max_length=16)
#     password = forms.CharField(widget=forms.PasswordInput())
    
#     def __init__(self, *args, **kwargs):
#         super(SignInForm, self).__init__(*args, **kwargs)
    
    
class RegFrom(RegistrationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']