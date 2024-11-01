import requests  # Импортируем библиотеку requests для работы с HTTP-запросами

img = "https://r.mradx.net/pictures/00/7D572F.jpg"  # Здесь указываем URL изображения, которое хотим скачать

response = requests.get(img)  # Выполняем GET-запрос к указанному URL для загрузки изображения

# Открываем файл "test.jpg" в режиме записи байтов ("wb")
# и записываем туда содержимое загруженного изображения
with open("test.jpg", "wb") as file:
    file.write(response.content)  # Записываем байтовое содержимое ответа в файл
