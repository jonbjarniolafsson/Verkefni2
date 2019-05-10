from django.forms import ModelForm, widgets
from ..models import Locations
from django import forms


class AddressCreateForm(ModelForm):
    class Meta:
        model = Locations
        exclude = ['id']
        widgets = {
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'region': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.TextInput(attrs={'class': 'form-control'})
        }