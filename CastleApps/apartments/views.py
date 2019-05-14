
from .forms.apartmentform import CastleAppsCreateForm
from .forms.locationform import AddressCreateForm
# from .forms.signup_form import CastleAppsSignupForm
from django.http import HttpResponse
# Create your views here.
from apartments.models import *
from users.models import *
from django.db.models import Max
from django.shortcuts import get_object_or_404,render,redirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import auth, Permission


from .forms import buynowform

from django.db.models import Q

from datetime import datetime
from django.utils import timezone



def home(request):

        openHouse =  OpenHouse.objects.all()


        newList = []
        # Context has to be a dictionary
        context = {}
        for x in range(0,len(OpenHouse.objects.all()) +1):
            # NEed to make sure the filter doesn't return empty or it crashes
            if len(openHouse.filter(id=x)) != 0:
                # We are comparing the date in our timezone vs the date coming from the database
                if timezone.now() < openHouse.get(id = x).openhousestart:
                    #We know for sure it exists, now we need access to the object
                    y = OpenHouse.objects.get(id=x)
                    #Make a new list of all the apartments that have open houses scheduled in the future
                    newList.append(y.listingid.apartmentid.id)
                    newList = set(newList)
                    newList = list(newList)
                    # We ask the DB to return all the apartments in the list that match
                    newApart = Apartments.objects.filter(pk__in=newList)
                    context = {
                        'apartments' : newApart, # Send all the apartments
                    }

        return render(request, 'apartments/home.html', context)


def buyNow(request, apartmentID):
    context = {
        'apartment': Apartments.objects.get(id=apartmentID)
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
    # Checks if the person in the Users table is staff
    users = Users.objects.filter(is_staff = True)
    # Simply returns every users that returned true as staff
    # HTML will then loop through the users that are part of the staff and display them
    context = {
        'agents': users
    }
    return render(request, 'apartments/agents.html', context)
    

def aboutus(request):
    context = {
        'oliver': 'oliver'
    }
    return render(request, 'apartments/about_us.html', context)


# This is the page you are led to when an apartment is clicked on
def singleApartment(request, apartmentID):  # Need to add error handling
    context = {}

    print("Print machine :",Locations.objects.filter(country_id= 'Iceland', zip = '108'))

    if Apartments.objects.get(id=apartmentID).id == apartmentID:
        # print("HEre we are", apartmentid)
        apartments = Apartments.objects.get(id=apartmentID)
        apartmentImages = Apartments.objects.get(pk=apartmentID).apartmentimages_set.all()
        apartmentImages = apartmentImages.all()
        listings = Listings.objects.filter(apartmentid=apartmentID)

        idOfActiveListing = listings.aggregate(Max('id'))

        listing = Listings.objects.get(id = idOfActiveListing['id__max'])

        #print("PRINTING agentID: ", listing.agentID_id)
        listingAgent = Users.objects.get(id = listing.agent_id)
        context = {
            'apartment': apartments,
            'images': apartmentImages,
            'agent': listingAgent
        }
    return render(request, 'apartments/single-apartment.html', context)



#Here you can display a single users
def singleUser(request, userID):
    #users = Users.objects.get(id = userID)
    #print("Printing all users: ", users)
    user = get_object_or_404(Users, pk=userID)
    context = {
        'users': user
    }
    return render(request, 'apartments/single_user.html', context)


def all_apartments(request):
    context = {
        'apartments' : Apartments.objects.all()
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
    currentUser = request.user
    if currentUser.id == None or currentUser.is_staff == False:
        return HttpResponse('Unauthorized', status=401)
    if request.method == 'POST':
        address_form = AddressCreateForm(data=request.POST, prefix='location')
        if address_form.is_valid(): #Built in to check if valid
            address_form.save() #Saves to the DB
            return redirect('create-apartment') #Supposed to redirect to create apartment
        context = {'address_form': address_form}
        return render(request, 'apartments/create-location.html', context)
    else:
        address_form = AddressCreateForm(data=request.GET, prefix='location')
        return render(request, 'apartments/create-location.html', {
            'address_form': address_form
        })


def create_apartment(request):
        currentUser = request.user
        if currentUser.id == None or currentUser.is_staff == False:
            return HttpResponse('Unauthorized', status=401)
        if request.method == 'POST':
            # Read data from apartments form, and from address form.
            app_form = CastleAppsCreateForm(data=request.POST, prefix='apartment')
            if app_form.is_valid():
                app_form.save()
                return redirect('frontpage')
            context = {'app_form': app_form}
            return render(request, 'apartments/create-apartment.html', context)
        else:
            app_form = CastleAppsCreateForm(data=request.GET, prefix='apartment')
            return render(request, 'apartments/create-apartment.html', {
                'app_form': app_form
            })



def search_apartment(request):
    searchString = request.GET.get("search")
    zipCode = request.GET.get("zip")

    if zipCode != None:
        apartments = Apartments.objects.filter(Q(locationid__zip=zipCode))
        apartments = apartments.filter(Q(address__icontains=searchString) | Q(type__icontains=searchString) | Q(locationid__city__icontains=searchString) | Q(locationid__region__icontains=searchString))
    else:
        apartments = Apartments.objects.filter(Q(address__icontains=searchString) | Q(type__icontains=searchString) | Q(locationid__zip__icontains=searchString) | Q(locationid__city__icontains=searchString) | Q(locationid__region__icontains=searchString) | Q(locationid__country_id__country__icontains=searchString))
    
    apps = {
        'apartments' : apartments
    }

    if searchString == None and zipCode == None:
        return render(request, "apartments/search-results.html")
    else:
        return render(request, "apartments/search-results.html", apps)




# def search_apartment(request):
#     #Getting the string that is being searched
#     searchString = request.GET.get("search")
#     zipCode = request.GET.get("zip")

#     #First we filter everything in the search string by location. SELECT * FROM Locations L WHERE x OR y OR Z OR M
#     checkingListings = Listings.objects.filter(Q(description__icontains=searchString))
#     checkingApartments = Apartments.objects.filter(Q(registration__icontains=searchString) | Q(address__icontains=searchString) | Q(aptsuite__icontains=searchString) | Q(type__icontains=searchString))
#     records = checkingListings | checkingApartments
#     if zipCode != None:
#         checkingLocation = Locations.objects.filter(Q(zip__icontains=zipCode)).filter(Q(country__country__icontains=searchString) | Q(region__icontains=searchString) | Q(city__icontains=searchString))
#     else:
#         checkingLocation = Locations.objects.filter(Q(country__country__icontains=searchString) | Q(zip__icontains=searchString) | Q(region__icontains=searchString) | Q(city__icontains=searchString))

#     # Now we have the 3 main tables that we need to check and so we do the same except now we check if the APID is in the QueryStrings
#     apps = Apartments.objects.filter(Q(locationid__in = checkingLocation) | Q(id__in =checkingListings) | Q(id__in =checkingApartments))
#     context = {
#         'apartments' : apps
#     }



#     if searchString == None and zipCode == None:
#         return render(request, "apartments/search-results.html")
#     else:
#         return render(request, "apartments/search-results.html", context)