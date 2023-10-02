from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_registration.backends.one_step.views import RegistrationView
from django.views.generic import DetailView
from . import forms


class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = forms.LoginForm


class CustomRegistrationView(RegistrationView):
    template_name = 'account/registration.html'
    form_class = forms.RegistrationForm


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    pass


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'account/profile.html'

    def get_object(self, queryset=None):
        return self.request.user



