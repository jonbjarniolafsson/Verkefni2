from django.shortcuts import render,redirect

# This document will act as our controller in our Apartments app. The main magic happens here.

from .forms.buy_now_form import PaymentInfoForm
from .forms.apartment_form import CastleAppsCreateForm,EditAppForm
from .forms.location_form import AddressCreateForm
from .forms.listing_form import ListingForm
from .forms.listing_misc_form import MiscInfoForm
# from .forms.signup_form import CastleAppsSignupForm
from django.http import HttpResponse
# Create your views here.
from apartments.models import *
from users.models import *
from django.db.models import Max
from django.shortcuts import get_object_or_404,render,redirect, reverse

from django.contrib.auth.decorators import login_required


from .forms import buy_now_form

from django.db.models import Q

from datetime import datetime
from django.utils import timezone

def home(request):
        #print("PRINTING CURRENT DATETIME: ", datetime.now())
        #apartment = Apartments.objects.get(id=3)
        #seller = apartment.owner_id
        #apartment.forsale = False  # change field
        #apartment.save()
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

        newlyListed = Listings.objects.all()
        print("NEWLY LISTED: ",newlyListed)
        apps = Apartments.objects.filter(forsale=True)
        #companyInfo = CompanyInformation.objects.all()
        context = {
            'apartments': newApart,  # Send all the apartments
            'newlyListed': apps,
            'userid': request.user.id
        }

        return render(request, 'apartments/home.html', context)




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



    #apartmentid = models.ForeignKey(Apartments, on_delete=models.CASCADE)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
# This is the page you are led to when an apartment is clicked on
def singleApartment(request, apartmentID):  # Need to add error handling
    context = {}
    user = request.user.id
    print("PRINTING ID OF USER: ", user)
    print("Print machine :",Locations.objects.filter(country_id= 'Iceland', zip = '108'))
    aparments = get_object_or_404(Apartments, pk=apartmentID)


    if user != None:
        ViewHistory.objects.create(apartmentid_id=apartmentID, user_id=user)


    #if request.user.is_authenticated == True:

    #    apartment = Apartments.objects.get(id=apartmentID)
    #    ViewHistory.objects.create(apartmentid=apartment.pk, user=user)


    checking = Listings.objects.filter(apartmentid_id =apartmentID)
    apartments = Apartments.objects.get(id=apartmentID)
    print(len(checking))
    if len(checking) == 0 or apartments.forsale == False:
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
        listingAgent = Users.objects.get(id = listing.agent_id)
        user = request.user
    #Tests if listing has misc information to display
    try:
        listingMisc = ListingMiscs.objects.get(listingid_id=listing.id)
        context1 = {
            'apartment': apartments,
            'images': apartmentImages,
            'agent': listingAgent,
            'listing': listing,
            'user': user,
            'listingMisc': listingMisc
        }
        return render(request, 'apartments/single_apartment.html', context1)

    except ListingMiscs.DoesNotExist:
        listingMisc = None
        context2 = {
            'apartment': apartments,
            'images': apartmentImages,
            'agent': listingAgent,
            'listing': listing,
            'user': user,
        }
    return render(request, 'apartments/single_apartment.html', context2)







def allApartments(request):
    context = {
        'apartments' : Apartments.objects.all()[0:6]
    }
    return render(request, 'apartments/apartments_list.html', context)

def addKeyDistances(request, apartmentID):
    listings = Listings.objects.filter(apartmentid_id=apartmentID)
    idOfActiveListing = listings.aggregate(Max('id'))
    listing = Listings.objects.get(id=idOfActiveListing['id__max'])
    if request.method == 'POST':
        form = MiscInfoForm(data=request.POST)
        if form.is_valid():
            miscData = form.save(commit=False)
            miscData.listingid_id = listing.id
            miscData.save()
            print("REDIRECTING")
            return redirect("/apartments/{apartmentID}")
    form = MiscInfoForm()

    return render(request, 'apartments/listing_misc.html', {
        'form': form,
        'listing': listing
    })


def createLocation(request):
    # currentUser = request.user
    # if currentUser.id == None or currentUser.is_staff == False:
    #     return HttpResponse('Unauthorized', status=401)
    if request.method == 'POST':
        addressForm = AddressCreateForm(data=request.POST, prefix='location')
        if addressForm.is_valid(): #Built in to check if valid
            locationID = Locations.objects.latest('id').id
            addressForm.save() #Saves to the DB
            return redirect(reverse("create-apartment",args=[locationID])) #Supposed to redirect to create apartment
        context = {'address_form': addressForm}
        return render(request, 'apartments/create_location.html', context)
    else:
        addressForm = AddressCreateForm(data=request.GET, prefix='location')
        return render(request, 'apartments/create_location.html', {
            'address_form': addressForm
        })


def createApartments(request, locationID):
        # currentUser = request.user
        # if currentUser.id == None or currentUser.is_staff == False:
        #     return HttpResponse('Unauthorized', status=401)
        instance = Locations.objects.latest('id')
        if request.method == 'POST':
            # Read data from apartments form, and from address form.
            appForm = CastleAppsCreateForm(data=request.POST, instance=instance)
            if appForm.is_valid():
                appForm.save()
                return redirect('frontpage')
            context = {'app_form': appForm, 'locationID': locationID}
            return render(request, 'apartments/create_apartment.html', context)
        else:
            appForm = CastleAppsCreateForm(instance=instance, initial={'locationid': locationID})
            return render(request, 'apartments/create_apartment.html', {
                'app_form': appForm,
                'locationID': locationID


            })



