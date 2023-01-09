# import module
from geopy.geocoders import Nominatim

# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")


def name_loction(name):
    location = geolocator.geocode(name)
    lat = location.latitude
    lon = location.longitude
    l = geolocator.reverse(str(lat)+","+str(lon))
    address = l.raw['address']
    ans = {
        'lat' : lat,
        'lon' : lon,
        'address': address
    }
    return ans


#a = name_loction('trichy')
#print(a['lat'])


def loction_name(Latitude,Longitude):
    l = geolocator.reverse(str(Latitude)+","+str(Longitude))
    address = l.raw['address']
    ans = {
        'city': address['city'],
        'state': address['state'],
        'country': address['country'],
        'postcode': address['postcode']
    }
    return ans

#a = loction_name(10.7905,78.7047)
#print(a['city'])




"""# Latitude & Longitude input
Latitude = "28.6517178"
Longitude = "77.2219388"
 
location = geolocator.reverse(Latitude+","+Longitude)
 
# Display
print(location)


address = location.raw['address']
print(address)


city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
code = address.get('country_code')
zipcode = address.get('postcode')
print('City : ',city)
print('State : ',state)
print('Country : ',country)
print('Zip Code : ', zipcode)


#geolocator = Nominatim(user_agent="MyApp")

location = geolocator.geocode("delli")

print("The latitude of the location is: ", location.latitude)
print("The longitude of the location is: ", location.longitude)"""


