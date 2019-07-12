from geopy.geocoders import Nominatim
first_city = input("Please Enter the first City ")
second_city = input("Please Enter the second City ")


geolocator = Nominatim(user_agent="My Application")
location = geolocator.geocode(first_city)
first= (location.latitude, location.longitude)
print(first)


geolocator = Nominatim(user_agent="My Application")
location = geolocator.geocode(second_city)
second= (location.latitude, location.longitude)
print(second)

from geopy import distance
print("The distance between the two city is ",distance.distance(first, second).km)

