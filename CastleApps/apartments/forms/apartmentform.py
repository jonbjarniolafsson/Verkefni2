from django.forms import ModelForm, widgets
from ..models import Apartments, Locations
from django import forms


class CastleAppsCreateForm(ModelForm):
    class Meta:
        image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
        model = Apartments
        exclude = [ 'id' ]
        widgets = {

            'registration': widgets.TextInput(attrs={'class' : 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'aptsuite': widgets.TextInput(attrs={'class': 'form-control'}),
            'size': widgets.NumberInput(attrs={'class' : 'form-control'}),
            'rooms': widgets.NumberInput(attrs={'class' : 'form-control'}),
            'bathrooms': widgets.NumberInput(attrs={'class' : 'form-control'}),
            'timeofconstruction': widgets.TextInput(attrs={'class': 'form-control'}),
            'type': widgets.TextInput(attrs={'class':'form-control'})

}


class EditAppForm(ModelForm):
    class Meta:
        model = Apartments
        exclude = ['id']
        widgets = {
            'registration': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'aptsuite': widgets.TextInput(attrs={'class': 'form-control'}),
            'size': widgets.NumberInput(attrs={'class': 'form-control'}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'bathrooms': widgets.NumberInput(attrs={'class': 'form-control'}),
            'timeofconstruction': widgets.TextInput(attrs={'class': 'form-control'}),
            'type': widgets.TextInput(attrs={'class': 'form-control'})
        }

