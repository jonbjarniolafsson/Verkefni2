from django.shortcuts import render,redirect
from .forms.apartmentform import CastleAppsCreateForm
#from .forms.signup_form import CastleAppsSignupForm
from django.http import HttpResponse
# Create your views here.
from apartments.models import *
from users.models import *



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
def singleApartment(request, apartmentid): # Need to add error handling
    context = {}
    print("ERROR HANDLING" ,apartmentid)
    if Apartments.objects.get(id=apartmentid).id == apartmentid:
        print("HEre we are", apartmentid)
        apartments = Apartments.objects.get(id = apartmentid)
        apartmentImages = Apartments.objects.get(pk=2).apartmentimages_set.all()
        print("image print: ",apartmentImages.first())
        apartmentImages = apartmentImages.all()
        listings = Listings.objects.get(apartment =apartmentid)

        context = {
            'apartment': apartments,
            'images' : apartmentImages,
            'listings': listings
        }
    return render(request, 'apartments/single-apartment.html', context)


def all_apartments(request):
    context = {
        'apartments': apartments
    }
    return render(request, 'apartments/apartments-list.html', context)



def create_apartment(request):
    if request.method == 'POST':
        form = CastleAppsCreateForm(data=request.POST)
        print("POST")
        if form.is_valid():
            print("IS VALID")
            Apartments = form.save()
            apartments_image = ApartmentImages(image=request.POST['image'], Apartments=Apartments)
            apartments_image.save()
            return redirect('frontpage')
        else:
            response_data = {
                'SType' : 'error',
                'message' : form.errors
            }

    form = CastleAppsCreateForm(data=request.GET)
    return render(request, 'apartments/create-apartment.html', {
        'form' : form
})