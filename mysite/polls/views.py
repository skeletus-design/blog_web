from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "main.html"
    
class auth(TemplateView):
    template_name = "auth.html"
    
class registration_page(TemplateView):
    template_name = "registration.html"
    
class profile(TemplateView):
    template_name = "profile.html"
    
class add_post(TemplateView):
    template_name = "add_post.html"
def registration(request):
    if request.method == "POST":
        return render(request, 'registration.html')
