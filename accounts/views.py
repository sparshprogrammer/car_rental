from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

# Create your views here.

def login(request):
    return render(request,"login.html", {})