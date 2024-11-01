import requests  # Импортируем модуль requests для работы с HTTP-запросами
import pprint  # Импортируем модуль pprint для красивого вывода данных

# Отправляем GET-запрос на указанный URL и сохраняем ответ в переменной response
response = requests.get('https://api.github.com')

# Распечатываем статусный код ответа
# print(response.status_code)

# Проверяем, успешно ли выполнен запрос
# if response.ok:
#     print("Запрос успешно выполнен")  # Если да, выводим сообщение об успехе
# else:
#     print("Запрос не удался")  # Если нет, выводим сообщение о неудаче

# Выводим текст ответа
# print(response.text)

# Выводим содержимое ответа в формате байтов
# print(response.content)

# Выводим JSON-объект, полученный из ответа
# print(response.json)

# Преобразуем ответ в JSON-формат и сохраняем в переменной response_json
response_json = response.json()

# Выводим JSON-объект в удобочитаемом формате с помощью pprint
pprint.pprint(response_json)
