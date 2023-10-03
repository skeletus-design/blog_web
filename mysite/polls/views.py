from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "main.html"
    
class auth(TemplateView):
    template_name = "auth.html"
    
<<<<<<< HEAD
class registration(TemplateView):
    template_name = "registration.html"
    
class profile(TemplateView):
    template_name = "profile.html"
=======
def registration(request):
    if request.method == "POST":
        return render(request, 'registration.html')
>>>>>>> 1d8763eb7697d33385f69ed463612b8ccb889ae4
