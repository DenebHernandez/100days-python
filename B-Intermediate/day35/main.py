import requests

key = ''
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'


weather_params = {
    'lat': 10.078186,
    'long': -84.085420,
    'appid': key
}

response = requests.get(OWM_ENDPOINT, params=weather_params)

print(response.status_code)
