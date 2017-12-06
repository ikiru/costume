# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, Group

    # def __str__(self):
    #     string_output = " ID: {} Email: {} Password: {} Admin: {}"
    #     return string_output.format(
    #     self.id,
    #     self.email,
    #     self.password,
    #     self.is_admin,
    #     )

class State(models.Model):
    name = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Renter(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100) #Seed with cities
    zipcode = models.CharField(max_length=10) #Seed with available zips
    phone = models.CharField(max_length=12)
    tax_id = models.CharField(max_length=45)
    state = models.ForeignKey(State, related_name="renters") #Seed with states
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100) #Seed with cities
    zipcode = models.CharField(max_length=10) #Seed with zips
    phone = models.CharField(max_length=12)
    tax_id = models.CharField(max_length=45)
    state = models.ForeignKey(State, related_name="owners") #Seed with states
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    check_out = models.DateField(null=True)
    check_in = models.DateField(null=True)
    event_date = models.DateField(null=True) #Needs to be able to accomadate multiple dates

    one_week_price = models.DecimalField(max_digits=7, decimal_places=2)
    two_week_price = models.DecimalField(max_digits=7, decimal_places=2) #Eliminate this field, as per 3NF
    other_week_price = models.DecimalField(max_digits=7, decimal_places=2) #Eliminate this field, as per 3NF

    purchases = models.DecimalField(max_digits=7, decimal_places=2)# Not sure if we need all these fields
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)# but including anyway just in case
    tax = models.DecimalField(max_digits=10, decimal_places=6)# This one too
    total_price = models.DecimalField(max_digits=8, decimal_places=2) #Eliminate this field, as per 3NF

    customer = models.ForeignKey(Renter, related_name="invoices")
    owner = models.ForeignKey(Owner, related_name="invoices")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Pertains to Costume
class PrimaryColor(models.Model):
    color = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.color

#Pertains to Costume
class SecondaryColor(models.Model):
    color = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.color

#Pertains to Costume
class TimePeriod(models.Model):
    name = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

#Pertains to Costume
class Size(models.Model):
    size = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.size

#Pertains to Costume
class Show(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Costume(models.Model):
    image_1 = models.CharField(max_length=500)
    image_2 = models.CharField(max_length=500)
    image_3 = models.CharField(max_length=500)

    qr_code = models.TextField()
    description = models.TextField()

    size = models.ForeignKey(Size, related_name="costumes")
    primary_color = models.ForeignKey(PrimaryColor, related_name="costumes")
    secondary_color = models.ForeignKey(SecondaryColor, related_name="costumes")

    owner = models.ForeignKey(Owner, related_name="costumes")
    renter = models.ForeignKey(Renter, related_name="costumes")
    timePeriod = models.ForeignKey(TimePeriod, related_name="costumes")

    shows = models.ManyToManyField(Show, related_name="costumes")

    in_stock = models.BooleanField(default=True)
    on_exchange = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
