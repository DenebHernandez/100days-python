import requests
from datetime import datetime

PIXELA_ENDPOINT = 'https://pixe.la'
TOKEN = 'ghgsl7Gg73Ss8'

def create_graph(id: str, name: str, unit: str, data_type: str, color: str):

    graph_config = {
       'id': id,
       'name': name,
       'unit': unit,
       'type': data_type,
       'color': color
    }

    headers = {
        'X-USER-TOKEN': TOKEN
    }

    temp_response = requests.post(url=f'{PIXELA_ENDPOINT}/v1/users/denebhdz/graphs', json=graph_config, headers=headers)

    return temp_response


def add_pixel(graph_id: str, date: str, quantity: str):

    pixel_config = {
       'date': date,
       'quantity': quantity
    }

    headers = {
        'X-USER-TOKEN': TOKEN
    }

    temp_response = requests.post(url=f'{PIXELA_ENDPOINT}/v1/users/denebhdz/graphs/{graph_id}', json=pixel_config, headers=headers)

    return temp_response

# params = {
#     'token': TOKEN,
#     'username': 'denebhdz',
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes'
# }

# response = requests.post(url=f'{PIXELA_ENDPOINT}/v1/users', json=params)

# response = requests.get(url=f'{PIXELA_ENDPOINT}/@denebhdz')

# test = create_graph(id='graph1', name='Test graph', unit='km', data_type='int', color='sora')
# print(test.text)

current_day = datetime.now()
 
formatted_date = current_day.strftime("%Y%m%d")
print(formatted_date)

test = add_pixel(graph_id='graph1', date=formatted_date , quantity='2')
print(test.text)
