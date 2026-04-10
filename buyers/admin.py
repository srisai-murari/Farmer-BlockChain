from django.contrib import admin
from .models import BuyerUserRegistrationModel,BuyerCropCartModels,BuyerTransactionModels,BlockChainTransactionModel
# Register your models here.
admin.site.register(BuyerUserRegistrationModel)
#admin.site.register(BuyerCropCartModels)
#admin.site.register(BuyerTransactionModels)



"""
changes for clean code

from django.contrib import admin
from .models import BuyerUserRegistrationModel, BuyerTransactionModels

admin.site.register(BuyerUserRegistrationModel)
admin.site.register(BuyerTransactionModels)

"""
