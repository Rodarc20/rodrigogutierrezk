from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("I'm Rodrigo Gutierrez Kasparette.")

# Create your views here.
