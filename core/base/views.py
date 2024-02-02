from django.shortcuts import render, redirect
from .models import *
import datetime
import requests
from django.contrib import messages
# Create your views here.
def home(request):
    current_time=datetime.datetime.now()
    quote_url = "https://api.quotable.io/random"
    quote_response = requests.get(quote_url)
    quote_data = quote_response.json()
    random_quote = quote_data.get("content")
    author=quote_data.get("authorSlug")

    context = {'random_quote': random_quote,'current_time': current_time, 'author': author}
    return render(request, 'home.html',context)
def submit_form(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobileno=request.POST.get('mobileno')
        message=request.POST.get('message')
        form_obj=FormData(name=name, email=email, mobileno=mobileno, message=message)
        form_obj.save()
        messages.success(request,"Form submitted successfully")
        return redirect('/')
    return render(request,"home.html")

def about(request):
    context={'datas':FormData.objects.all()}
    
    return render(request,"about.html", context)