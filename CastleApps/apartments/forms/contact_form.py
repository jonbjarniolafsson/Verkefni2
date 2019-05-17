from django.forms import  widgets
from ..models import ContactForm
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = ContactForm
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }