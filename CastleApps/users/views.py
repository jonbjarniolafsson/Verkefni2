from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from users.forms import UsersCreationForm, EditProfileForm


from django.http import HttpResponse
# Create your views here.
from apartments.models import *
from users.models import *
from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth.decorators import login_required



Users = get_user_model()
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
            return redirect('users/', request.user)


def viewProfile(request, userID=None):
    if userID:
        user = Users.objects.get(pk=userID)
    else:

        user = request.user
    context = {'user': user}
    return render(request, 'users/user_profile.html', context)



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


# Here you can display a single users
def singleUser(request, userID):

    user = get_object_or_404(Users, pk=userID)

    if user.is_staff is False:
        apartments = Apartments.objects.filter(owner_id=userID, forsale=True)
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
    apartments = Apartments.objects.filter(id__in=pkOfApps, forsale =True)
    context = {
        'user': user,
        'apartments': apartments
    }
    return render(request, 'users/single_employee.html', context)


def viewHistory(request, userID):
    user = request.user
    if user.id != userID:
        return HttpResponse('Unauthorized', status=401)
    newList = []
    history = ViewHistory.objects.filter(user_id=userID)
    for x in history:
        newList.append(x.apartmentid_id)
    helloGo = Apartments.objects.filter(id__in=newList)[0:6]
    context = {
        'apartments': helloGo
    }
    return render(request, 'users/view_history.html', context)


def ownedApartments(request, userID):
    user = request.user
    if user.id != userID:
        return HttpResponse('Unauthorized', status=401)
    apartments = Apartments.objects.filter(owner_id=userID)
    context = {
        'apartments': apartments
    }
    return render(request, 'users/owned_apartments.html', context)


def managedApartments(request, userID):
    #listings = Listings.objects.filter(agent_id=userID)
    listingsOfApartments = Listings.objects.filter(agent_id=userID)
    pkOfApps = []
    for x in listingsOfApartments:
        print(x.apartmentid_id)
        pkOfApps.append(x.apartmentid_id)
    apartments = Apartments.objects.filter(id__in=pkOfApps, forsale=True)

    context = {
        'apartments': apartments
    }
    print("DSKFDSJFJDSFJDSFJDSF", apartments)
    return render(request, 'users/managed_apartments.html', context)


@login_required
def editProfile(request, userID):
    user = request.user
    if user.id != userID:
        return HttpResponse('Unauthorized', status=401)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('frontpage')
    else:
        form = EditProfileForm(instance=request.user)
        context = {'form': form}
        return render(request, 'users/edit_profile.html', context)


def contactUs(request):
    print("START OF CONTACTUS VIEW FUNCTION")
    if request.method == "POST":
        print("GETTING PARAMS")
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('description')
        print("PRINTING PARAMS", name, email, msg)
        print("POSTING TO DB")
        ContactForm.objects.create(name=name, email=email, description=msg)
        return HttpResponse(status=201)
