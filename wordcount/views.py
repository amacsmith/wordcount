from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'hithere':'This is me'})

def count(request):
    return render(request, 'count.html')