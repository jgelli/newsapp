from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelState
from django.utils import timezone
from .functions import path_and_rename

class Topic(models.Model):
    """
    Model for the news' topic.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class News(models.Model):
    """
    Model for the news.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=path_and_rename)
    published_date = models.DateTimeField(default=timezone.now())
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

