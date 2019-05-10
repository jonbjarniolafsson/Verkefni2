from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='frontpage'),
    path('agents/',views.agents, name='agents'),
    path('all-apartments/',
         views.all_apartments, name="apartment-list"),
    path('apartments/<int:apartmentid>/',
         views.singleApartment, name="apartment"),
    path('create_apartment', views.create_apartment, name="create-apartment"),
    path('create_location', views.create_location, name="create-location")

]