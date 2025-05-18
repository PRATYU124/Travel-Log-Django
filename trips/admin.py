from django.contrib import admin
from .models import Trip, Expense, Destination, PlaceToVisit, Restaurant,Hotel

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    list_filter = ('start_date', 'end_date')
    date_hierarchy = 'start_date'
    ordering = ('-start_date',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'trip', 'amount', 'paid_by')
    search_fields = ('description',)
    list_filter = ('trip',)
    autocomplete_fields = ('split_between',)

# ✅ Registering new models for trip destinations, places, and restaurants

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'trip', 'latitude', 'longitude')
    
    
@admin.register(PlaceToVisit)
class PlaceToVisitAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination')
    search_fields = ('name',)
    list_filter = ('destination',)

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'cuisine', 'rating')
    search_fields = ('name', 'cuisine')
    list_filter = ('destination', 'cuisine', 'rating')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'price_per_night', 'availability', 'rating')
    search_fields = ('name',)
    list_filter = ('destination', 'availability', 'rating')
