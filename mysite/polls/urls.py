from django.urls import path

from . import views

urlpatterns = [
    path("", views.AboutView.as_view(), name="index"),
    path("auth/", views.auth.as_view(), name="auth"),
    path("registration_page/", views.registration_page.as_view(), name="registration_page"),
    path("profile/", views.profile.as_view(), name="profile"),
    path("", views.registration, name="registr"),
    path("add_post/", views.add_post.as_view(), name="add_post"),
]

