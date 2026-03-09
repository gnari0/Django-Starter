from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import User, dbEntry
from django.contrib.auth import authenticate, login, logout

def Users(request):
    Users = User.objects.all().values()
    dbEntries = dbEntry.objects.all().values()
    template = loader.get_template('allUsers.html')
    context = {
        'Users': Users,
    }   
    return HttpResponse(template.render(context, request))

def userDetails(request, user_id):
    entries = dbEntry.objects.filter(user=user_id).values()
    userDetails = User.objects.get(id=user_id)
    user = request.user
    template = loader.get_template('userDetails.html')
    context = {
        'user': user,
        'userDetails': userDetails,
        'entries': entries,
    }
    return HttpResponse(template.render(context, request))

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"user: {username}, pass: {password}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f"user login: {username}")
            login(request, user)
            # Redirect to a success page
            return redirect('/')
        else:
            print(f"failed login: {username}")
            # Return an 'invalid login' error message
            # You can add a message here using the messages framework
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
    
def userLogout(request):
    logout(request)
    return redirect('/')

def userSignup(request):
    template = loader.get_template('signup.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def createAccount(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    u = User(username=username, password=password)
    u.save()
    return redirect('/')

def postUserEntry(request):
    title = request.POST.get('title')
    desc = request.POST.get('desc')
    entry = dbEntry(title=title, desc=desc)
    entry.save()