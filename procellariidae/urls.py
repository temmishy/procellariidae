from django.urls import path
from . import views

urlpatterns = [
    path('', views.incidents_list, name='incidents_list'),
]