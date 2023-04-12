import requests

cityName = input('Choose a location (by city): ')

APIkey = 'd43fa3449113ba8f1b2b43193a35444e'

data = None

#GET by location request
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={APIkey}')
if response.status_code == 200:
    data = response.json()
    #print(data)
else:
    print('Error:', response.status_code)

temperature = data['main']['temp']
humidity = data['main']['humidity']
desc = data['weather'][0]['description']

print(f'Temperature in {cityName} is {temperature} with a humidity of {humidity} and can be described as \"{desc}\"')
