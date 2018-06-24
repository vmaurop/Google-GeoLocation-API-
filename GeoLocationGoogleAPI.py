# importing only the necessary for memory saving
from urllib.request import urlopen as OPEN
from urllib.parse import urlencode as ENCODE
from xml.etree import ElementTree as XML

# the location of Google's geolocation API
api_url = 'http://maps.googleapis.com/maps/api/geocode/xml?'

#input
address = input('Enter location: ')

# if no address specified, my Home
if len(address) == 0:
    address = "Cholargos, Greece"

# UTF-8 format
url = api_url + ENCODE({'sensor': 'false', 'address': address})

# getting that data
# print Get locatation for input address and open url for read
print ('\nGet location for:', address)
data = OPEN(url).read()

# digging into the XML tree
tree = XML.fromstring(data)

# let's see the results
results = tree.findall('result')


#try- for invalid input address
try:
    # dig into the XML tree to find latitude and longitude
    latitude = results[0].find('geometry').find('location').find('lat').text

    longitude = results[0].find('geometry').find('location').find('lng').text



    latitude = float(latitude)
    longitude = float(longitude)

    # format the coordinates to a more appealing form
    if latitude < 0:
        lat_c = chr(167) + 'S'
    else:
        lat_c = chr(167) + 'N'
    if longitude < 0:
        lng_c = chr(167) + 'W'
    else:
        lng_c = chr(167) + 'E'

    # location holds the geomap unit found by API, based on user input, e.x. approximately
    location = results[0].find('formatted_address').text
    location_type = results[0].find('geometry').find('location_type').text

    # the location of Google Places API
    url = 'http://maps.googleapis.com/maps/api/place/details/xml?'


    data = OPEN(url).read()
    tree = XML.fromstring(data)
    results = tree.findall('status')[0].text


    #print the reults, Latitude, Longitude, Location type
    print("\n", location)
    print('Latitude: {0:.5f}{1}'.format(abs(latitude), lat_c))
    print('Longitude: {0:.5f}{1}'.format(abs(longitude), lng_c))
    print('Location type:', location_type)


    #exception
except Exception as e:
    print("Invalid input address..Please try again")



