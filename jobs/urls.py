from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings

from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('catagory', views.category, name='category'),  
    path('login', views.login, name='login'),
    path('post_job', views.post_job, name='post_job'),
    path('logout', views.logout, name='logout'),
]