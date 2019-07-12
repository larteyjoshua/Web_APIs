import tweepy
import pyowm
import time


owm=pyowm.OWM('2e26b43d8673cfe8f80d56157c2ba6c3')
observation= owm.weather_at_place('London,UK')
w=observation.get_weather()

w.get_wind()['speed']
w.get_humidity()
w.get_temperature()['temp']
tem =w.get_temperature()['temp']
speed= w.get_wind()['speed']

# Authenticate to Twitter
auth = tweepy.OAuthHandler("Jm5axFFsnfo2Erf30FRea4yuI", "ITQG0lm3oCbHaSg0fmiSliVAjs9iw0UcigFFvVf7COgOH5hX1v")
auth.set_access_token("133000414-aIJiWnc2GjUgC46fuxhUARP6V0wDnkc2HSqseehd", "kRJ8TQ8r4ObBiGNcSiKChbar8rqMf0sRO6TnXNtVBsnNX")




# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("tem=" +str(tem) + "speed="+ str(speed))
time.sleep(3600)