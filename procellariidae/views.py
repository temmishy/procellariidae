from django.shortcuts import render

from .models import Incident
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def incidents_list(request):
    incidents = Incident.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'procellariidae/incidents_list.html', {'incidents': incidents})

def incident_detail(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    return render(request, 'procellariidae/incident_detail.html', {'incident': incident})