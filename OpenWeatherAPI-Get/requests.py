import requests

#GET by location request
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={APIkey}')
if response.status_code == 200:
    data = response.json()
    #print(data)
else:
    print('Error:', response.status_code)

#add try catch

temperature = data['main']['temp']
humidity = data['main']['humidity']
desc = data['weather'][0]['description']