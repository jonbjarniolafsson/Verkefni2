from apartments.models import *

def getZipCodes(request):
    zipList = Locations.objects.all().values_list("zip", flat=True).distinct()
    companyInfo = CompanyInformation.objects.get(name = 'Castle Inc.')

    # locations = Locations.objects.all()
    # zipList = [loc.zip for loc in locations]
    zipCodes = {
<<<<<<< HEAD
        'zip' : zipList
    } 

    return zipCodes
=======
        'zip' : zipList,
        'compInfo':companyInfo
    }
    return zipCodes
>>>>>>> 050dcdd62e4e87c1bca8b8d15dc5c72d493e39cb
