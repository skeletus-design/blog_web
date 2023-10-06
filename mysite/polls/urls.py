from django.urls import path

from . import views

urlpatterns = [
    path("", views.AboutView, name="index"),
    path("auth/", views.auth, name="auth"),
    path("registration_page/", views.registration_page.as_view(), name="registration_page"),
    path("profile/", views.profile.as_view(), name="profile"),
    path("sign_in", views.login_ , name="login"), #Путь до логина
]