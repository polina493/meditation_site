from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'core/home.html')

def meditations(request):
    return render(request, 'core/meditations.html')