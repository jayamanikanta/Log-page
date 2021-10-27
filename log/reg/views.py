from django.shortcuts import render
from django.http import HttpResponse, request
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls.conf import path
from reg.forms import logform
from .models import logpage
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout as logouts

# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form=logform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/login')
            except:
                pass
    else:
        form = logform()
    return render(request,'signup.html',{'form':form})

  

def login(request):
    my_sql=logpage.objects.all()
    if request.method=='POST':
        for i in my_sql:

            if request.POST['email']==i.email and request.POST['password']==i.password:
                return render(request,'user.html', {'i':i})
        else:
            messages.info(request,'invalid input')
        return redirect('login')
    return render(request,'login.html')

def user(request):
    logouts(request)
    return redirect('home')

def user_del(request,id):
    data=logpage.objects.get(id=id)
    data.delete()
    return render(request,'user.html')

def edit(request,id):
    if request.method == "POST":
        data = logpage.objects.get(id=id)

        form = logform(request.POST or None,instance=data)
        print(form)
        if form.is_valid():
            form.save()
            print(form)
        return redirect('user')
    else:
        data=logpage.objects.get(id=id)
        return render(request,'edit.html',{'data':data})













