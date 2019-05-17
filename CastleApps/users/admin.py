# from django.contrib import admin

# users/admin.py
from django.contrib import admin
# from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UsersCreationForm, EditProfileForm
from .models import Users


class CustomUserAdmin(UserAdmin):
    model = Users
    add_form = UsersCreationForm
    form = EditProfileForm
    list_display = ['email', 'username']


admin.site.register(Users, CustomUserAdmin)
