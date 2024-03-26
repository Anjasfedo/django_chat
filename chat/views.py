from django.shortcuts import render
from .models import Room, Message

# Create your views here.

def home(request):
    return render(request, 'home.html')

def room(request, room):
    context = {}
    
    return render(request, 'room.html', context)

def checkview(request):
    context = {}
    
    return render(request, 'template.html', context)
