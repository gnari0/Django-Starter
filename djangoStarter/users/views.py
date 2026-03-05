from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User, dbEntry

def Users(request):
    Users = User.objects.all().values()
    dbEntries = dbEntry.objects.all().values()
    template = loader.get_template('allUsers.html')
    context = {
        'Users': Users,
        'dbEntries': dbEntries,
    }   
    return HttpResponse(template.render(context, request))

def userDetails(request, user_id):
    entries = dbEntry.objects.filter(user=user_id).values()
    user = User.objects.get(id=user_id)
    template = loader.get_template('userDetails.html')
    context = {
        'user': user,
        'entries': entries,
    }
    return HttpResponse(template.render(context, request))