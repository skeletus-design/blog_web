from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationFrom
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# class AboutView(TemplateView):
#     template_name = "main.html"
    
def AboutView(request):
    return render(request, 'polls/main.html')

class auth(TemplateView):
    template_name = "polls/auth.html"

def auth(request):
    return render(request, 'polls/auth.html')

class registration_page(TemplateView):
    template_name = "polls/registration.html"

class profile(TemplateView):
    template_name = "polls/profile.html"



# def SignIn(forms.Form):
#     if request.method == 'POST':
#         form = SignIn
#             username = forms.CharField(max_length=16)
#             password = forms.PasswordInput()

# # Логин
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



#
def index(request):
    if request.user.is_authenticated:
        return render(request, 'polls/main.html')
    else:
        return redirect('/auth')

def registration(request):
    if request.method == 'POST':
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('AboutView')

        else:
            form = RegistrationFrom()

        return render(request, 'polls/registration.html', {'form': form})

