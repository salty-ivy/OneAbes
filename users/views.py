from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url="signin-view")
def profileView(request, uid):
    profile = Profile.objects.get(user=User.objects.get(uid=uid))
    context = {
        'profile':profile,
        'is_editable':True if request.user==profile.user else False,
    }
    return render(request,'users/profile.html',context)
