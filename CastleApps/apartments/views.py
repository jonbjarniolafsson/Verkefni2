from django.shortcuts import render,redirect

# This document will act as our controller in our Apartments app. The main magic happens here.

from .forms.buy_now_form import PaymentInfoForm
from .forms.apartment_form import CastleAppsCreateForm,EditAppForm
from .forms.location_form import AddressCreateForm
from .forms.listing_form import ListingForm
# from .forms.signup_form import CastleAppsSignupForm
from django.http import HttpResponse
# Create your views here.
from apartments.models import *
from users.models import *
from django.db.models import Max
from django.shortcuts import get_object_or_404,render,redirect



from .forms import buy_now_form

from django.db.models import Q

from datetime import datetime
from django.utils import timezone

def home(request):

        #listing = Listings.objects.get(id=1)
        #print(listing.shortMortgage)
        newUser = request.user.id
        print(newUser)

        openHouse =  OpenHouse.objects.all()

        newList = []
        # Context has to be a dictionary
        context = {}
        newApart = ''
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

        newlyListed = Listings.objects.all().order_by('registered')
        apps = Apartments.objects.filter(pk__in=newlyListed)
        companyInfo = CompanyInformation.objects.all()
        context = {
            'apartments': newApart,  # Send all the apartments
            'newlyListed': apps,
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
        form = buy_now_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return buy_now_form('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = 'empty'

    return render(request, 'apartments/purchase_status.html', {'form': form})


def agents(request):
    # Checks if the person in the Users table is staff
    users = Users.objects.filter(is_staff = True)
    # Simply returns every users that returned true as staff
    # HTML will then loop through the users that are part of the staff and display them
    context = {
        'users': users
    }
    return render(request, 'apartments/agents.html', context)
    

# History of the company. It is important to play to the prestige of the company
# As this is supposed to be a reputable seller
def companyHistory(request):

    context = {
        'oliver': 'oliver'
    }
    return render(request, 'apartments/company_history.html', context)


# Price list is what the seller can come to expect to pay to the real estate agent
# Some of the prices are also charged directly to the buyer and added to the final
# price of the real estate in question
def priceList(request):
    fluff = ''
    prices = PriceLists.objects.all()
    price = prices.last()
    print(price)
    context = {
        'price': price,
        'fluff':fluff
    }
    return render(request, 'apartments/price_list.html', context)


# This is the page you are led to when an apartment is clicked on
def singleApartment(request, apartmentID):  # Need to add error handling
    context = {}

    print("Print machine :",Locations.objects.filter(country_id= 'Iceland', zip = '108'))
    aparments = get_object_or_404(Apartments, pk=apartmentID)

    checking = Listings.objects.filter(apartmentid_id =apartmentID)
    apartments = Apartments.objects.get(id=apartmentID)
    print(len(checking))
    if len(checking) == 0:
        context = {
            'apartment': apartments,
        }
        return render(request, 'apartments/unlisted_apartment.html', context)

    else:
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
            'agent': listingAgent,
            'listing' : listing
        }
        return render(request, 'apartments/single_apartment.html', context)




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
        return render(request, 'apartments/single_user.html', context)
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
    return render(request, 'apartments/single_employee.html', context)



def allApartments(request):
    context = {
        'apartments' : Apartments.objects.all()
    }
    return render(request, 'apartments/apartments_list.html', context)



def addPaymentInfo(request, apartmentID):
    #get or what??
    print("addPaymentInfo")
    if request.method == 'POST':
        print("IF ")
        form=PaymentInfoForm(data=request.POST)
        if form.is_valid():
            print('HANDLING POST REQUEST',request)
            #færa notanda á review síðu
            #TODO review.html
            payment=form.save(commit=False)
            payment.user = request.user
            payment.save()
            print(payment.user, request.user.id)
            return redirect('review', {{apartmentID}}, request.user.id[-1])
        #else:
         #   print("ELSE")
            #form = PaymentInfoForm()
    currentUser = request.user.id
    form = PaymentInfoForm(data=request.GET)
    print('HANDLING GET REQUEST',request)
    return render(request, 'apartments/buy_now.html', {
        'form': form
    })

#shows info for user and user confirms payment
def reviewPayment(request, apartmentID, paymentID):
    if PaymentInfos.objects.get(id=paymentID).id == paymentID:
        paymentInfo = PaymentInfos.objects.get(id=paymentID)
        apartment = Apartments.objects.get(id=apartmentID)
        context = {
            'payment': paymentInfo,
            'apartment': apartment
        }
    return render(request, 'apartments/review_payment.html', context)




def createLocation(request):
    currentUser = request.user
    if currentUser.id == None or currentUser.is_staff == False:
        return HttpResponse('Unauthorized', status=401)
    if request.method == 'POST':
        addressForm = AddressCreateForm(data=request.POST, prefix='location')
        if addressForm.is_valid(): #Built in to check if valid
            addressForm.save() #Saves to the DB
            return redirect('create-apartment') #Supposed to redirect to create apartment
        context = {'address_form': addressForm}
        return render(request, 'apartments/create_location.html', context)
    else:
        addressForm = AddressCreateForm(data=request.GET, prefix='location')
        return render(request, 'apartments/create_location.html', {
            'address_form': addressForm
        })


def createApartments(request):
        currentUser = request.user
        if currentUser.id == None or currentUser.is_staff == False:
            return HttpResponse('Unauthorized', status=401)
        if request.method == 'POST':
            # Read data from apartments form, and from address form.
            appForm = CastleAppsCreateForm(data=request.POST, prefix='apartment')
            if appForm.is_valid():
                appForm.save()
                return redirect('frontpage')
            context = {'app_form': appForm}
            return render(request, 'apartments/create_apartment.html', context)
        else:
            appForm = CastleAppsCreateForm(data=request.GET, prefix='apartment')
            return render(request, 'apartments/create_apartment.html', {
                'app_form': appForm
            })



def searchApartments(request):
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


def editApartment(request, apartment_id=None):
    currentUser = request.user
    if currentUser.id == None or currentUser.is_staff == False:
        return HttpResponse('Unauthorized', status=401)
    instance = get_object_or_404(Apartments, pk=apartment_id)
    if request.method == 'POST':
        form = EditAppForm(data=request.POST, instance=instance)
        if form.is_valid():
            print("FORM IS VALID!")
            form.save()
            return redirect('frontpage')
        else:
            print('invalid!!!')
    form = EditAppForm(instance=instance)
    print("FORM INVALID")
    return render(request, 'apartments/edit-apartment.html', {"form": form, "apartment_id": apartment_id})


def addListing(request, apartment_id=None):
    print("IN ADD LISTING")
    print("PRINTING APARTMENT ID: ", apartment_id)
    apartment = Apartments.objects.get(id=apartment_id)

    if request.method == 'POST':
        #currentUser = request.user
        #if currentUser.id == None or currentUser.is_staff:
            #return HttpResponse('Unauthorized', status=401)
        form = ListingForm(data=request.POST)
        if form.is_valid():
            t = Apartments.objects.get(id=apartment_id)
            t.forsale = True  # change field
            t.save()  # this will update only
            print("FORM VALID")
            form.save()
            print("Form saved")
            return redirect('frontpage')

    form = ListingForm(data=request.GET)

    return render(request, 'apartments/add_listing.html', {'form': form})

