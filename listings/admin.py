from django.contrib import admin

# Register your models here.
from .models import Listing
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('listing_id', 'title', 'location', 'price_per_night', 'available_from', 'available_to', 'created_at')
    search_fields = ('title', 'location')
    list_filter = ('available_from', 'available_to', 'created_at')
    ordering = ('-created_at',)
