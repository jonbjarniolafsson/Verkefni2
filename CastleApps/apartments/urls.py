from . import views
from django.urls import path

urlpatterns = [
     #Our mainpage
     path('',views.home, name='frontpage'),
     # Here we have a list of employees page -> Should lead to their profile if clicked on
     path('agents/',views.agents, name='agents'),

     path('aboutus/',views.aboutus, name='aboutus'),

     #Page below is for ajax search
     path('all-apartments/',
          views.pureApartment, name="apartment-list"),

     #Search form on frontpage
     path('search-results/', views.search_apartment, name="search-results"),

     #This should lead to a listing
     path('apartments/<int:apartmentID>/',
          views.singleApartment, name="apartment"),

     #Path leads to a single users in our system
     path('users/<int:userID>/',
          views.singleUser, name = "users"),

     path('create_apartment', views.create_apartment, name="create-apartment"),
     path('create_location', views.create_location, name="create-location"),
     path('edit_apartment/<int:apartment_id>/', views.edit_apartment, name="edit-apartment"),


     path('buy_now', views.buyNow, name= "buy_now"),

    path('apartments/<int:apartmentID>/buynow', views.buyNow, name= "buy_now"),
    path('apartments/<int:apartmentID>/buynow/submit', views.buyNowSubmit, name= "buy_now")

]