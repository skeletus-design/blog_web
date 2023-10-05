from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django import forms
from django.contrib.auth import authenticate, login, logout
from polls.forms import SignInForm


class AboutView(TemplateView):
    template_name = "main.html"
    
class auth(TemplateView):
    template_name = "auth.html"
    
class registration_page(TemplateView):
    template_name = "registration.html"
    
class profile(TemplateView):
    template_name = "profile.html"
    
    
def registration(request):
    if request.method == "POST":
        return render(request, 'registration.html')

# def SignIn(forms.Form):
#     if request.method == 'POST':
#         form = SignIn        
#             username = forms.CharField(max_length=16)
#             password = forms.PasswordInput()

# Логин
def login_(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        
# if request.user.is_authenticated:
#         return render(request, 'index.html') 
#     else:
#         return redirect('/sign_in')

# def form_context(request):
#     form = SignInForm(request.POST or None)
#     return {'form': form}