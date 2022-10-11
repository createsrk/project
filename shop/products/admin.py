from django.contrib import admin
from .models import Product,Offer

class ProductAdmnin(admin.ModelAdmin):
    list_display = ('name','price','stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount')


# Register your models here.
admin.site.register(Product,ProductAdmnin)
admin.site.register(Offer,OfferAdmin)

