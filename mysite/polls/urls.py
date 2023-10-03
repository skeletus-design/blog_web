from django.urls import path

from . import views

urlpatterns = [
    path("", views.AboutView.as_view(), name="index"),
    path("auth/", views.auth.as_view(), name="auth"),
<<<<<<< HEAD
    path("registration/", views.registration.as_view(), name="registration"),
    path("profile/", views.profile.as_view(), name="profile")
=======
    path("", views.registration, name="registr")
>>>>>>> 1d8763eb7697d33385f69ed463612b8ccb889ae4
]

