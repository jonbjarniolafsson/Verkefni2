# Create your models here.
from django.db import models  # Tells it to map to database
from django.utils import timezone
from django.conf import settings


# You do not need to specify primary key. It is automatically
# generated and auto incremented

# Steps to update the Database
# makemigrations apartments
# migrate apartments
# sqlmigrate apartments 0001_initial
# migrate

# Our model.py was designed with the ID being auto generated in mind.

# Location is a general place to be able to better normalize the data.


# In the model.py we decided to break our own rules when it comes to variables
# We did this to make it easier for us to access the Database through the Django code
# So we did not have to worry about capitalization
class Country(models.Model):
    country = models.CharField(primary_key=True, max_length=100)
    def __str__(self):
        return self.country

class Locations(models.Model):
    city = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=50)
    zip = models.CharField(max_length=15)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.country)

# Apartments is general information about the apartment that is only inserted once
class Apartments(models.Model):
    registration = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=50)
    size = models.IntegerField(max_length=50)
    rooms = models.IntegerField(max_length=50)
    bathrooms = models.IntegerField(max_length=50)
    type = models.CharField(max_length=50, default="Apartment")
    aptsuite = models.CharField(blank=True, null=True, max_length=30)
    timeofconstruction = models.CharField(max_length=50, default=2000)
    displayimage = models.CharField(max_length=5000)
    forsale = models.BooleanField(default=False, blank=True, null=True)
    locationid = models.ForeignKey(Locations, on_delete=models.CASCADE, )  # Foreign keys are singular. While the table
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# Apartments usually have many images associated with them
class ApartmentImages(models.Model):
    image = models.CharField(max_length=5000)
    aid = models.ForeignKey(Apartments, on_delete=models.CASCADE)
    def __str__(self):
        return self.image

# Each apartments has a listing. It can have many listings.
# Same apartment can only have one listing up at a time though!
class Listings(models.Model):
    price = models.IntegerField(max_length=200)
    description = models.TextField()
    registered = models.DateTimeField(default=timezone.now)
    soldondate = models.DateTimeField(default=None, blank=True, null=True)
    agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    apartmentid = models.ForeignKey(Apartments, on_delete=models.CASCADE)

    @property
    def shortMortgage(self):
        price = int(self.price)
        priceAfterDownPayment = price * 0.85  # We assume people put 15% down
        return (priceAfterDownPayment / 120) + (0.05 / 12 * priceAfterDownPayment)

    @property
    def mediumMortgage(self):
        price = int(self.price)
        priceAfterDownPayment = price * 0.85  # We assume people put 15% down
        return (priceAfterDownPayment / 240) + (0.05 / 12 * priceAfterDownPayment)

    @property
    def longMortgage(self):
        price = int(self.price)
        priceAfterDownPayment = price * 0.85  # We assume people put 15% down
        return (priceAfterDownPayment / 360) + (0.05 / 12 * priceAfterDownPayment)


# We use this to register the open houses. THese are displayed on the front page.
class OpenHouse(models.Model):
    openhousestart = models.DateTimeField(default=None, max_length=75)
    openhouseend = models.DateTimeField(default=None, max_length=75)
    listingid = models.ForeignKey(Listings, on_delete=models.CASCADE)


# These are small things as the table names suggest. We display this after an apartment has been
# Listed for sale you can add distance to supermarket etc.
class ListingMiscs(models.Model):
    footpreschool = models.CharField(max_length=5, blank=True, null=True)
    carpreschool = models.CharField(max_length=5, blank=True, null=True)
    footbusstop = models.CharField(max_length=5, blank=True, null=True)
    carbusstop = models.CharField(max_length=5, blank=True, null=True)
    carsupermarket = models.CharField(max_length=5, blank=True, null=True)
    footsupermarket = models.CharField(max_length=5, blank=True, null=True)
    footmetro = models.CharField(max_length=5, blank=True, null=True)
    carmetro = models.CharField(max_length=5, blank=True, null=True)
    listingid = models.ForeignKey(Listings, on_delete=models.CASCADE)


# Each apartment can have many documents attached to them. repair bills/copy of deed and more
class ListingDocs(models.Model):
    attachment = models.CharField(max_length=500, default=None)
    description = models.CharField(max_length=500, default=None)
    listingid = models.ForeignKey(Listings, on_delete=models.CASCADE)


# Used to calculate the final price and used to display the list on our website
class PriceLists(models.Model):
    salescost = models.CharField(max_length=20)
    appraisalcost = models.CharField(max_length=15)
    photocost = models.CharField(max_length=15)
    managementcost = models.CharField(max_length=15)
    datacollection = models.CharField(max_length=15)


class Transactions(models.Model):
    price = models.CharField(max_length=4000)
    date = models.DateField()
    isseller = models.BooleanField()
    listingid = models.ForeignKey(Listings, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

# All the information necessary to make a purchase on our platform
class PaymentInfos(models.Model):
    cardnumber = models.CharField(max_length=30)
    cardholder = models.CharField(max_length=80)
    expmonth = models.CharField(max_length=50)
    expyear = models.CharField(max_length=50)
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    aptsuite = models.CharField(max_length=20, default=None, blank=True, null=True)
    zip = models.CharField(max_length=80)
    ssn = models.CharField(max_length=40)
    isreviewed = models.BooleanField(default=False, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# The contact form being used on the front page down to the right
# Sends an AJAX request.
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField(max_length=1000)




class ViewHistory(models.Model):
    apartmentid = models.ForeignKey(Apartments, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class CompanyInformation(models.Model):
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=5000)
    backgroundPhoto = models.CharField(max_length=5000)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    officeHours = models.CharField(max_length=40)
