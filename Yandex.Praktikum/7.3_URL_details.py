user_query = 'как стать бэкенд-разработчиком'

url = 'https://yandex.ru/search/?text='
uq = user_query.split(' ')
user_query = '%20'.join(uq)
url = url + user_query
print(url)