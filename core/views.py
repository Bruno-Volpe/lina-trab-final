from django.shortcuts import render, redirect

def home_view(request):
    # if not logged in, redirect to login page
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'core/home.html')
