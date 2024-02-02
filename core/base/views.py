from django.shortcuts import render
import datetime
import requests
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