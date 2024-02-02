from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name='home'),
    path('submit_form/', submit_form, name='submit_form'),  
    path('about/',about, name='about'),
]
