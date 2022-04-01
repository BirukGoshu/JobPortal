from django.shortcuts import render
from django.http import HttpResponse

class IndexView(generic.ListView):
    return HttpResponse("candidate page comming soon")

