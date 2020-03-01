from django.urls import path

from cars import views
from cars.views import CarCreateView, CarListView, DetailView

urlpatterns = [
    path('', views.index, name='index.html'),
    path('cars-list/', CarListView.as_view()),
    path('cars/create', CarCreateView.as_view()),
    path('about/', views.about,  name='about.html'),
    path('login/', views.login,  name='login.html'),
    path('register/', views.register,  name='register.html'),
]