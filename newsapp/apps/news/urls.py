from django.urls import path
from news.views import *

urlpatterns = [
    path('', home, name='home'),
    path('noticia/<int:news_id>', news, name='news')

]
