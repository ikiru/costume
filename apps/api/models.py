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
        string_output = " ID: {} Email: {} Password: {} Active: {} Admin: {}"
        return string_output.format(
        self.id,
        self.email,
        self.password,
        self.is_active,
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
    state = models.ForeignKey(State, related_name="clients")
    phone = models.Charfield(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Renter(Organization):
    tax_id = models.Charfield(max_length=45)
    is_school = models.BooleanField(default=False) #Easily see which renters are schools


#Pertains to Costume
#https://docs.djangoproject.com/en/1.11/topics/db/models/ Multi-table Inheritance
class Color(models.Model):
    color = CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Pertains to Costume
#Inherits from Color
class PrimaryColor(Color):


#Pertains to Costume
#Inherits from Color
class SecondaryColor(Color):


class Costume(models.Model):
    image_1 = SlugField(max_length=100)
    image_2 = SlugField(max_length=100)
    image_3 = SlugField(max_length=100)
    qr_code = TextField()
    description = models.TextField()
    primary_color = models.ForeignKey(PrimaryColor, related_name="costumes")
    secondary_colors = models.ManyToManyField(SecondaryColor, related_name="costumes")
    owner = models.ForeignKey(Client, related_name="costumes")
    renter = models.ForeignKey(Client, related_name="costumes")
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Pertains to Costume
#Waiting on list from Jeff
class TimePeriod(models.Model):
    costume = models.OneToOneField(Costume, related_name="time_period")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Pertains to Costume
class Size(models.Model):
    xxsmall = models.BooleanField(default=False)
    xsmall = models.BooleanField(default=False)
    small = models.BooleanField(default=False)
    medium = models.BooleanField(default=False)
    large = models.BooleanField(default=False)
    xlarge = models.BooleanField(default=False)
    xxlarge = models.BooleanField(default=False)
    xxxlarge = models.BooleanField(default=False)
    xxxxlarge = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Pertains to Costume
class Shows(models.Model):
    costumes = models.ManyToManyField(Costume, related_name="shows")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
