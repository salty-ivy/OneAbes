from django.shortcuts import render, redirect
from users.models import *
from users.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def timeline(request):
    return render(request,'timeline.html',)


def signupView(request):
    form = SingupForm()
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('password')==form.cleaned_data.get('confirm_password'):
                user = User.objects.create_user(email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password'))
                user.save()
                profile = Profile.objects.get(user=user)
                profile.name = form.cleaned_data.get('name')
                profile.year = int(form.cleaned_data.get('year'))
                profile.phone = form.cleaned_data.get('phone')
                profile.addminsion_number = form.cleaned_data.get('addmision_number')
                profile.branch = form.cleaned_data.get('name')
                profile.save()
                messages.success(request,"Account created successfully")
                return redirect('timeline-view')
            else:
                messages.danger(request,"Password didn't match")
                return redirect('signup-view')

    context = {'form':form,}
    return render(request,'signup.html',context)


def signinView(request):
    form = SigninForm()
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(username=email,password=password)

            if user is not None:
                login(request,user)
                messages.success(request,f"Login successful, wlecome {user.profile.name}")
                return redirect("timeline-view")
            else:
                messages.warning(request,f'Incorrect credentials')
                return redirect('signin-view')
    context = {
        'form':form,
    }
    return render (request,'signin.html',context)

def signoutView(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            logout(request)
            return redirect('timeline-view')

