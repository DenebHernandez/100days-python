import requests

parameters = {
    'amount': 10,
    'type': 'boolean'
}

response = requests.get('https://opentdb.com/api.php', params=parameters)

if response.status_code == 200:
    data = response.json()
    # print(data)
    question_data = data['results']
