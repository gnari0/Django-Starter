from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import dbEntry
from .models import User

def dbEntries(request):
    dbEntries = dbEntry.objects.all().values()
    template = loader.get_template('allEntries.html')
    context = {
        'dbEntries': dbEntries,
    }
    return HttpResponse(template.render(context, request))

def Users(request):
    Users = User.objects.all().values()
    template = loader.get_template('allEntries.html')
    context = {
        'Users': Users,
    }
    return HttpResponse(template.render(context, request))