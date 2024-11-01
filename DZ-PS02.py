import requests
import pprint

#Задание 1: Получение данных

response = requests.get('https://api.github.com/search/repositories', params={'q': 'html'})

response_json = response.json()

print(response.status_code)

print(f'Количество репозиториев: {response_json["total_count"]}')

#Задание 2: Параметры запроса

response = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': 1})

response_json = response.json()

pprint.pprint(response_json)

#Задание 3: Отправка данных

response = requests.post('https://jsonplaceholder.typicode.com/posts', data={'title': 'foo', 'body': 'bar', 'userId': 1})

response_json = response.json()

print(response.status_code)

pprint.pprint(response_json)
