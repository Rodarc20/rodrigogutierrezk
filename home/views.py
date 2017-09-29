from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home/home.html')
    #return HttpResponse("I'm Rodrigo Gutierrez Kasparette.")

# Create your views here.
