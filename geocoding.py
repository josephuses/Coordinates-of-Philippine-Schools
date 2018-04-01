#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 16:58:12 2018

@author: josephuses
"""

#!/usr/bin/env python
import pandas as pd
from gmaps import Geocoding
# Use your own api key by registering at https://console.cloud.google.com/apis/credentials?project=starlit-woods-175707
api = Geocoding(api_key = 'Your api key')

# import the data
data = pd.read_csv("data.csv")
# make a list of the addresses in data['address']
# change the index as desired
# remember that you are only limited to 2500 queries in a day
address = data['address'][:1000].tolist()
# initialize the location list
location = []
# Download the geocodes for each school address
for place in address:
    try:
        location.append(api.geocode(place))
    except Exception as e:
        location.append("No Result")

# Initialize the lat (latitude) and long (longitude) lists
lat = []
long = []
# Get the number of schools in the list
n_address = len(address)
# loop through the addresses and store the lat and long values
# a value of 0 means that there is no match from the query
for i in list(range(n_address)):
    if type(location[i]) is list:
        lat.append(location[i][0]['geometry']['location']['lat'])
        long.append(location[i][0]['geometry']['location']['lng'])
    else:
        lat.append(0.0)
        long.append(0.0)

# create a slic of the data
# index the name of the slice as necessary
data3 = data[2000:3000]
lat = pd.Series(lat)
data3['latitude'] = lat.values
long = pd.Series(long)
data3['longitude'] = long.values
# save result to a csv file
data3.to_csv('data3py.csv')