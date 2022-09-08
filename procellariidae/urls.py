from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('incidents/', views.incidents_list, name='incidents_list'),
    path('incident/<int:pk>', views.incident_detail, name='incident_detail'),
    path('incident/new/', views.incident_new, name='incident_new'),
    path('incident/<int:pk>/edit/', views.incident_edit, name='incident_edit'),
]