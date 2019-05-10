from django.forms import ModelForm, widgets
from ..models import Apartments
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
            'timeOfConstruction': widgets.TextInput(attrs={'class': 'form-control'})



}
        #address = models.CharField(max_length = 50)
        #size = models.IntegerField()
        #rooms = models.IntegerField()
        #bathrooms = models.IntegerField()
        #type = models.CharField(max_length=200)
        #timeOfConstruction = models.IntegerField()
        #displayImage = models.CharField(max_length = 5000)
        #location = models.ForeignKey(Locations, on_delete=models.CASCADE)