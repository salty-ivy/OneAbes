from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def clubView(request):
    return HttpResponse(" <h3> clubview is working </h3>")