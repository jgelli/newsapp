from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('news/<int:news_id>', news, name='news')

]
