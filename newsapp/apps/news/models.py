from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelState
from django.utils import timezone

class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='media/%d/%m/%Y')
    published_date = models.DateTimeField(default=timezone.now())
    topic = models.ManyToManyField(Topic)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
