from django.urls import path
from . import views

urlpatterns = [
    #Our mainpage
    path('',views.home, name='frontpage'),
    # Here we have a list of employees page -> Should lead to their profile if clicked on
    path('agents/',views.agents, name='agents'),

    path('aboutus/',views.aboutus, name='aboutus'),

    #Page below has to be revamped
    path('all-apartments/',
         views.all_apartments, name="apartment-list"),

    #This should lead to a listing
    path('apartments/<int:apartmentID>/',
         views.singleApartment, name="apartment"),

    #Path leads to a single user in our system
    path('users/<int:userID>/',
         views.singleUser, name = "user"),

    path('create_apartment', views.create_apartment, name="create-apartment"),
    path('create_location', views.create_location, name="create-location"),

    path('buy_now', views.buyNow, name= "buy_now")

]