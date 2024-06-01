from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'core/home.html')

def meditations(request):
    return render(request, 'core/meditations.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})