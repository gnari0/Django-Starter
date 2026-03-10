from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def homePage(request):
    filePath = 'djangoStarter/main/templates/ascii.txt'
    txt = ''
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            txt = file.read()
    except Exception as e:
        print(f"error loading ascii: {e}")

    
    context = {
        'ascii': txt,
    }
    #user = request.user
    #print(f"logged user: {user.username}")
    template = loader.get_template('homePage.html')
    return HttpResponse(template.render(context, request))
    #return render(request, 'homePage.html')