from django.forms import ModelForm, widgets
from ..models import Listings, OpenHouse
# from django import forms


class ListingForm(ModelForm):
    class Meta:
        model = Listings
        exclude = ['id', 'agent_id', 'soldondate', 'apartmentid']
        widgets = {
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'registered': widgets.DateTimeInput(attrs={'type': 'date'})
        }


class OpenHouseForm(ModelForm):
    class Meta:
        model = OpenHouse
        exclude = ['id', 'listingid']
        widgets = {
            'openhousestart': widgets.DateTimeInput(attrs={'type': 'date'}),
            'openhouseend': widgets.DateTimeInput(attrs={'type': 'date'}),

        }
