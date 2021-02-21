# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import requests
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from decouple import config
from .models import Shelter, Freedge, C19TestSite, C19VaccSite

#@login_required(login_url="/login/")
def index(request):

    url_OW_current = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + config('OPEN_WEATHER_API_KEY')
    url_OW_forecast = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&appid=' + config('OPEN_WEATHER_API_KEY')
    city = 'Sacramento'

    weatherCurrent = requests.get(url_OW_current.format(city)).json()
    weatherForecast = requests.get(url_OW_forecast.format(city)).json()

    #weatherCurrent = json.loads(weatherCurrent)
    #weatherForecast = json.loads(weatherForecast)

    weatherCurrent = weatherCurrent['main']['feels_like']

    weatherForecast_dict = {}
    for datapoint in weatherForecast['list']:
        new = { datapoint['dt'] : datapoint['main']['feels_like'] }
        weatherForecast_dict.update(new)

    num_shelters = Shelter.objects.count()
    num_shelters_avail = Shelter.objects.filter(availability='y').count()

    num_freedges = Freedge.objects.count()
    num_freedges_avail = Freedge.objects.filter(availability='y').count()

    context = {
        'segment' : 'index',
        'num_shelters' : num_shelters,
        'num_freedges' : num_freedges,
        'num_shelters_available' : num_shelters_avail,
        'num_freedges_available' : num_freedges_avail,
        'weather_current' : weatherCurrent,
        'weather_forecast' : weatherForecast_dict,

    }
    #context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

#@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
