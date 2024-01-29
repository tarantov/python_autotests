"""
Reqests for API on PYTHON  
"""
# Импортирую библиотеку с которой работаю 
import requests 

URL = 'https://api.pokemonbattle.me:9104'
HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': 'ed12e04103db5c5894b9fdecac939595'
}

HEADERS1 = {
    'Content-Type': 'application/json'
}
# Тут создал три разных переменных, для разных запросов
BODY = {
    "name": "autotest",
    "photo": "https://dolnikov.ru/pokemons/albums/002.png"
}

BODY2 = {
    "pokemon_id": "28342",
    "name": "Popo",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

BODY3 = {
    "pokemon_id": "28342"
}
# # Получаю ответ в Json
# # Создаю пост запрос, черес "Ф" строку сохроняю ответ в JSON и выделяю только ключ "message"
response=requests.post(url = f'{URL}/pokemons', json= BODY, headers= HEADERS)
print(f'Ответ: {response.json()['message']}. Статус код: {response.status_code}')

# Запрашиваю список покемонов, моего тренера 
# В начале запустил запрос через "DeBug", посмотрел какие есть коючи у JSON и через переменную с точкой указал ключ JSON
response1=requests.get(url = f'{URL}/pokemons', headers= HEADERS1, params={'trainer_id': 4718})
print(f'ID Первого покемона: {response1.json()[0]['id']}. Статус покебола: {response1.json()[0]['in_pokeball']}')
print(f'ID Второго покемона: {response1.json()[1]['id']}. Статус покебола: {response1.json()[1]['in_pokeball']}')
print(f'ID Третьего покемона: {response1.json()[2]['id']}. Статус покебола: {response1.json()[2]['in_pokeball']}')
print(f'ID Четвертого покемона: {response1.json()[3]['id']}. Статус покебола: {response1.json()[3]['in_pokeball']}')
print(f'ID Пятого покемона: {response1.json()[4]['id']}. Статус покебола: {response1.json()[4]['in_pokeball']}') 
print(f'Статус код: {response1.status_code}')


# Меняю имя покемона 
response2=requests.put(url = f'{URL}/pokemons',json= BODY2, headers= HEADERS)
print(f'Ответ: {response2.json()['message']}. Статус код: {response2.status_code}')

# Поймать покемона в покебол 
response3=requests.post(url = f'{URL}/trainers/add_pokeball',json= BODY3, headers= HEADERS)
print(f'Ответ: {response3.json()['message']}. Статус код: {response3.status_code}')

