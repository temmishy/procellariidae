from django.shortcuts import render

from .models import Incident
from django.utils import timezone

def incidents_list(request):
    incidents = Incident.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'procellariidae/incidents_list.html', {'incidents': incidents})
