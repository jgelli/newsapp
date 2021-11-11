from django import forms
from django.forms import ModelForm
from django.forms import widgets
from contact.models import Contact
from .validation import *

class ContactForms(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {'name':'Nome', 'cellphone':'Celular', 'message':'Mensagem'}



    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        cellphone = cleaned_data.get('cellphone')

        if (cellphone):
            cellphone_has_letter(self, cellphone)
            cellphone_length(self, cellphone)