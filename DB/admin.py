from django.contrib import admin

# Register your models here.
from .models import Location, Hotel, Room, Review, Wishlist

admin.site.register(Location)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Review)
admin.site.register(Wishlist)
