from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView
# Create your views here.
from cars.models import Cars


def index(request):

    # Render the HTML template base.html with the data in the context variable
    return render(request, 'index.html', context={})


def about(request):

    # Render the HTML template base.html with the data in the context variable
    return render(request, 'about.html', context={})


def login(request):

    # Render the HTML template base.html with the data in the context variable
    return render(request, 'login.html', context={})


def register(request):
    return render(request, 'register.html', context={})


class CarListView(ListView):
    model = Cars
    template_name = 'cars/cars_list.html'


class CarDetailView(DetailView):
    model = Cars


class CarCreateView(CreateView):
    model = Cars

