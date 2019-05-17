from django.forms import ModelForm, widgets, Select
from ..models import PaymentInfos

from django import forms


# from django.forms import extras

# from django_month_year_widget.widgets import MonthYearWidget

class PaymentInfoForm(ModelForm):
    # add from foreignkey image
    # modelform virkar þannig að þegar það er innsett í templates þá veit það
    # hvernig á að rendera formin sem innihalda alla dálkana

    class Meta:
        MONTHS = [
            ('', 'month of expiration'),
            ('January', '01 January'),
            ('February', '02 February'),
            ('March', '03 March'),
            ('April', '04 April'),
            ('May', '05 May'),
            ('June', '06 June'),
            ('July', '07 July'),
            ('August', '08 August'),
            ('September', '09 September'),
            ('October', '10 October'),
            ('November', '11 November'),
            ('December', '12 December'),
        ]
        YEARS = [
            ('', 'year of expiration'),
            ('2019','19'),
            ('2020', '20'),
            ('2021', '21'),
            ('2022', '22'),
            ('2023', '23'),
            ('2024', '24'),
            ('2025', '25'),
            ('2026', '26'),
        ]
        model = PaymentInfos
        exclude = ['user_id', 'user', 'isreviewed']
        widgets = {
            # hvernig fields líta út í html
            # attributes on name
            # nafndálkur er input type text og hafa css klasann form-control
            'cardholder': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'cardnumber': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '0000 0000 0000 0000'}),
            'expmonth': widgets.Select(choices=MONTHS,attrs={'class': 'form-control', 'placeholder': '0000 0000 0000 0000'}),
            'expyear': widgets.Select(choices=YEARS, attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'ssn': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'aptsuite': widgets.NumberInput(attrs={'class': 'form-control'}),
            # 'user': widgets.TextInput(attrs={'class':'form-control'})
        }
