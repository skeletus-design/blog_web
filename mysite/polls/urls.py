from django.urls import path

from . import views

urlpatterns = [
    path("", views.AboutView.as_view(), name="index"),
    path("auth/", views.auth.as_view(), name="auth"),
    path("", views.registration, name="registr")
]

