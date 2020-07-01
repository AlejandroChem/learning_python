import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
}

request_headers = {
    'Accept-Language': 'ru'
    # заполните словарь с заголовками
}

# не забудьте передать параметры и заголовки в http-запрос
# через аргументы `params` и `headers` функции get()
response = requests.get(url, headers = request_headers, params = weather_parameters)
print(response.text)