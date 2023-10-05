from django import forms

class SignInForm(forms.Form):
    login = forms.CharField(max_length=16)
    password = forms.CharField(widget=forms.PasswordInput())
    
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)