from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User,auth

from .models import Job

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request, user)
            Job.objects.create(position_name=request.POST['position_name'],
                            text_description=request.POST['description'], 
                            min_age=request.POST['min_age'], 
                            max_age=request.POST['max_age'],
                            salary=request.POST['salary'], 
                            number_of_opening=request.POST['num_of_opening'],)
            messages.info(request, 'job posted successfully')
        else:
            messages.info(request,"invalid credentials")
            return render(request,'jobs/index.html')
    else:
        return render(request,'jobs/index.html')
        
    print(request.POST)
    return render(request, "jobs/index.html")

    
