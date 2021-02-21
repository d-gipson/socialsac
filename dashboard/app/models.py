# -*- encoding: utf-8 -*-

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django_google_maps import fields as map_fields

class Shelter(models.Model):

    AVAILABILITY = (
            ('y', 'yes'),
            ('s', 'some'),
            ('n', 'no'),
        )

    name = models.CharField(max_length=75)
    address = map_fields.AddressField(max_length=75)
    location = map_fields.GeoLocationField(max_length=75)
    availability = models.CharField(max_length=1, choices=AVAILABILITY)
    date_updated = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=45, default='')
    email = models.EmailField(max_length=254, default='')

    class Meta:
        ordering = ['availability']

    def __str__(self):
        return self.name

class Freedge(models.Model):

    AVAILABILITY = (
            ('y', 'yes'),
            ('s', 'some'),
            ('n', 'no'),
        )

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    location = models.CharField(max_length=100, default='n/a')
    availability = models.CharField(max_length=1, choices=AVAILABILITY)
    date_updated = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=45, default='')

    class Meta:
        ordering = ['availability']

    def __str__(self):
        return self.name

class C19TestSite(models.Model):

    AVAILABILITY = (
            ('y', 'yes'),
            ('s', 'some'),
            ('n', 'no'),
        )

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    location = models.CharField(max_length=100, default='n/a')
    availability = models.CharField(max_length=1, choices=AVAILABILITY)
    date_updated = models.DateTimeField(default=timezone.now)
    link = models.CharField(max_length=200,default="https://www.projectbaseline.com/studies/covid-19/eligibility/")

    class Meta:
        ordering = ['availability']

    def __str__(self):
        return self.name

class C19VaccSite(models.Model):

    AVAILABILITY = (
            ('y', 'yes'),
            ('s', 'some'),
            ('n', 'no'),
        )

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    location = models.CharField(max_length=100, default='n/a')
    availability = models.CharField(max_length=1, choices=AVAILABILITY)
    date_updated = models.DateTimeField(default=timezone.now)
    link = models.CharField(max_length=200,default="https://myturn.ca.gov/landing")


    class Meta:
        ordering = ['availability']

    def __str__(self):
        return self.name
