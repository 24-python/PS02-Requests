import requests  # Импортируем модуль requests для выполнения HTTP-запросов
import pprint    # Импортируем модуль pprint для форматированного вывода данных

# Создаем словарь с параметрами запроса, где 'q' — это параметр поиска
params = {
    'q': 'JavaScript'  # Ищем репозитории, связанные с JavaScript
}

# Отправляем GET-запрос к API GitHub для поиска репозиториев с указанными параметрами
response = requests.get('https://api.github.com/search/repositories', params=params)

# Преобразуем ответ в JSON-формат и сохраняем в переменную response_json
response_json = response.json()

# Закомментированная строка для вывода полного JSON-ответа в удобочитаемом виде
# pprint.pprint(response_json)

# Выводим количество найденных репозиториев, используя значение из JSON-ответа
print(f'Количество репозиториев: {response_json["total_count"]}')
