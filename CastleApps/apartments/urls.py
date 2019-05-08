from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='frontpage'),
    path('about/',views.about, name='about'),
    path('all-apartments/',
         views.all_apartments, name="apartment-list"),
    path('apartment/<int:apartmentid>/',
         views.apartment, name="apartment")

]