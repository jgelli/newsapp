from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, name='nome')
    email = models.EmailField()
    cellphone = models.CharField(max_length=11, name='celular')
    message = models.TextField(max_length=500, name='mensagem')

    
