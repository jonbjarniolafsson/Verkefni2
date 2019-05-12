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
from django.db.models import Q

# This is the main home page
def home(request):
    context = {
        'apartments': Apartments.objects.all(),
    }
    return render(request, 'apartments/home.html', context)


def buyNow(request, apartmentID):
    context = {
        'apartments' : Apartments.objects.get(id=apartmentID)
    }
    return render(request, 'apartments/buy_now.html')

# This is
def agents(request):

    users = Users.objects.filter(is_staff = True)
    #print("PRINTING ALL THE USERS : ", users.profileImagePath)
    context = {
       'agents': users
    }
    return render(request, 'apartments/agents.html', context)

def pureApartment(request):
    context = {
        'apartments': Apartments.objects.all(),
    }

    return render(request, 'apartments/pure-apartments.html', context)

def aboutus(request):
    context = {
        'oliver':'oliver'
    }
    return render(request, 'apartments/about_us.html', context)

# This is the page you are led to when an apartment is clicked on
def singleApartment(request, apartmentID): # Need to add error handling
    context = {}
    print("ERROR HANDLING" ,apartmentID)
    if Apartments.objects.get(id=apartmentID).id == apartmentID:
        #print("HEre we are", apartmentid)
        apartments = Apartments.objects.get(id = apartmentID)
        apartmentImages = Apartments.objects.get(pk=apartmentID).apartmentimages_set.all()
        apartmentImages = apartmentImages.all()
        listings = Listings.objects.filter(apartmentid=apartmentID)
        #print("LISTING OBJECT: ", listings)
        idOfActiveListing = listings.aggregate(Max('id'))
        print(idOfActiveListing)
        listing = Listings.objects.get(id = idOfActiveListing['id__max'])
        print(listing)
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

def create_location(request):
    if request.method == 'POST':
        address_form = AddressCreateForm(data=request.POST, prefix='location')
        if address_form.is_valid():
            print("VALID")
            address_form.save()
            return redirect('create-apartment')
        context = {'address_form': address_form}
        f = AddressCreateForm(data)
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



def search_apartment(request):
    searchString = request.GET.get("search")
    checkingLocation = Locations.objects.filter(Q(country__country__icontains=searchString) | Q(zip__icontains=searchString) | Q(region__icontains=searchString) | Q(city__icontains=searchString))
    checkingListings = Listings.objects.filter(Q(description__icontains=searchString))
    checkingApartments = Apartments.objects.filter(Q(registration__icontains=searchString) | Q(address__icontains=searchString) | Q(aptsuite__icontains=searchString))
    apps = Apartments.objects.filter(Q(locationid__in = checkingLocation) | Q(id__in =checkingListings) | Q(id__in =checkingApartments))

    context = {
        'apartments' : apps
    }

    
    return render(request, "apartments/search-results.html", context)


def returnType(string):
    return type(string)