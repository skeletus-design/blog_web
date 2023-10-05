from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django import forms
from django.contrib.auth import authenticate, login, logout



# class AboutView(TemplateView):
#     template_name = "main.html"
    
def AboutView(request):
    return render(request, 'main.html')
    
# class auth(TemplateView):
#     template_name = "auth.html"
    
def auth(request):
    return render(request, 'auth.html')
    
class registration_page(TemplateView):
    template_name = "registration.html"
    
class profile(TemplateView):
    template_name = "profile.html"
    
def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/auth')   
     

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
            return redirect('index')
        else:
            return redirect('auth')
        



def index(request):
    if request.user.is_authenticated:
        return render(request, 'main.html') 
    else:
        return redirect('/auth')

