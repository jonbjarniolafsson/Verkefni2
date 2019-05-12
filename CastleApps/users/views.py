#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
Users = get_user_model()

from .forms import UsersCreationForm, EditProfileForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UsersCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request, 'users/register.html', {
        'form': UserCreationForm()
    })


def editProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.users)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {}
    return render(request, 'users/edit_profile.html',args)