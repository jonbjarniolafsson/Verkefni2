from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='frontpage'),
    path('about/',views.about, name='about'),
    path('all-apartments/',
         views.all_apartments, name="apartment-list"),
    path('apartments/<int:apartmentid>/',
         views.singleApartment, name="apartment"),
    path('create_apartment', views.create_apartment, name="create-apartment"),

]