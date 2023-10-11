from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    return render(request, 'aensonga/about.html')

def blog(request):
    return render(request, 'aensonga/blog.html')

def causes(request):
    return render(request, 'aensonga/causes.html')

def contact(request):
    return render(request, 'aensonga/contact.html')

def donate(request):
    return render(request, 'aensonga/donate.html')

def event(request):
    return render(request, 'aensonga/event.html')

def index(request):
    return render(request, 'aensonga/index.html')

def service(request):
    return render(request, 'aensonga/service.html')

def single(request):
    return render(request, 'aensonga/single.html')

def team(request):
    return render(request, 'aensonga/team.html')

def volunteer(request):
    return render(request, 'aensonga/volunteer.html')