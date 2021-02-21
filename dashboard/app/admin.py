# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from .models import Shelter, Freedge, C19TestSite, C19VaccSite

admin.site.register(Shelter)
admin.site.register(Freedge)
admin.site.register(C19TestSite)
# admin.site.register(C19VaccSite)

class ShelterAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }