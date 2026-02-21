from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import dbEntry

def dbEntries(request):
    dbEntries = dbEntry.objects.all().values()
    template = loader.get_template('allEntries.html')
    context = {
        'dbEntries': dbEntries,
    }
    return HttpResponse(template.render(context, request))