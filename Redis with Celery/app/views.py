from django.shortcuts import render
from .task import *
from django.http import HttpResponse

# Create your views here.
def timer(request):
    handle_timer.delay()
    return HttpResponse("The timer is being started")

def write(request):
    to_write.delay()
    return HttpResponse("The Data is being written ")