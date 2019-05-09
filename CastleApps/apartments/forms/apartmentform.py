from django.forms import ModelForm, widgets
from ..models import Apartments
from django import forms


class CastleAppsCreateForm(ModelForm):
    class Meta:
        image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
        model = Apartments
        exclude = [ 'pkid', 'locationID' ]
        widgets = {
            'RegNumber': widgets.TextInput(attrs={'class' : 'form-control'}),
            'Address': widgets.TextInput(attrs={'class': 'form-control'}),
            'Zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'Size': widgets.NumberInput(attrs={'class' : 'form-control'}),
            'Rooms': widgets.NumberInput(attrs={'class' : 'form-control'}),
            'Bathrooms': widgets.NumberInput(attrs={'class' : 'form-control'}),
            'Type': widgets.TextInput(attrs={'class' : 'form-control'}),
            'Description': widgets.TextInput(attrs={'class': 'form-control'}),
            'Time of Construction': widgets.TextInput(attrs={'class' : 'form-control'}),
            'Registered': widgets.DateTimeInput(attrs={'class' : 'form-control'}),
            'Price': widgets.NumberInput(attrs={'class': 'form-control'}),

}