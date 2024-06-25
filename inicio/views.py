from django.shortcuts import render 
from datetime import datetime

def inicio (request):
    return render (request, 'inicio/index.html')
