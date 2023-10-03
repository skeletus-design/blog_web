from django.urls import path

from . import views

urlpatterns = [
    path("", views.AboutView.as_view(), name="index"),
    path("auth/", views.auth.as_view(), name="auth"),
    path("registration/", views.registration.as_view(), name="registration"),
    path("profile/", views.profile.as_view(), name="profile")
]

