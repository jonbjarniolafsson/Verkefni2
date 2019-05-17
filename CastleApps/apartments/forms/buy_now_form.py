from django.forms import ModelForm, widgets
from ..models import PaymentInfos

# from django import forms


# from django.forms import extras

# from django_month_year_widget.widgets import MonthYearWidget

class PaymentInfoForm(ModelForm):
    # add from foreignkey image
    # modelform virkar þannig að þegar það er innsett í templates þá veit það
    # hvernig á að rendera formin sem innihalda alla dálkana

    class Meta:
        model = PaymentInfos
        exclude = ['user_id', 'user', 'isreviewed']
        widgets = {
            # hvernig fields líta út í html
            # attributes on name
            # nafndálkur er input type text og hafa css klasann form-control
            'cardholder': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'cardnumber': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '0000 0000 0000 0000'}),
            'expmonth': widgets.NumberInput(attrs={'class': 'form-control'}),
            'expyear': widgets.NumberInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'ssn': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'aptsuite': widgets.NumberInput(attrs={'class': 'form-control'}),
            # 'user': widgets.TextInput(attrs={'class':'form-control'})
        }