def searchApartments(request):
    searchString = request.GET.get("search")
    zipCode = request.GET.get("zip")
    sort = request.GET.get("sort")

    if zipCode != "":
        apartments = Apartments.objects.filter(Q(locationid__zip=zipCode))
        apartments = apartments.filter(Q(address__icontains=searchString) | Q(type__icontains=searchString) | Q(locationid__city__icontains=searchString) | Q(locationid__region__icontains=searchString) | Q(locationid__country_id__country__icontains=searchString))

    else:
        apartments = Apartments.objects.filter(Q(address__icontains=searchString) | Q(type__icontains=searchString) | Q(locationid__zip__icontains=searchString) | Q(locationid__city__icontains=searchString) | Q(locationid__region__icontains=searchString) | Q(locationid__country_id__country__icontains=searchString))



    if sort != "":
        if sort == "price":
            apartments = apartments.order_by('listings__price')
        elif sort == "address":
            apartments = apartments.order_by('address')
        elif sort == "size":
            apartments = apartments.order_by('-size')
        elif sort == "rooms":
            apartments = apartments.order_by('-rooms')
        elif sort == "country":
            apartments = apartments.order_by('-locationid__country_id__country')
    
    apps = {
        'apartments' : apartments
    }
    return render(request, "apartments/search-results.html", apps)


def editApartment(request, apartmentID=None):
    currentUser = request.user
    if currentUser.id == None or currentUser.is_staff == False:
        return HttpResponse('Unauthorized', status=401)
    instance = get_object_or_404(Apartments, pk=apartmentID)
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
    return render(request, 'apartments/edit-apartment.html', {"form": form, "apartment_id": apartmentID})


def addListing(request, apartmentID=None):
    print("IN ADD LISTING")
    print("PRINTING APARTMENT ID: ", apartmentID)
    apartment = Apartments.objects.get(id=apartmentID)

    if request.method == 'POST':
        #currentUser = request.user
        #if currentUser.id == None or currentUser.is_staff:
            #return HttpResponse('Unauthorized', status=401)
        form = ListingForm(data=request.POST)
        if form.is_valid():
            t = Apartments.objects.get(id=apartmentID)
            t.forsale = True  # change field
            t.save()  # this will update only
            print("FORM VALID")
            form.save()
            print("Form saved")
            return redirect('frontpage')

    form = ListingForm(data=request.GET)

    return render(request, 'apartments/add_listing.html', {'form': form})

def removeListing(request, apartmentID=None):
    listings = Listings.objects.filter(apartmentid=apartmentID)
    idOfActiveListing = listings.aggregate(Max('id'))
    listing = Listings.objects.get(id=idOfActiveListing['id__max'])
    listing = Listings.objects.get(id=listing.id).delete()
    apartment = Apartments.objects.get(id = apartmentID)
    apartment.forsale=False
    apartment.save()
    return render(request, 'apartments/single_apartment.html')

def removeApartment(request, apartmentID=None):
    theApartment = Apartments.objects.get(id=apartmentID)
    apartment = Apartments.objects.get(id=apartmentID).delete()
    return render(request, 'apartments/deleted_apartment.html', {'apartment':theApartment})


@login_required
def addPaymentInfo(request, apartmentID):
    #get or what??
    if Apartments.objects.get(id=apartmentID).forsale:
        listings = Listings.objects.filter(apartmentid=apartmentID)
        idOfActiveListing = listings.aggregate(Max('id'))
        listing = Listings.objects.get(id=idOfActiveListing['id__max'])
        if request.method=="POST":
            form = PaymentInfoForm(data=request.POST)
            if form.is_valid():
                print("VALID FORM")
                #færa notanda á review síðu
                payment = form.save(commit=False)
                payment.user = request.user
                payment.save()
                return redirect(reverse("review", args=[apartmentID, listing.id, payment.id]))
        form = PaymentInfoForm()
        print('HANDLING GET REQUEST',request)
        apartment = Apartments.objects.get(id=apartmentID)
        return render(request, 'apartments/buy_now.html', {
            'form': form,
            'listing': listing,
            'apartment': apartment
        })
    else:
        return redirect('frontpage')

#shows info for user and user confirms payment
@login_required
def reviewPayment(request, apartmentID, listingID, paymentID):

    #hvað á að auðkenna?
    #vantar aðgengi að context
    listing = Listings.objects.get(id=listingID)
    if request.method == 'POST':

        apartment = Apartments.objects.get(id=apartmentID)
        apartment = Apartments.objects.get(id=apartmentID)
        seller = apartment.owner_id
        apartment.forsale = False  # change field
        apartment.owner_id = request.user.id
        apartment.save()  # this will update only
        listing = Listings.objects.get(id=listingID)
        listing.soldondate = datetime.now()
        listing.save()
        buyer = apartment.owner_id
        price = int(listing.price)
        priceSeller = str(price)
        priceBuyer = str(-price)

        #BUYER TRANSACTION
        buyerTransaction = Transactions.objects.create(price=priceBuyer, date=datetime.now(), isseller=False, listingid_id=listingID, user_id=buyer)
        #SELLER TRANSACTION
        sellerTransaction = Transactions.objects.create(price=priceSeller, date=datetime.now(), isseller=True, listingid_id=listingID, user_id=seller)
        return redirect('frontpage')
    context = {
        'listing': listing,
        'payment': PaymentInfos.objects.get(id=paymentID),
    }
    return render(request, 'apartments/review_payment.html', context)



