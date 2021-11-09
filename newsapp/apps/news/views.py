from django.shortcuts import render, get_object_or_404, redirect
from news.models import News
from django.core.paginator import Paginator
from .functions import paragraph

def home(request):
    news = News.objects.order_by('-published_date').all()
    paginator = Paginator(news, 9)
    page = request.GET.get('page')
    news_per_page = paginator.get_page(page)

    context = {
        'context' : news_per_page
    }

    return render(request, 'news/home.html', context)

def news(request, news_id):

    news = get_object_or_404(News, pk=news_id)
    related_topic = News.objects.order_by('-published_date').filter(topic=news.topic).exclude(pk=news_id)[0:6]
    
    paragraphs = paragraph(news.content)
    show_news = {
        'news' : news,
        'paragraphs' : paragraphs,
        'related' : related_topic
    }


    return render(request, 'news/news.html', show_news)

