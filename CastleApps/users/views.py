#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
Users = get_user_model()

from users.forms import UsersCreationForm, EditProfileForm

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
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('apartments/1')
    else:
        form = EditProfileForm(instance=request.user)
        context = {'form': form}
        return render(request, 'users/edit_profile.html', context)


# Allows the user to view their own profile
def viewProfile(request, userID=None):
    if userID:

        user = Users.objects.get(pk=userID)
    else:

        user = request.user
    context = {'user': user}
    return render(request, 'apartments/single_user.html', context)