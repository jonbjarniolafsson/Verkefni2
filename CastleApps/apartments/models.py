from django.db import models

# Create your models here.
from django.db import models #Tells it to map to database
from django.utils import timezone
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
class Locations(models.Model):
    city = models.CharField(max_length=100, default=None)
    region = models.CharField(max_length=50)
    zip = models.CharField(max_length=15)
    country = models.CharField(max_length=100)

# Apartments is general information about the apartment that is only inserted once
class Apartments(models.Model):
    address = models.CharField(max_length = 50)
    size = models.IntegerField()
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    type = models.CharField(max_length=200)
    timeOfConstruction = models.IntegerField()
    timeOfRegistration= models.DateTimeField(default=datetime.now)
    price = models.IntegerField()
    displayImage = models.CharField(max_length = 5000)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE) # Foreign keys are singular. While the table
    # they belong to are multi
    def __str__(self):
        return self.displayImage
# Apartments usually have many images associated with them
class ApartmentImages(models.Model):
    image = models.CharField(max_length=5000)
    aID = models.ForeignKey(Apartments, on_delete=models.CASCADE)
    def __str__(self):
        return self.image

class roles(models.Model):
    description = models.CharField(max_length = 500)

# Employees are the people that work for the company.
# If employees want to be buyers/sellers then they can make their own User account
class Users(models.Model):
    email = models.CharField(unique = True, max_length = 40)
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 20)
    profileImagePath = models.CharField(default = None, max_length = 50000)
    role = models.ForeignKey(roles, on_delete = models.CASCADE)

class Employees(models.Model):
    description = models.CharField(max_length = 500)
    startDate = models.DateField(null = True, blank = True, default = None)
    endDate = models.DateField(null = True, blank = True, default = None)
    user = models.ForeignKey(Users, on_delete = models.CASCADE)


# Each apartments has a listing. It can have many listings.
# Same apartment can only have one listing up at a time though!
class Listings(models.Model):
    price = models.BigIntegerField()
    desc = models.TextField()
    registered = models.DateTimeField(default=timezone.now)
    soldOnDate = models.DateTimeField(default = None)
    openHouse = models.CharField(default = None, max_length = 75)
    employee = models.ForeignKey(Employees, default = None, on_delete = models.CASCADE)
    User = models.ForeignKey(Users, on_delete = models.CASCADE)
    apartment = models.ForeignKey(Apartments, on_delete = models.CASCADE)

# Each apartment can have many documents attached to them. repair bills/copy of deed and more
class listingDocs(models.Model):
    listing = models.ForeignKey(Listings, on_delete = models.CASCADE)
    attachment = models.CharField(max_length = 500, default = None)
    description = models.CharField(max_length = 500, default = None)

# Used to calculate the final price and used to display the list on our website
class PriceLists(models.Model):
    salesCost = models.CharField(max_length = 20)
    appraisalCost = models.CharField(max_length = 15)
    photoCost = models.CharField(max_length = 15)
    managementCost = models.CharField(max_length = 15)
    dataCollection = models.CharField(max_length = 15)

# All the information necessary to make a purchase on our platform
class PaymentInfos(models.Model):
    cardNumber = models.CharField(max_length=30)
    cardHolder = models.CharField(max_length=80)
    expMonth = models.IntegerField()
    expYear = models.IntegerField()
    address = models.CharField(max_length=80)
    aptSuite = models.CharField(max_length=20, default = None)
user = models.ForeignKey(Users, on_delete=models.CASCADE)