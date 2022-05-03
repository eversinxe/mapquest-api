# jacob dinapoli
# professor sitterly
# CSI-180-01/02
# april 25th, 2022
# final project

# In this project the user will input their origin and destination:
# the code will return with correct directions and the distance between each step in the process;
# it will also return the total distance.

# imports
import requests

# mapquest key
consumer_key = 'r9YWFqEpiTCMPaNsfvTHuYXpHJGfz0EJ'

# this is the url used to gather the information
# this is the url used to gather the information
url = 'https://www.mapquestapi.com/directions/v2/route?outFormat=json&ambiguities=ignore&routeType=fastest&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false'
time_url = 'http://open.mapquestapi.com/directions/v2/pathfromroute'


# this is where the user inputs their origin and destination
origin = input('Please input your origin: ')
destination = input('Please input your destination: ')
print()

#this is the method where the key is incorporated
params = {'key': consumer_key,
          'from': origin,
          'to': destination}


response = requests.get(url, params)
data = response.json()
dists = []

for step in data['route']['legs'][0]['maneuvers']:
    print(step['narrative'])
    dists.append(step['distance'])

# this will print out the distance each leg is and the total distance
print(dists)
print(round(sum(dists), 3))  # Continuation of another option
