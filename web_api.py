import pyowm
owm=pyowm.OWM('2e26b43d8673cfe8f80d56157c2ba6c3')
observation= owm.weather_at_place('London,UK')
w=observation.get_weather()

print (w.get_wind()['speed'])
print (w.get_humidity())
print (w.get_temperature()['temp'])

print 
