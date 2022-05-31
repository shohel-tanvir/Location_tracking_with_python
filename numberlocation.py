# -*- coding: utf-8 -*-
"""
Created on Mon May 30 23:21:59 2022

@author: 88017
"""
import phonenumbers

number="+8801792854428"

from phonenumbers import geocoder
key='d906e702a1a4498fbfbcca10169348b8'

samnumber=phonenumbers.parse(number)
mylocation=geocoder.description_for_number(samnumber, "en")
print(mylocation)

from phonenumbers import carrier

service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode 

geocoder=OpenCageGeocode(key)
query=str(mylocation)
result=geocoder.geocode(query)
## print(result)

lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']

print(lat,lng)
