from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'portfolio/home.html')

def contact(request):
    return render(request,'portfolio/contact.html')    

# Create your views here.
