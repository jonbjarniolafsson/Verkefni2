from apartments.models import *

def getZipCodes(request):
    zipList = Locations.objects.all().values_list("zip", flat=True).distinct()
    companyInfo = CompanyInformation.objects.get(name = 'Castle Inc.')

    # locations = Locations.objects.all()
    # zipList = [loc.zip for loc in locations]
    zipCodes = {
        'zip' : zipList
    } 

    return zipCodes