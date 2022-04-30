from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def home(request):
    return HttpResponse("Funcionou")

def about(request):
    return HttpResponse("sobre nos")

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"