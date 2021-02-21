# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us

"""

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Shelter(models.Model):

    name = models.CharField(max_length=75)
    location = models.CharField(max_length=75)

    AVAILABILITY = (
            ('Y', 'Yes'),
            ('S', 'Some'),
            ('N', 'No'),
        )

    availability = models.CharField(max_length=1, choices=AVAILABILITY)
    date_updated = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=45)
    email = models.EmailField(max_length=254)

    class Meta:
        ordering = ['-date_updated']

    def __str__(self):
        return self.name

# creating record would look something like:
# record = Shelter(name="",
# location="",
# availability="",
# date_updated="",
# phone="",
# email="")
#
# record.save()

class Freedge(models.model):

    name = models.CharField(max_length=30)
    location = models.CharField(max_length=75)
    availability = models.CharField(max_length=1, choices=AVAILABILITY)
