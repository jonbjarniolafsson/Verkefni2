from django.forms import ModelForm, widgets
from ..models import Listings
from django import forms


class ListingForm(ModelForm):
    class Meta:
        model = Listings
        exclude = ['id', 'agent_id']
        widgets = {
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'registered': widgets.DateTimeInput(attrs={'type': 'date'}),
            'soldondate': widgets.DateTimeInput(attrs={'type': 'date'})
        }
