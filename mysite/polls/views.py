from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'templates/main.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        form.is_valid()
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Привет {username} ваш аккаунт был успешно создан!')
        return redirect('home')
    else:
        form = UserRegisterForm

    return render(request, 'templates/registration.html', {'form': form})
# @login_required()
# def profile(request):
#     return render(request,)
