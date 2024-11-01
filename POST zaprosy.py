import requests

url = ""

data = {
    "title": "тестовый заголовок post запроса",
    "body": "тестовый контент post запроса",
    "userId": 2
    }

response = requests.post(url, data=data)

print(response.status_code)

print(f"текст ответа  - {response.json()}")

