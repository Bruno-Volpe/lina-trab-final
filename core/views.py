from django.shortcuts import render

def home_view(request):
    # if not logged in, redirect to login page
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    return render(request, 'core/home.html')
