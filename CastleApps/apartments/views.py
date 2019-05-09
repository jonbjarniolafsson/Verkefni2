#from django.shortcuts import render
from .forms.apartmentform import CastleAppsCreateForm
#from .forms.signup_form import CastleAppsSignupForm
from django.http import HttpResponse
# Create your views here.
from apartments.models import *




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
def about(request):
    dbEmployees = Employees.objects.all()
    context = {
        'employees': dbEmployees
    }
    return render(request, 'apartments/about.html', context)


def singleApartment(request, apartmentid):

    context = {}
    for item in apartments:
        if item['aid'] == str(apartmentid):

            context = {
                'apartment': item
            }
    return render(request, 'apartments/single-apartment.html', context)


def all_apartments(request):
    context = {
        'apartments': apartments
    }

    return render(request, 'apartments/apartments-list.html', context)



def create_apartment(request):
    if request.method == 'POST':
        form = CastleAppsCreateForm(data=request.POST['image'],)
        if form.is_valid():
            apartment = form.save()
            apartment_image = ApartmentImage(image=request.POST)
    else:
        form = CastleAppsCreateForm()
        return render(request, 'apartments/create-apartment.html', {
            'form' : form
})