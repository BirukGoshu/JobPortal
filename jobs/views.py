from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User,auth

from .models import Job

def index(request):
    # print(request.POST)
    return render(request, "jobs/index.html")

def post_job(request):
    if request.method == 'POST':
        print(request.user)
        if request.user is not 'WSGIRequest':
            user = auth.authenticate(username=request.user)
            # auth.login(request, request.user)
            Job.objects.create(position_name=request.POST['position_name'],
                            text_description=request.POST['description'], 
                            min_age=request.POST['min_age'], 
                            max_age=request.POST['max_age'],
                            salary=request.POST['salary'], 
                            number_of_opening=request.POST['num_of_opening'],
                            creater = request.user,)
            messages.info(request, 'job posted successfully')
            return render(request,'jobs/post_job.html')
        else:
            messages.info(request, 'please login first')
            return redirect('jobs/login.html')
    else:
        return render(request,'jobs/post_job.html')
    
def login(request):
    # return render(request,'jobs/login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'login successfully')
            return redirect("/")
        else:
            messages.info(request,'Invalid credentials entered')
            return redirect('login.html')
        
    else:
        return render(request,'jobs/login.html')
    
def Logout(request):
    return redirect('index')

def about(request):
    return render(request, 'jobs/about.html')

def contact(request):
    return render (request, 'jobs/contact.html')

def category(request):
    return render(request, 'jobs/category.html')