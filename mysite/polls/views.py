from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "main.html"
    
class auth(TemplateView):
    template_name = "auth.html"