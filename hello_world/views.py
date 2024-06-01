from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == "GET":
        return HttpResponse("You must have POSTed something")
    else:
         return HttpResponse(request.method)