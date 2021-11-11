from django.db import models
from functions import path_and_rename_ads

class Advertising(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    image = models.ImageField(upload_to=path_and_rename_ads)

