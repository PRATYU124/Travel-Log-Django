from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class Expense(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paid_expenses')
    split_between = models.ManyToManyField(User, related_name='shared_expenses')

# ✅ Add from here below Expense

class Destination(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='destinations')
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True, null=True)  # ✅ New field

    

    def __str__(self):
        return self.name


class PlaceToVisit(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='places')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='restaurants')
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='hotels')
    name = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    address = models.CharField(max_length=255)
    rating = models.FloatField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
