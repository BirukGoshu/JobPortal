from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Job

def index(request):
    # Job.objects.create(position_name=request.POST['position_name'],
    #                    text_description=request.POST['description'], 
    #                    min_age=request.POST['min_age'], 
    #                    max_age=request.POST['max_age'],
    #                    salary=request.POST['salary'], 
    #                    number_of_opening=request.POST['num_of_opening'],)
    
    print(request.POST)
    return render(request, "jobs/index.html")

    