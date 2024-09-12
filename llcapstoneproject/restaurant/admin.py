from django.contrib import admin
from .models import Booking, Menu, MenuItem

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "noOfGuests", "bookingDate")

class MenuAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "inventorydata")
    
admin.site.register(Booking, BookingAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem)