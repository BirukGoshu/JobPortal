from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings

from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.index, name='index'),
    path('/about', views.about, name='about'),
    path('/contact', views.contact, name='contact'),
    path('/catagory', views.catagory, name='catagory'),    
]