from django.shortcuts import render
from djangohttp import HttpResponse
# Create your views here.
def index(request):
    saludo = "Hola mundo"
    return HttpResponse(saludo)