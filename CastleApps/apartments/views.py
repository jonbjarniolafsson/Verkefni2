from django.shortcuts import render

# Create your views here.
employees = [
    {
        'name': 'Jón Bjarni Ólafsson',
        'age': '23',
        'gender': 'male',
        'description': 'Jón is learning computer science at Háskólinn í Reykjavík and is pursuing a career in web developement.'
    },

    {
        'name': 'Haraldur Björnsson',
        'age': '23',
        'gender': 'male',
        'description': 'Haraladur is learning Mechatronical engineering with computer science, Haraldur is great with robots.'
    },

    {
        'name': 'Þorgeir Björnsson',
        'age': '23',
        'gender': 'male',
        'description': 'Þorgeir is learning computer science at Háskólinn í Reykjavík and wants to work at a bank someday'
    },
    {
        'name': 'Friðrik Örn Gunnarson',
        'age': '22',
        'gender': 'male',
        'description': 'Friðrik is studying business with computer science and his passion selling real estate'
    },
    {
        'name': 'Fjölnir Þrastarson',
        'age': '22',
        'gender': 'male',
        'description': 'Fjölnir is is studying business with computer science and he plays a lot of basketball'
    }
]


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


def home(request):
    context = {
        'apartments':apartments

    }
    return render(request, '../templates/home.html',context)

def about(request):

    context = {
        'employees': employees
    }

    return render(request, '../templates/about.html', context)

def apartment(request, apartmentid):

    context = {}
    for item in apartments:
        if item['aid'] == str(apartmentid):

            context = {
                'apartment': item
            }
    return render(request, '../templates/single-apartment.html', context)


def all_apartments(request):
    context = {
        'apartments': apartments
    }
    return render(request, '../templates/apartments-list.html', context)

