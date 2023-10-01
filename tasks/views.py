from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def taskView(request):
    return HttpResponse( '<h3> taskview is working </h3>')
