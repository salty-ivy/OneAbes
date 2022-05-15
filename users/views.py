from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.contrib.auth.decorators import login_required


@login_required(login_url="signin-view")
def profileView(request, uid):
    return render(request,'users/profile.html')
