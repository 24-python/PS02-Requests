import requests
import pprint

response = requests.get('https://api.github.com')
# print(response.status_code)
#
# if response.ok:
#     print("Запрос успешно выполнен")
# else:
#     print("Запрос не удался")

#print(response.text)

#print(response.content)

#print(response.json)

response_json = response.json()
#print(response_json)

pprint.pprint(response_json)
