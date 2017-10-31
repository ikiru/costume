# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name):
        if not email:
            raise ValueError('Email address must be valid')
        if not password:
            raise ValueError('Password must be valid')
        if not first_name:
            raise ValueError('First name must be valid')
        if not last_name:
            raise ValueError('Last name must be valid')

        user = self.model(
        first_name = first_name,
        last_name = last_name,
        email = self.normalize_email(email),
        password = password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(email, password, first_name, last_name)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45, unique = True)
    password = models.CharField(max_length=45)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    #Email is the identifying field
    USERNAME_FIELD = 'email'

    #Want to require these field at registration
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def get_full_name(self):
        return self.first_name, self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        string_output = " ID: {} Email: {} Password: {} Admin: {}"
        return string_output.format(
        self.id,
        self.email,
        self.password,
        self.is_admin,
        )

class State(models.Model):
    name = models.Charfield(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Organization(models.Model):
    name = models.Charfield(max_length=104)
    address = models.Charfield(max_length=104)
    zipcode = models.Charfield(max_length=10)
    phone = models.Charfield(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Renter(Organization):
    state = models.ForeignKey(State, related_name="renters", on_delete=models.CASCADE)
    tax_id = models.Charfield(max_length=45)

class Owner(Organization):
    state = models.ForeignKey(State, related_name="owners", on_delete=models.CASCADE)
    customers = models.ManyToManyField(Renter, through="Event")

class Event(models.Model):
    name = models.CharField(max_length=45)
    event_date = models.DateTimeField(null=True) #Needs to be able to accomadate multiple dates
    pickup_date = models.DateTimeField(null=True)
    return_date = models.DateTimeField(null=True)
    one_week_price = models.CharField(max_length=45)
    two_week_price = models.CharField(max_length=45)
    other_week_price = models.CharField(max_length=45)
    purchases = models.CharField(max_length=45)# Not sure if we need all these fields
    subtotal = models.CharField(max_length=45)# but including anyway just in case
    tax = models.CharField(max_length=45)# This one too
    total_price = models.CharField(max_length=45)
    customer = ForeignKey(Renter, on_delete=models.CASCADE)
    owner = ForeignKey(Owner, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Pertains to Costume
class PrimaryColor(models.Model):
    color = CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Pertains to Costume
class SecondaryColor(models.Model):
    color = CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Pertains to Costume
class TimePeriod(models.Model):
    name = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Pertains to Costume
class Size(models.Model):
    size = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Costume(models.Model):
    image_1 = SlugField(max_length=500)
    image_2 = SlugField(max_length=500)
    image_3 = SlugField(max_length=500)
    qr_code = TextField()
    description = models.TextField()
    primary_color = models.ForeignKey(PrimaryColor, related_name="costumes", on_delete=models.CASCADE)
    secondary_colors = models.ManyToManyField(SecondaryColor, related_name="costumes")
    owner = models.ForeignKey(Owner, related_name="costumes", on_delete=models.CASCADE)
    renter = models.ForeignKey(Renter, related_name="costumes", on_delete=models.CASCADE)
    timePeriod = models.ForeignKey(TimePeriod, related_name="costumes", on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=True)
    on_exchange = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Pertains to Costume
class Show(models.Model):
    name = models.CharField(max_length=100)
    costumes = models.ManyToManyField(Costume, related_name="shows")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
