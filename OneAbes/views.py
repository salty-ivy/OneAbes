from django.shortcuts import render, redirect
from users.models import *
from users.forms import *
from django.contrib import messages

def home(request):
    return render(request,'base.html',)


def signupView(request):
    form = SingupForm()
    if request.method == 'POST':
        form = SingupForm(request.POST)
        print(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('password')==form.cleaned_data.get('confirm_password'):
                user = User.objects.create_user(email=form.cleaned_data.get('email'),password=form.cleaned_data.get('password'))
                user.save()
                profile = Profile.objects.get(user=user)
                profile.name = form.cleaned_data.get('name')
                profile.year = int(form.cleaned_data.get('year'))
                profile.phone = form.cleaned_data.get('phone')
                profile.addminsion_number = form.cleaned_data.get('addminsion_number')
                profile.branch = form.cleaned_data.get('name')
                profile.save()
                messages.success(request,"Account created successfully")
                return redirect('signup-view')
            else:
                messages.danger(request,"Password didn't match")
                return redirect('signup-view')

    context = {'form':form,}
    return render(request,'signup.html',context)