   #Remove http.client.HTTPResponse from import and follow:
from django.shortcuts import render
from django.http import HttpResponse

   # Create your views here.
def index(request):
        return HttpResponse("Hello bro")