from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


def create_user(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        User.objects.create_user(name, email, password)
    return render(request, "index.html")


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
        else:
            return render(request, 'index.html',)


@login_required
def log_out(request):
    logout(request)
    return render(request, "index.html")
