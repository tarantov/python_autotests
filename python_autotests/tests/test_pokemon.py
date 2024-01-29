# Импорт библиотек 
import requests
import pytest 
# Создаю переменные и через рановно, назначаю им значения. 2 знака равно - приравнивание. 
URL = 'https://api.pokemonbattle.me:9104'
HEADER =  {
    'Content-Type': 'application/json'
}
# Обязательное условие для названия тестов - в начале test_... 
# Название документа с тестом должно начинаться с test, а заканчиваться на ".py"
# def - описание тестовой функции 
# Важно сохранять табуляцию
def test_get_trainers():
    """
    GR-1. Get trainers id, status 
    """
    response=requests.get(url = f'{URL}/trainers', params={'trainer_id': 4718})
    assert response.status_code == 200, 'Неожиданный статус код'
    

def test_get_trainers_id():
    """
    GR-1. Get trainers, true id
    """
    # Базовый реквест с квери параметром = params 
    response=requests.get(url = f'{URL}/trainers', params={'trainer_id': 4718})
    # Что бы сосластся на клшюч в JSON его ключ и значение нужно записать в кавычках ''
    # Вместо if,else используется assert
    # assert = Я удтверждаю что ..... равен ... , если это не так, то ....
    assert response.json()['id'] == '4718', ''
 
  