from apartments.models import *
from users.forms import ContactUs

def getZipCodes(request):
    zipList = Locations.objects.all().values_list("zip", flat=True).distinct()
    companyInfo = CompanyInformation.objects.get(name='Castle Apartments')

    # locations = Locations.objects.all()
    # zipList = [loc.zip for loc in locations]
    zipCodes = {
        'zip': zipList
    }

    return zipCodes


def contactForm(request):
    return {
        'contactForm' : ContactUs()
    }