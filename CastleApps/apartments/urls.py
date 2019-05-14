from . import views
from django.urls import path

urlpatterns = [
     #Our mainpage
     path('',views.home, name='frontpage'),
     # Here we have a list of employees page -> Should lead to their profile if clicked on
     path('agents/',views.agents, name='agents'),

     #Paths below are available to everyone
     path('price_list/',views.priceList, name='priceList'),
     path('company_history/', views.companyHistory, name ='companyHistory'),

     #Page below is for ajax search
     path('all_apartments/',
          views.allApartments, name="apartment-list"),

     #Search form on frontpage
     path('search_results/', views.searchApartments, name="search-results"),

     #This should lead to a listing
     path('apartments/<int:apartmentID>/',
          views.singleApartment, name="apartment"),

     #Path leads to a single users in our system
     path('users/<int:userID>/',
          views.singleUser, name = "users"),

     path('create_apartment', views.createApartments, name="create-apartment"),
     path('create_location', views.createLocation, name="create-location"),
     path('edit_apartment/<int:apartment_id>/', views.edit_apartment, name="edit-apartment"),
     path('add_listing/<int:apartment_id>/', views.add_listing, name="add-listing"),



    path('apartments/<int:apartmentID>/payment_info', views.addPaymentInfo, name="pay_info"),
     path('apartments/<int:apartmentID>/payment_info/<int:id>/review', views.reviewPayment, name="review"),

]