from django.forms import ModelForm, widgets
from ..models import ListingMiscs


class MiscInfoForm(ModelForm):
    class Meta:
        model = ListingMiscs
        exclude = ['id', 'listingid']
        widgets = {
            'carpreschool': widgets.NumberInput(attrs={'class': 'form-control'}),
            'footpreschool': widgets.NumberInput(attrs={'class': 'form-control'}),
            'carbusstop': widgets.NumberInput(attrs={'class': 'form-control'}),
            'footbusstop': widgets.NumberInput(attrs={'class': 'form-control'}),
            'carsupermarket': widgets.NumberInput(attrs={'class': 'form-control'}),
            'footsupermarket': widgets.NumberInput(attrs={'class': 'form-control'}),
            'carmetro': widgets.NumberInput(attrs={'class': 'form-control'}),
            'footmetro': widgets.NumberInput(attrs={'class': 'form-control'}),
        }
