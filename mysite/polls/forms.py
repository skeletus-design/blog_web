
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class SignInForm(forms.Form):
#     login = forms.CharField(max_length=16)
#     password = forms.CharField(widget=forms.PasswordInput())
    
#     def __init__(self, *args, **kwargs):
#         super(SignInForm, self).__init__(*args, **kwargs)
    
    
class RegistrationFrom(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        app_label = 'polls'
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']