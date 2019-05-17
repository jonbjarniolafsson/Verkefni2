from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users
from apartments.models import ContactForm
from django.forms import ModelForm, widgets


class UsersCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Users  # this is the "YourCustomUser" that you imported at the top of the file
        fields = ('username', 'email')  # etc etc, other fields you want displayed on the form)


class ContactUs(ModelForm):
    class Meta(UserCreationForm):
        model = ContactForm
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'message': widgets.Textarea(attrs={'class': 'form-control'})
        }


class EditProfileForm(ModelForm):
    class Meta:
        model = Users
        image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
        exclude = ['id', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups',
                   'user_permissions']
        widgets = {
            'password': widgets.TextInput(attrs={'class': 'form-control'}),
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'workplace': widgets.TextInput(attrs={'class': 'form-control'})

        }
