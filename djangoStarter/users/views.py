from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User, dbEntry

def Users(request):
    Users = User.objects.all().values()
    template = loader.get_template('allUsers.html')
    context = {
        'Users': Users,
        'dbEntries': dbEntry.objects.all().values(),
    }   
    return HttpResponse(template.render(context, request))