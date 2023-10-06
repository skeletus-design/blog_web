from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from polls.forms import RegistrationFrom
from django.contrib.auth import authenticate, login, logout
from django_registration.backends.one_step.views import RegistrationView




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

def sign_up(request):
    if request.method == 'POST':
        print('bigballs')
        form = RegistrationFrom()
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('auth')
        return render(request, 'registration.html', { 'form': form})
    else:
        form = RegistrationFrom()
        return render(request, 'registration.html', { 'form': form})ы
    
    
# def sign_upp(request):
#     if request.method == 'POST':
#         form = RegistrationFrom()
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('auth')


class CustomRegistrationView(RegistrationView):
    """
    Вьюшка для регистрации пользователя в аккаунт
    """

    template_name = 'registration.html'
    form_class = RegFrom
    success_url = reverse_lazy('profile')

    def dispatch(self, args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.success_url)

        return super().dispatch(args, **kwargs)
        

def index(request):
    if request.user.is_authenticated:
        return render(request, 'main.html') 
    else:
        return redirect('/auth')

