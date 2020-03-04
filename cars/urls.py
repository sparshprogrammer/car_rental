from django.urls import path

from cars import views
from accounts import views as acc_views
from cars.views import CarCreateView, CarListView, DetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('cars-list/', CarListView.as_view()),
    path('cars/create', CarCreateView.as_view()),
    path('about/', views.about,  name='about'),
    path('login/', acc_views.user_login,  name='login'),
    path('register/', acc_views.registration,  name='register'),
    path('logout/', acc_views.user_logout,  name='logout'),
]