# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 0.7.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KTQKcoJ0qJhJplp2rhT1Pf67JakUoLP6
"""

https://drive.google.com/file/d/16Cm2tgrpuDH8eIdxdSYyOsfDPqnJ3byd/view?usp=sharing

"""ФИО:"""



"""## Задание 1. HTTP-запросы, ответы и погода

Описание:

Напишите HTTP-запрос для получения информации о погоде в введенном городе из API.

Можно использовать API: https://open-meteo.com/. Используйте метод GET.


Ввод
```
56.50, 60.35
```

Вывод
```
Сегодня (1.11) погода 20 ◦С, нет осадков, туман
```
"""

import requests


data=input('Введите широту и долготу:').split(', ')

url=f'https://api.open-meteo.com/v1/forecast?latitude={data[0]}\
&longitude={data[1]}&current=temperature_2m,precipitation,weather_code'
response=requests.get(url)

status_code=response.status_code
json=response.json()


def precipitation(json):#Наличие/отсутствие осадков
    if json['current']['precipitation']==0.0:
        return 'нет осадков'
    if json['current']['precipitation']!=0.0:
        return 'есть осадки'


def fog(json):#Наличие/отсутствие тумана
    if json['current']['weather_code']==45 \
    or json['current']['weather_code']==48:
        return 'туман'
    else:
        return 'нет тумана'


print(f'Сегодня\
 ({json["current"]["time"][5:7]}.{json["current"]["time"][8:10]})\
 погода {json["current"]["temperature_2m"]} °C,\
 {precipitation(json)}, {fog(json)}')

"""## Задание 2. HTTP-запросы, ответы и покемоны

**Описание:**


Создайте код программы, которая будет взаимодействовать с API, со следующим функионалом:

1. Используя метод GET, отправьте запрос на endpoint /pokemon, чтобы получить список первых 20 покемонов

2. Извлеките имена покемонов из ответа и выведите их списком

3. Введите с помощью input() название одного из покемонов


```
Имя покемона: clefairy
```



4. Отправьте GET-запрос, чтобы получить полную информацию о выбранном покемоне

5. Извлеките и выведите следующие данные о введенном покемоне:

     • Имя

     • Тип

     • Вес

     • Рост

     • Способности

