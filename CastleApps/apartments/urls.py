from . import views
from django.urls import path

urlpatterns = [
     #Our mainpage
     path('',views.home, name='frontpage'),


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



     path('create_apartment', views.createApartments, name="create-apartment"),
     path('create_location', views.createLocation, name="create-location"),
     path('apartments/<int:apartmentID>/edit_apartment', views.editApartment, name="edit-apartment"),
     path('apartments/<int:apartmentID>/add_listing/', views.addListing, name="add-listing"),
     path('apartments/<int:apartmentID>/remove_listing/', views.removeListing, name="add-listing"),

     path('apartments/<int:apartmentID>/payment_info', views.addPaymentInfo, name="pay_info"),
     path('apartments/<int:apartmentID>/payment_info/<listingID>/<int:paymentID>/review', views.reviewPayment, name="review"),
]