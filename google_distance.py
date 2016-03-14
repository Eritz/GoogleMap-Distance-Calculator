#! python3
# google_distance.py - uses Google maps to display the distance between two areas

import requests, json, os
api = 'YOURAPIHERE'

# Setting the locations
location_a = input('Enter the starting location:\n')
location_b = input('Enter the destination:\n')

# Output for the user
print()
print('Calculating...')
print()

# Downloads the json data
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&units=imperial&key=%s' %(location_a, location_b, api)
resurl = requests.get(url)
resurl.raise_for_status()

# Load the json data
dist = json.loads(resurl.text)

# Print the results
d = dist['rows'][0]['elements'][0]

print('The distance between "%s" and "%s":' %(location_a, location_b))
print(d['distance']['text'])
print()
print('It is approximately:')
print(d['duration']['text'] + ' by car')
