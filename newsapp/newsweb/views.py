from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    news_api_request = requests.get("https://newsapi.org/v2/top-headlines?sources=google-news-br&apiKey=6c3e029bfed541f29941c48c88353900")
    api = json.loads(news_api_request.content)
    return render(request, 'home.html', {'api': api})