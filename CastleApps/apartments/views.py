from django.shortcuts import render,redirect
from .forms.apartmentform import CastleAppsCreateForm
from .forms.locationform import AddressCreateForm
#from .forms.signup_form import CastleAppsSignupForm
from django.http import HttpResponse
# Create your views here.
from apartments.models import *
from users.models import *
from django.db.models import Max
from django.shortcuts import get_object_or_404



apartments = [
    {
        'aid': '123',
        'address': 'Lindarberg 26',
        'city': 'Hafnarfjörður',
        'zip': '221',
        'country': 'Iceland',
        'size': '250',
        'rooms': '6',
        'price': '50000000',
        'type': 'Villa',
        'image': '/static/img/b70.jpeg'
    },
    {
        'aid': '124',
        'address': 'Miðvangur 56',
        'city': 'Hafnarfjörður',
        'zip': '220',
        'country': 'Iceland',
        'size': '230',
        'rooms': '3',
        'price': '73000000',
        'type': 'Penthouse apartment',
        'image': '/static/img/b70.jpeg'
    },
    {
        'aid': '125',
        'address': 'Skuggagata 56',
        'city': 'Reykjavík',
        'zip': '101',
        'country': 'Iceland',
        'size': '500',
        'rooms': '10',
        'price': '12000000',
        'type': 'Penthouse apartment',
        'image': '/static/img/b70.jpeg'
    },
    {
        'aid': '126',
        'address': 'Bergstaðastræti 70',
        'city': 'Reykjavík',
        'zip': '101',
        'country': 'Iceland',
        'size': '100',
        'rooms': '2',
        'price': '150000000',
        'type': 'Luxury Lodge',
        'image': '/static/img/b70.jpeg'
    }
]

# This is the main home page
def home(request):
    context = {
        'apartments': Apartments.objects.all(),
    }
    return render(request, 'apartments/home.html', context)


# This is
def agents(request):

    users = Users.objects.filter(is_superuser = True)
    #print("PRINTING ALL THE USERS : ", users.profileImagePath)
    context = {
       'agents': users
    }
    return render(request, 'apartments/agents.html', context)

# This is the page you are led to when an apartment is clicked on
def singleApartment(request, apartmentID): # Need to add error handling
    context = {}
    print("ERROR HANDLING" ,apartmentID)
    if Apartments.objects.get(id=apartmentID).id == apartmentID:
        #print("HEre we are", apartmentid)
        apartments = Apartments.objects.get(id = apartmentID)
        apartmentImages = Apartments.objects.get(pk=apartmentID).apartmentimages_set.all()
        apartmentImages = apartmentImages.all()
        listings = Listings.objects.filter(apartment=apartmentID)
        print("LISTING OBJECT: ", listings)
        idOfActiveListing = listings.aggregate(Max('id'))
        listing = Listings.objects.get(id = idOfActiveListing['id__max'])
        print("PRINTING agentID: ", listing.agentID_id)
        listingAgent = Users.objects.get(id = listing.agentID_id)
        context = {
            'apartment': apartments,
            'images' : apartmentImages,
            'agent': listingAgent
        }
    return render(request, 'apartments/single-apartment.html', context)



#Here you can display a single user
def singleUser(request, userID):
    #user = Users.objects.get(id = userID)
    #print("Printing all users: ", user)
    user = get_object_or_404(Users, pk=userID)
    context = {
        'user': user
    }
    return render(request, 'apartments/single_user.html', context)



def all_apartments(request):
    context = {
        'apartments': apartments
    }
    return render(request, 'apartments/apartments-list.html', context)

def create_location(request):
    if request.method == 'POST':
        address_form = AddressCreateForm(data=request.POST, prefix='location')
        if address_form.is_valid():
            address_form.save()
            return redirect('create-apartment')
        context = {'address_form': address_form}
        return render(request, 'apartments/create-location.html', context)
    else:
        address_form = AddressCreateForm(data=request.GET)
        return render(request, 'apartments/create-location.html', {
            'address_form': address_form
        })

def create_apartment(request):
    if request.method == 'POST':
        # Read data from apartments form, and from address form.
        app_form = CastleAppsCreateForm(data=request.POST, prefix='apartment')
        if app_form.is_valid():
            app_form = app_form.save()
            return redirect('frontpage')

        context = {'app_form': app_form}
        return render(request, 'apartments/create-apartment.html', context)
    else:
        app_form = CastleAppsCreateForm(data=request.GET)
        return render(request, 'apartments/create-apartment.html', {
            'app_form': app_form
        })