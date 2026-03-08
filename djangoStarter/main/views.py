from django.shortcuts import render

def homePage(request):
    user = request.user
    print(f"logged user: {user.username}")
    return render(request, 'homePage.html')