from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelState
from django.utils import timezone
from uuid import uuid4
import os

class Topic(models.Model):
    """
    Model for the news' topic.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

def path_and_rename(instance, filename):
    """
    Rename the image from news and return the path.
    """
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class News(models.Model):
    """
    Model for the news.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=path_and_rename)
    published_date = models.DateTimeField(default=timezone.now())
    topic = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title

