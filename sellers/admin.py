from django.contrib import admin
from .models import SellerUserRegistrationModel, FarmersCropDataModels, FarmersCropsModels

admin.site.register(SellerUserRegistrationModel)
admin.site.register(FarmersCropDataModels)
admin.site.register(FarmersCropsModels)



"""
changes for clean code

from django.contrib import admin
from .models import SellerUserRegistrationModel, FarmersCropsModels

admin.site.register(SellerUserRegistrationModel)
admin.site.register(FarmersCropsModels)
"""