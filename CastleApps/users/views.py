#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
Users = get_user_model()
from apartments.models import *
from .forms import EditProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render,redirect, reverse

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

@login_required
def editProfile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users/',request.user)

# def editProfile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#
#         if form.is_valid():
#             form.save()
#             return redirect('apartments/1')
#     else:
#         form = EditProfileForm(instance=request.user)
#         context = {'form': form}
#         return render(request, 'users/edit_profile.html', context)
#
#
# # Allows the user to view their own profile
def viewProfile(request, userID=None):
    if userID:

        user = Users.objects.get(pk=userID)
    else:

        user = request.user
    context = {'user': user}
    return render(request, 'users/user_profile.html', context)


# def editProfile(request, userID):
#     if request.method == 'POST':
#         form = EditProfileForm(data=request.POST)
#         if form.is_valid():
#             print("FORM IS VALID")
#             form.save()
#             print("FORM IS SAVED")
#             return redirect('frontpage')
#     form = EditProfileForm(data=request.GET)
#     return render(request, 'users/edit_profile.html', {'form': form})
#
def agents(request):
    # Checks if the person in the Users table is staff
    users = Users.objects.filter(is_staff=True)
    # Simply returns every users that returned true as staff
    # HTML will then loop through the users that are part of the staff and display them
    context = {
        'users': users
    }
    return render(request, 'users/agents.html', context)


#Here you can display a single users
def singleUser(request, userID):

    #print("PRINTINGDSFDSF: ",Locations.objects.all().zip_set)
    #users = Users.objects.get(id = userID)
    #print("Printing all users: ", users)
    user = get_object_or_404(Users, pk=userID)
    #user = Users.objects.get(pk=userID )


    if user.is_staff == False:
        apartments = Apartments.objects.filter(owner_id=userID)
        context = {
            'user': user,
            'apartments': apartments
        }
        return render(request, 'users/user_profile.html', context)
    listingsOfApartments = Listings.objects.filter(agent_id=userID)
    pkOfApps = []
    for x in listingsOfApartments:
        print(x.apartmentid_id)
        pkOfApps.append(x.apartmentid_id)
    apartments = Apartments.objects.filter(id__in=pkOfApps)
    context = {
        'user': user,
        'apartments': apartments
    }
    #Listings.objects.filter(userID)
    return render(request, 'users/single_employee.html', context)

