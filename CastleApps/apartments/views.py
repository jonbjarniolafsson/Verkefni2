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

from .forms import buynowform

from django.db.models import Q




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

        #listings = Listings.objects.all()
        #print("PRINT STATEMENT: ", Listings.apartmentid)
        newList = []

        for x in OpenHouse.objects.all():
            #appID = x.listingid.apartmentid
            print(x.listingid.apartmentid.id)
            newList.append(x.listingid.apartmentid.id)
        newList = set(newList)
        newList = list(newList)

        newApart = Apartments.objects.filter(pk__in=newList)


        context = {
            'listings': Listings.objects.all(),
            'apartments' : newApart,
            #'appID': appID
        }
        return render(request, 'apartments/home.html', context)


def buyNow(request, apartmentID):
    context = {
        'apartment' : Apartments.objects.get(id=apartmentID)
    }
    return render(request, 'apartments/buy_now.html', context)


def buyNowSubmitss(request, apartmentID):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = buynowform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return buynowform('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = 'empty'

    return render(request, 'apartments/purchase_status.html', {'form': form})

# This is
def agents(request):

    users = Users.objects.filter(is_staff = True)
    #print("PRINTING ALL THE USERS : ", users.profileImagePath)
    context = {
       'agents': users
    }
    return render(request, 'apartments/agents.html', context)

def aboutus(request):
    context = {
        'oliver':'oliver'
    }
    return render(request, 'apartments/about_us.html', context)

# This is the page you are led to when an apartment is clicked on
def singleApartment(request, apartmentID): # Need to add error handling
    context = {}

    print("Print machine :",Locations.objects.filter(country_id= 'Iceland', zip = '108'))

    if Apartments.objects.get(id=apartmentID).id == apartmentID:
        #print("HEre we are", apartmentid)
        apartments = Apartments.objects.get(id = apartmentID)
        apartmentImages = Apartments.objects.get(pk=apartmentID).apartmentimages_set.all()
        apartmentImages = apartmentImages.all()
        listings = Listings.objects.filter(apartmentid=apartmentID)

        idOfActiveListing = listings.aggregate(Max('id'))

        listing = Listings.objects.get(id = idOfActiveListing['id__max'])

        #print("PRINTING agentID: ", listing.agentID_id)
        listingAgent = Users.objects.get(id = listing.agent_id)
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



def buyNowSubmit(request):
    if request.method == 'POST':
        address_form = AddressCreateForm(data=request.POST, prefix='location')
        if address_form.is_valid(): #Built in to check if valid
            print("VALID")
            address_form.save() #Saves to the DB
            return redirect('create-apartment') #Supposed to redirect to create apartment
        context = {'address_form': address_form}
        f = AddressCreateForm(data=request.POST)
        f.non_field_errors()
        field_errors = [(field.label, field.errors) for field in f]
        return render(request, 'apartments/create-location.html', context)
    else:
        address_form = AddressCreateForm(data=request.GET)
        return render(request, 'apartments/create-location.html', {
            'address_form': address_form
        })


def create_location(request):
    if request.method == 'POST':
        address_form = AddressCreateForm(data=request.POST, prefix='location')
        if address_form.is_valid(): #Built in to check if valid
            print("VALID")
            address_form.save() #Saves to the DB
            return redirect('create-apartment') #Supposed to redirect to create apartment
        context = {'address_form': address_form}
        f = AddressCreateForm(data=request.POST)
        f.non_field_errors()
        field_errors = [(field.label, field.errors) for field in f]
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
            print("VALID")
            app_form.save()
            return redirect('frontpage')

        context = {'app_form': app_form}
        print("INVALID")
        return render(request, 'apartments/create-apartment.html', context)
    else:
        app_form = CastleAppsCreateForm(data=request.GET)
        return render(request, 'apartments/create-apartment.html', {
            'app_form': app_form
        })