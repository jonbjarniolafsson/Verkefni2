from django.forms import ModelForm, widgets
from ..models import Apartments, Locations
from django import forms


class CastleAppsCreateForm(ModelForm):
    class Meta:
        image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
        model = Apartments
        exclude = [ 'pkid' ]
        widgets = {
            'RegNumber': widgets.TextInput(attrs={'class' : 'form-control'}),
            'Address': widgets.TextInput(attrs={'class': 'form-control'}),
            'Size': widgets.NumberInput(attrs={'class' : 'form-control'}),
            'Rooms': widgets.NumberInput(attrs={'class' : 'form-control'}),
            'Bathrooms': widgets.NumberInput(attrs={'class' : 'form-control'}),
            'Description': widgets.TextInput(attrs={'class': 'form-control'}),
            'timeOfConstruction': widgets.TextInput(attrs={'class': 'form-control'}),
            'type': widgets.TextInput(attrs={'class':'form-control'})
}