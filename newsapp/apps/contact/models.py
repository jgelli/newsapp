from django.db import models

class Contact(models.Model):
    """ Model for get in tounch """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cellphone = models.CharField(max_length=11)
    message = models.TextField(max_length=1000)

    
