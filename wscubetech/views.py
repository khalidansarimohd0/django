from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request,"about.html")


def homepage(request):
   
    return render(request,"index.html")

def contact(request):
   
    return render(request,"contact.html")

def amazon(request):
   
    return render(request,"amazon.html")