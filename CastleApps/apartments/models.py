from django.db import models

# Create your models here.
from django.db import models #Tells it to map to database
from django.utils import timezone
from django.conf import settings
from datetime import datetime

from django.shortcuts import  render

# You do not need to specify primary key. It is automatically
# generated and auto incremented

#Steps to update the Database
# makemigrations apartments
# migrate apartments
# sqlmigrate apartments 0001_initial
# migrate

# Our model.py was designed with the ID being auto generated in mind.

# Location is a general place to be able to better normalize the data.

class Country(models.Model):
    country = models.CharField(primary_key = True, max_length = 40)

class Locations(models.Model):
    city = models.CharField(max_length=100, blank=True,null=True)
    region = models.CharField(max_length=50)
    zip = models.CharField(max_length=15)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
#    def __str__(self):
#        return self.country


# Apartments is general information about the apartment that is only inserted once
class Apartments(models.Model):
    registration = models.CharField(max_length = 100, unique = True)
    address = models.CharField(max_length = 50)
    size = models.IntegerField()
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    aptsuite = models.CharField(blank=True,null=True, max_length = 30)
    type = models.CharField(max_length=50)
    timeofconstruction = models.IntegerField( default = 2000)
    type = models.CharField(max_length = 50)
    displayimage = models.CharField(max_length = 5000)
    locationid = models.ForeignKey(Locations, on_delete=models.CASCADE, ) # Foreign keys are singular. While the table
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)




# Apartments usually have many images associated with them
class ApartmentImages(models.Model):
    image = models.CharField(max_length=5000)
    aid = models.ForeignKey(Apartments, on_delete=models.CASCADE)
    def __str__(self):
        return self.image


# Each apartments has a listing. It can have many listings.
# Same apartment can only have one listing up at a time though!
class Listings(models.Model):
    price = models.BigIntegerField()
    description = models.TextField()
    registered = models.DateTimeField(default=timezone.now)
    soldondate = models.DateTimeField(default = None, blank=True,null=True)
    agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    apartmentid = models.ForeignKey(Apartments, on_delete=models.CASCADE)

class OpenHouse(models.Model):
    openhousestart = models.DateTimeField(default=None, max_length=75)
    openhouseend = models.DateTimeField(default=None, max_length=75)
    listingid = models.ForeignKey(Listings, on_delete=models.CASCADE)

class ListingMiscs(models.Model):
    footpreschool = models.CharField(max_length = 5, blank=True,null=True)
    carpreschool = models.CharField(max_length = 5 ,blank=True,null=True)
    footbusstop = models.CharField(max_length = 5, blank=True, null=True)
    carsupermarket = models.CharField(max_length = 5, blank=True, null=True)
    footsupermarket = models.CharField(max_length=5, blank=True, null=True)
    footmetro = models.CharField(max_length=5, blank=True, null=True)
    carmetro = models.CharField(max_length=5, blank=True, null=True)
    listingid = models.ForeignKey(Listings, on_delete=models.CASCADE)


# Each apartment can have many documents attached to them. repair bills/copy of deed and more
class listingDocs(models.Model):
    attachment = models.CharField(max_length = 500, default = None)
    description = models.CharField(max_length = 500, default = None)
    listingid = models.ForeignKey(Listings, on_delete=models.CASCADE)

# Used to calculate the final price and used to display the list on our website
class PriceLists(models.Model):
    salescost = models.CharField(max_length = 20)
    appraisalcost = models.CharField(max_length = 15)
    photocost = models.CharField(max_length = 15)
    managementcost = models.CharField(max_length = 15)
    datacollection = models.CharField(max_length = 15)

# All the information necessary to make a purchase on our platform
class PaymentInfos(models.Model):
    cardnumber = models.CharField(max_length=30)
    cardholder = models.CharField(max_length=80)
    expmonth = models.IntegerField()
    expyear = models.IntegerField()
    address = models.CharField(max_length=80)
    aptsuite = models.CharField(max_length=20, default = None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
