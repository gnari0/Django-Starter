from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import User, dbEntry
from django.contrib.auth import authenticate, login

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

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            return redirect('home')
        else:
            # Return an 'invalid login' error message
            # You can add a message here using the messages framework
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')