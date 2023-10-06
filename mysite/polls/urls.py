from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auth/", views.auth, name="auth"),
    path("registration_page/", views.registration, name="registration_page"),
    path("profile/", views.profile.as_view(), name="profile"),
    path("sign_in", views.login_ , name="login"),#Путь для логина
    path("logout", views.log_out, name="logout"),
    #path("auth", views.sign_upp, name="registration"),
    # path("reg/", views.registration),
]

