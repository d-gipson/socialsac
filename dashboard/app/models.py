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
    address = models.CharField(max_length=75)

    AVAILABILITY = (
            ('O', 'Open'),
            ('P', 'Partial'),
            ('C', 'Closed'),
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
# address="",
# availability="",
# date_updated="",
# phone="",
# email="")
#
# record.save()