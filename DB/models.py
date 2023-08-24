from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Locations'
    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='item_images',  blank=True)
    description = models.TextField(blank=True)
    is_sold = models.BooleanField(default=False)
    Location = models.ForeignKey(Location, related_name='hotels', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='hotels', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type = models.CharField(max_length=250)
    image = models.ImageField(upload_to="products", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    max_occupancy = models.IntegerField(default=2, validators=[MaxValueValidator(100), MinValueValidator(1)])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


class Review(models.Model):
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=10, validators=[MaxValueValidator(10), MinValueValidator(1)])
    review = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review

class Wishlist(models.Model):
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
