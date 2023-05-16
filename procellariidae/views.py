from django.shortcuts import render

from .models import Incident
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import IncidentForm

import os
import subprocess



def index(request):
    return render(request, 'index.html' )

def train_start(request):
    if request.method == 'POST':
        tf_dir = '/var/www/django-app/terraform'
        os.chdir(tf_dir)
        subprocess.Popen(['/usr/bin/terraform', 'apply', '-auto-approve', '-compact-warnings', '-input=false'])

        message = 'Тренировка запускается'
        return render(request, 'procellariidae/train_start.html', {'message': message})
    else:
        return render(request, 'procellariidae/train_start.html')

def train_stop(request):
    if request.method == 'POST':
        tf_dir = '/var/www/django-app/terraform'
        os.chdir(tf_dir)
        subprocess.Popen(['/usr/bin/terraform', 'destroy', '-auto-approve', '-compact-warnings', '-input=false'])
        
        message = 'Тренировка завершается'
        return render(request, 'procellariidae/train_stop.html', {'message': message})
    else:
        return render(request, 'procellariidae/train_stop.html')

def incidents_list(request):
    incidents = Incident.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'procellariidae/incidents_list.html', {'incidents': incidents})

def incident_detail(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    return render(request, 'procellariidae/incident_detail.html', {'incident': incident})

def incident_new(request):
    if request.method == "POST":
        form = IncidentForm(request.POST)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.author = request.user
            incident.published_date = timezone.now()
            incident.save()
            return redirect('incident_detail', pk=incident.pk)
    else:
        form = IncidentForm()
    return render(request, 'procellariidae/incident_edit.html', {'form': form})

def incident_edit(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    if request.method == "POST":
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.author = request.user
            incident.published_date = timezone.now()
            incident.save()
            return redirect('incident_detail', pk=incident.pk)
    else:
        form = IncidentForm(instance=incident)
    return render(request, 'procellariidae/incident_edit.html', {'form': form})