Используйте PokéAPI (https://pokeapi.co/), который предоставляет информацию о покемонах, их характеристиках, типах и другую информацию.
"""

import requests


def pokemon_list():#Получение списка первых 20 покемонов
    url='https://pokeapi.co/api/v2/pokemon/?limit=20'
    response=requests.get(url)
    json=response.json()
    return [pokemon['name'] for pokemon in json['results']]


def pokemon_info(pokemon_name):#Нахождение покемона по имени
    url=f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response=requests.get(url)
    json=response.json()
    return f'имя: {json["name"]}\n\
тип: {', '.join(map(str,[pokemon["type"]["name"] for\
pokemon in json["types"]]))}\n\
вес: {json["weight"]}\n\
рост: {json["height"]}\n\
способности: {', '.join(map(str,[pokemon['ability']['name'] for\
pokemon in json['abilities']]))}'


def main():
    print('\n',*[pokemon+'\n' for pokemon in pokemon_list()])
    pokemon_name=input('Выберите имя покемона:').lower()
    print(pokemon_info(pokemon_name))


main()
#В vscode все работает!

"""## Задание 3. HTTP-запросы, ответы и посты

**Описание:**

Создайте программу, которая будет взаимодействовать с JSONPlaceholder API, реализуя следующие функции:

1. Реализуйте функцию, которая выполняет GET-запрос к https://jsonplaceholder.typicode.com/posts и возвращает список постов в формате JSON

2. Реализуйте функцию, котороая получает вводимое ID поста, выполняет GET-запрос по ID и возвращает данные поста в формате JSON

3. Реализуйте функцию, которая выполняет обработку JSON из пункта 2 и выводит всю важную информацию в консоль
"""

import requests


def get_posts():#Возвращает список постов в формате JSON
    url=' https://jsonplaceholder.typicode.com/posts'
    response=requests.get(url)
    json=response.json()
    return json


def get_posts_by_id(id_post):#Возвращает важные данные поста по ID
    url=' https://jsonplaceholder.typicode.com/posts'
    response=requests.get(url)
    json=response.json()
    for item in json:
        if item['id']==int(id_post):
            return f'userID: {item['userId']}\n\
id: {item['id']}\n\
title: {item['title']}\n\
body: {item['body']}'


def main():
    id_post=input(f'Всего постов: {len(get_posts())}. Введите ID поста:')
    get_posts_by_id(id_post)
    print(get_posts_by_id(id_post))


main()
#В vscode все работает!

"""## Задание 4. HTTP-запросы, ответы и работа с постами

**Описание**

Создайте программу, которая будет взаимодействовать с JSONPlaceholder API (из предыдущего задания), реализуя новые функции:

1. Реализуйте функцию, которая принимает заголовок, содержимое и ID пользователя (информация вводится с помощью input()), выполняет POST-запрос для создания нового поста и возвращает информацию о созданном посте в формате JSON


```
Заголовок: Новый пост
Содержимое поста: Тут должно находиться содержимое нового поста...
ID пользователя: 10
```



2. Реализуйте функцию, которая принимает ID поста, новый заголовок и новое содержимое, выполняет PUT-запрос и возвращает обновлённый пост в формате JSON

3. Реализуйте функцию, которая принимает ID поста, выполняет DELETE-запрос и возвращает статус-код ответа
"""

import requests


def get_posts():#Возвращает список постов в формате JSON
    url=' https://jsonplaceholder.typicode.com/posts'
    response=requests.get(url)
    json=response.json()
    return json


def new_post(title,body,userId):#Создание нового поста
    url=' https://jsonplaceholder.typicode.com/posts'
    new_data={'userId': userId, 'title': title, 'body': body}
    response=requests.post(url,json=new_data)
    print('Создан новый пост:', response.json())


def change_post(id,title,body,userId):#Изменение существующего поста
    url=f'https://jsonplaceholder.typicode.com/posts/{id}'
    new_data={'userId': userId, 'id': id, 'title': title, 'body': body}
    response=requests.put(url,json=new_data)
    print(f'Обвновлен пост под номером {id}: {response.json()}')


def delete_post(id):#Удаление поста
    url=f'https://jsonplaceholder.typicode.com/posts/{id}'
    response=requests.delete(url)
    print(f'Статус-код: {response.status_code}')


def main():
    while True:
        choice=input('1) Создать новый пост\n2) Обновить уже существующий пост\
        \n3) Удалить пост\n')
        if choice=='1':
            title=input('Введите заголовок:')
            body=input('Введите содержимое поста:')
            userId=input('Введите Id пользователя:')
            new_post(title,body,userId)
        if choice=='2':
            id=input(f'Введите id в диапазоне от 1 до {len(get_posts())}:')
            if int(id) in range(1,len(get_posts())+1):
                title=input('Введите новый заголовок:')
                body=input('Введите новое содержимое поста:')
                userId=input('Введите новый Id пользователя:')
                change_post(id,title,body,userId)
            else:
                print('Поста с таким id нет.')
        if choice=='3':
            id=input(f'Введите id в диапазоне от 1 до {len(get_posts())}:')
            if int(id) in range(1,len(get_posts())+1):
                delete_post(id)
            else:
                print('Поста с таким id нет.')


main()

"""## Задание 5. HTTP-запросы, ответы и пёсики

**Описание**

Создайте программу, которая будет взаимодействовать с Dog API, которая позволит получать список пород собак, вводить несколько пород и получать их фотогрфии.

Этапы:

1. Создайте функцию, которая использует метод GET и возвращает список всех пород собак в формате нумерованного списка

2. Реализуйте возможность ввода нескольких пород собак через запятую


```
african, chow, dingo
```



3. Создание функции, которая реализует запрос, возвращает и выводит изображениия собак, породы которых были введены до этого


Используйте Dog API (https://dog.ceo/dog-api/), который предоставляет информацию о породах собак и их изображения.
"""

import requests


def dogs_list():#Выводит список пород
    url='https://dog.ceo/api/breeds/list/all'
    response=requests.get(url)
    json=response.json()
    cnt=0
    for breed in json['message']:
        cnt+=1
        print(f'{cnt}) {breed}')


def dog_breed(breed):#Выводит
    breeds=breed.split(',')
    for breed in range(len(breeds)):
        url=f'https://dog.ceo/api/breed/{breeds[breed]}/images/random'
        response=requests.get(url)
        json=response.json()
        print(f'Изображение породы {breeds[breed]}: {json['message']}')


def main():
    dogs_list()
    breed=input('Введите породу(породы) из списка:')
    dog_breed(breed)


main()
#В vscode все работает!