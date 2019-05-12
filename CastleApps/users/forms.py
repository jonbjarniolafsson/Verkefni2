# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users
#from django.contrib.auth import get_user_model
#Users = get_user_model()

class UsersCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Users #this is the "YourCustomUser" that you imported at the top of the file
        fields = ('username', 'email') #etc etc, other fields you want displayed on the form)



class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = Users
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )
