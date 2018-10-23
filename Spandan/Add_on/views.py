from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, You will find spandan schedule here")
def divyanshu(request):
    return HttpResponse("fuck off!")
