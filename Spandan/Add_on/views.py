from django.shortcuts import render
from django.http import HttpResponse
from Add_on.models import Sport,Team,Match
import ipdb
def index(request):
    return HttpResponse("Hello, You will find spandan schedule here")
def divyanshu(request):
    return HttpResponse("fuck off!")
def allmatch(request):
    matchlist = Match.objects.all()
    return HttpResponse(matchlist)

def homepage(request):
    return render(request , 'Add_on/index.html')
