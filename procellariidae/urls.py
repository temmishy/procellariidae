from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('incidents/', views.incidents_list, name='incidents_list'),
    path('<int:pk>', views.incident_detail, name='incident_detail'),
]