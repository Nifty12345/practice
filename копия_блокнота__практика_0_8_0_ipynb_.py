# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 0.8.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BnWMpx1Ro05QdCINoT8J6DZZUe3sHARa

# Задание 1

Задача: Создать чат бота для получения информации об исследованиях космоса

Описание: Создайте комплексное приложение командной строки, которое будет использоваться в качестве панели управления исследованиями космоса. Данное приложение будет обращаться к https://api.nasa.gov/ для предоставления пользователям набора информации о космосе, включая:

- Астрономическая картинка дня (APOD): Отображение APOD с пояснениями к нему.
- Фотографии с марсохода: позволяет пользователям выбирать и фильтровать фотографии с марсохода по дате и типу камеры.
- Объекты, сближающиеся с Землей (ОСЗ): Поиск и отображение информации об объекте, сближающихся с Землей, на определенную дату, включая их размеры и потенциальную опасность.
- Данные о космической погоде: Отображают последние данные о космической погоде, включая солнечные вспышки и геомагнитные бури.
Приложение должно позволять пользователям ориентироваться в этих функциях, корректно обрабатывать ошибки и обеспечивать удобство работы.

Требования:
- Пользовательский ввод: Приложение должно предложить пользователю ввести данные, чтобы выбрать, какую функцию он хочет изучить.
- Проверка данных: Убедитесь, что пользовательские данные (например, даты) проверены.
- Обработка ошибок: Корректно обрабатывайте ошибки API и неверные ответы.
- Представление данных: Представляйте данные в четкой и организованной форме.
- Опция выхода: позволяет пользователям выходить из приложения в любое время.
"""

import datetime
import requests

# Проверка правильности введеной пользователем даты
def check_date(date):
    try:
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except:
        return False

# Информация об астрономической фотографии дня
def get_APOD(api_key):
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
    response=requests.get(url)
    if response.status_code == 200:
        json = response.json()
        print(f'Сегодня {json["date"]} астрономической фотографией дня был объявлен снимок: {json["url"]}.\n\
Текст: {json["explanation"]}')
    else:
        print('Кажется, произошла ошибка :(')

# Список фото с марсохода по дате и типу камеры
def get_Mars_Rover_Photos(date, camera, api_key):
    cameras = ['fhaz','rhaz','mast','chemcam','mahli','mardi','navcam','pancam','minites']
    if camera not in cameras:
        print('Такой камеры нет. Попробуйте заново.')
    else:
        url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&camera={camera}&api_key={api_key}'
        response=requests.get(url)
        if response.status_code == 200:
            print(f'Фотографии за {date} с камеры {camera}:')
            json=response.json()
            cnt=0
            for photo in range(len(json['photos'])):
                cnt += 1
                print(f'{cnt}) {json['photos'][photo]['img_src']}')
            if cnt == 0:
                print('К сожалению, таких фото нет.')
            print('')
        else:
            print('Кажется, произошла ошибка :(')

# Информация о космических объектах за указанную дату, их размер и опасность
def get_Asteroids(date, api_key):
    url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={date}&end_date={date}&api_key={api_key}'
    response=requests.get(url)
    if response.status_code == 200:
        print(f'Ближайшие к земле объекты на момент {date}:')
        json = response.json()
        for object in range(int(json['element_count'])):
            print(f'Имя астероида: {json['near_earth_objects'][date][object]['name']}\n\
Минимальный размер астероида: {json['near_earth_objects'][date][object]['estimated_diameter']['meters']['estimated_diameter_min']} метров(метра).\n\
Максимальный размер астероида: {json['near_earth_objects'][date][object]['estimated_diameter']['meters']['estimated_diameter_max']} метров(метра).\n\
Опасность астероида для Земли: {json['near_earth_objects'][date][object]['is_potentially_hazardous_asteroid']}\n')

# Информация о недавних магнитных бурях и солнечных вспышках
def get_space_weather(date,api_key):
    url = f'https://api.nasa.gov/DONKI/GST?endDate={date}&api_key={api_key}'
    url2 = f'https://api.nasa.gov/DONKI/FLR?endDate={date}&api_key={api_key}'
    response=requests.get(url)
    response2=requests.get(url2)
    if response.status_code == 200:
        json = response.json()
        json2 = response2.json()
        cnt = 0
        cnt2 = 0
        print('Магнитные бури за последнее время:')
        for index in range(len(json[0]['allKpIndex'])):
            cnt += 1
            print(f'{cnt}) Время магнитной бури: {','.join((json[0]['allKpIndex'][index]['observedTime']).split('T'))[:-1]}')
            print(f'Сила магнитной бури: {(json[0]['allKpIndex'][index]['kpIndex'])}/9\n')
        print('Солнечные вспышки за последнее время:')
        for item in json2:
            cnt2 += 1
            try:
                print(f'{cnt2}) ID: {item['flrID']};\nНачало: {','.join(item['beginTime'].split('T'))[:-1]};\nКонец: {','.join(item['endTime'].split('T'))[:-1]};')
            except:
                print(f'{cnt2}) ID: {item['flrID']};\nНачало: {','.join(item['beginTime'].split('T'))[:-1]};\nКонец: {item['endTime']};')
            if len(item['note']) != 0:
                print(f'Заметка: {item['note']}\n')
            else:
                print('Заметка: None\n')


def main():
    print('Добро пожаловать! Выберите номер нужной функции:')
    while True:
        choice = input('1) Посмотреть астрономическую фотографию дня.\n\
2) Посмотреть фотографии с марсохода.\n\
3) Данные об объектах, сближающихся с Землей.\n\
4) Данные о космической погоде.\n\
5) Выход\n')
        if choice == '1':
            api_key = input('Введите ключ api:')
            get_APOD(api_key)
        if choice == '2':
            api_key = input('Введите ключ api:')
            date = input('Введите дату в формате YYYY-MM-DD:')
            if check_date(date) == True:
                print('FHAZ,RHAZ,MAST,CHEMCAM,MAHLI,MARDI,NAVCAM,PANCAM,MINITES')
                camera = input('Введите вид камеры из списка выше:').lower()
                get_Mars_Rover_Photos(date, camera,api_key)
            else:
                print('Неправильно введена дата. Попробуйте еще раз.')
        if choice == '3':
            api_key = input('Введите ключ api:')
            date = input('Введите дату в формате YYYY-MM-DD:')
            if check_date(date) == True:
                get_Asteroids(date, api_key)
            else:
                print('Неправильно введена дата. Попробуйте еще раз.')
        if choice == '4':
            api_key = input('Введите ключ api:')
            date = str(datetime.datetime.now())[:10]
            if check_date(date) == True:
                get_space_weather(date, api_key)
        if choice == '5':
            print('Сеанс завершен')
            break


main()

"""# Задание 2

Описание задачи

Цель этой задачи - создать скрипт на Python, который взаимодействует с API Чикагского института искусств (https://api.artic.edu/docs/) для извлечения и отображения произведений искусства. Скрипт должен позволять пользователям просматривать работы по страницам, фильтровать их по имени художника и просматривать подробную информацию о выбранных произведениях искусства. Ниже приведены требования и функциональные возможности, которые необходимо реализовать:

Требования:
Извлекать произведения искусства:

- Создайте функцию, которая извлекает список произведений искусства из API Чикагского института искусств.
Функция должна принимать параметр page для разбивки на страницы и возвращать список произведений искусства вместе с информацией о разбивке на страницы.
Фильтровать произведения искусства:

- Реализуйте функцию, которая фильтрует список произведений искусства на основе имени указанного художника. Функция должна возвращать список работ, которые соответствуют имени художника (без учета регистра).
Отображать подробную информацию об оформлении:

- Напишите функцию, которая отображает названия работ для пользователя и позволяет ему выбрать одну из них, введя соответствующий номер.
После выбора функция должна отображать подробную информацию о выбранном произведении, включая название, исполнителя, дату и носитель.
Разбивка на страницы и взаимодействие с пользователем:

- Создайте основную функцию, которая управляет выборкой произведений и взаимодействием с пользователем.

Разрешите пользователям перемещаться по страницам с произведениями искусства, выполнять фильтрацию по исполнителю или выходить из программы.

Если страниц с произведениями искусства несколько, укажите варианты перехода к следующей странице, предыдущей странице, фильтрации по исполнителю или выхода из программы.
"""

import requests

# Выводит информацию о произведению искусства по ID
def get_art_by_id(id):
    url = f'https://api.artic.edu/api/v1/artworks/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        json = response.json()
        print(f'Автор: {json['data']['artist_title']}\n\
Название произведения: {json['data']['title']}\n\
Дата начала создания: {json['data']['date_start']}\n\
Дата конца создания: {json['data']['date_end']}\n\
Носитель: {', '.join(json['data']['material_titles'])}')

# Выводит список работ по страницам с их ID, автором и названием
def get_list(page):
    url = f'https://api.artic.edu/api/v1/artworks?page={page}'
    response = requests.get(url)
    if response.status_code == 200:
        json = response.json()
        cnt = 0
        print(f'Страница {page}/10527')
        for art in json['data']:
            cnt += 1
            print(f'{cnt}) ID произведения: {art['id']}\n\
Название произведения: {art['title']}\n\
Автор: {art['artist_title']}\n')

#Выводит спиоск работ выбранного автора
def get_artist_by_name(name):
    url = f'https://api.artic.edu/api/v1/artworks/search?q={name}'
    response = requests.get(url)
    if response.status_code == 200:
        json = response.json()
        print(f'Работы автора {name}:')
        for artwork in json['data']:
            print(f'Название работы: {artwork['title']}, \
ID работы: {artwork['id']}')


def main():
    print('Добро пожаловать! Выберите дейсвие:')
    while True:
        choice = input('1) Список произведений искусства\n\
2) Фильтрация по создателю\n\
3) Выход\n')
        if choice == '1':
            while True:
                print('Для выхода из режима введите в поле для выбора страницы "exit".\n\
Для того, чтобы узнать информацию о произведении пр ID, введите в поле для выбора страницы "ID".')
                page=input('Выберете страницу от 1 до 10527:').lower()
                if page == 'exit':
                    break
                if page == 'id':
                    id=input('Введите ID нужного произведения:')
                    get_art_by_id(id)
                    break
                try:
                    if int(page) in range(1,10528):
                        get_list(page)
                    else:
                        print('Некорректный номер страницы.')
                except:
                    print('Некорректный номер страницы.')
        if choice == '2':
            name = input('Введите автора:')
            get_artist_by_name(name)
        if choice == '3':
            print('Сеанс окончен.')
            break


main()

"""# Задание 3

Задача: Создать программу по управлению портфелем криптовалют

Цель: Создать скрипт на Python, который извлекает цены на криптовалюты в режиме реального времени, позволяет пользователям управлять портфелем криптовалют, вычисляет общую стоимость портфеля, отслеживает изменения цен и предоставляет исторические данные о ценах для анализа.

Требования:
Получение текущих цен на криптовалюты:

Используйте https://docs.coingecko.com/ для получения актуальных цен на список криптовалют.

Управление портфелем:

- Позволяет пользователю создавать портфель криптовалют и управлять им, указывая количество каждой криптовалюты, которой он владеет.
- Расчитывает общую стоимость портфеля в указанной фиатной валюте (например, долларах США).

Отслеживание изменения цен:

- Отображение процентного изменения цены для каждой криптовалюты в портфеле за последние 24 часа.
- Выделите все криптовалюты, стоимость которых значительно увеличилась или снизилась.

Поиск исторических данных о ценах:

- Получение исторических данных о ценах на указанную криптовалюту за последнюю неделю.
- Предоставьте пользователю возможность визуализировать эти данные в простом текстовом формате (например, цены за день).

Взаимодействие с пользователем:

- Реализуйте интерфейс командной строки для ввода данных пользователем.
- Предоставьте опции для получения текущих цен, управления портфелем, просмотра изменений цен или анализа исторических данных.
"""

import requests
import datetime

cryptocurrency_bag = {}

# Портфель с криптовалютой, полной стоимостью, изменением за последние 24 часа
def get_cryptocurrency_bag():
    if len(cryptocurrency_bag) != 0:
        full_cost = 0
        for coin, amount in cryptocurrency_bag.items():
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd&include_24hr_change=true&x_cg_demo_api_key=CG-AVBFDUPDA8SrMQKT1qytuwaE"
            response = requests.get(url)
            json = response.json()
            if response.status_code == 200:
                # Оценка изменения цены криптовалюты за последние 24 часа
                if json[coin]['usd_24h_change'] >= 10:
                    print(f'{coin}: {int(amount) * int(json[coin]['usd'])}$. \
Изменение цены за последние 24 часа: {json[coin]['usd_24h_change']}% \
- ЗНАЧИТЕЛЬНОЕ ИЗМЕНЕНИЕ ЗА ПОСЛЕДНИЕ 24 ЧАСА ↑')
                    full_cost += int(amount) * int(json[coin]['usd'])
                if json[coin]['usd_24h_change'] <= -10:
                    print(f'{coin}: {int(amount) * int(json[coin]['usd'])}$. \
Изменение цены за последние 24 часа: {json[coin]['usd_24h_change']}% \
- ЗНАЧИТЕЛЬНОЕ ИЗМЕНЕНИЕ ЗА ПОСЛЕДНИЕ 24 ЧАСА ↓')
                    full_cost += int(amount) * int(json[coin]['usd'])
                if -10 <= json[coin]['usd_24h_change'] <= 10:
                    print(f'{coin}: {int(amount) * int(json[coin]['usd'])}$. \
Изменение цены за последние 24 часа: {json[coin]['usd_24h_change']}%')
                    full_cost += int(amount) * int(json[coin]['usd'])
        print(f'ПОЛНАЯ СТОИМОСТЬ ПОРТФЕЛЯ: {full_cost}$')
    else:
        print('Кажется, ваш портфель еще пустой.')

# Добавляет криптовалюту в портфель в указанном количестве
def add_cryptocurrency(cryptocurrency, amount):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={cryptocurrency}&vs_currencies=usd&x_cg_demo_api_key=CG-AVBFDUPDA8SrMQKT1qytuwaE"
    response = requests.get(url)
    json = response.json()
    if response.status_code == 200 and len(json) != 0:
        cryptocurrency_bag[cryptocurrency] = amount
        print(f'В портфель добавлена валюта {cryptocurrency} в\
количестве {amount}.')
        return
    else:
        print('Кажется, произошла какая-то ошибка.')

# Удаляет криптовалюту из портфеля
def delete_cryptocurrency(choice_to_delete):
    if choice_to_delete in cryptocurrency_bag:
        del cryptocurrency_bag[choice_to_delete]
        print(f'Валюта {choice_to_delete} удалена.')
    else:
        print('Кажется, произошла какая-то ошибка.')

# Выводит изменение цены криптовалюты за последнюю неделю
def sm(cryptocurrency):
    start_date = datetime.datetime.now() - datetime.timedelta(days=7)
    end_date = datetime.datetime.now()
    url = f"https://api.coingecko.com/api/v3/coins/{cryptocurrency}/market_chart/range?vs_currency=usd&from={start_date.timestamp()}&to={end_date.timestamp()}&x_cg_demo_api_key=CG-AVBFDUPDA8SrMQKT1qytuwaE"
    response = requests.get(url)
    json = response.json()
    if response.status_code == 200 and len(json) != 0:
        print('Изменение цен за предыдущую неделю:')
        for price in json['prices']:
            date = datetime.datetime.fromtimestamp(price[0]/1000)
            formatted_date = date.strftime('%Y-%m-%d')
            print(f'{formatted_date}: {price[1]}$')
    else:
        print('Кажется, произошла какая-то ошибка.')


def main():
    while True:
        choice = input('Выберите действие:\n\
1) Посмотреть портфель\n\
2) Добавить криптовалюту в портфель\n\
3) Убрать криптовалюту из портфеля\n\
4) Посмотреть исторические данные о ценах на криптовалюту\n\
5) Выход\n')
        if choice == '1':
            get_cryptocurrency_bag()
        if choice == '2':
            cryptocurrency = input('Введите названию криптовалюты: ').lower()
            amount = input('Введите количество криптовалюты: ')
            add_cryptocurrency(cryptocurrency, amount)
        if choice == '3':
            if len(cryptocurrency_bag) != 0:
                print('В вашем портфеле есть следующие криптовалюты:')
                for coin in cryptocurrency_bag:
                    print(coin)
                choice_to_delete = input('Введите название криптовалюты, \
которую хотите удалить: ').lower()
                delete_cryptocurrency(choice_to_delete)
            else:
                print('Кажется, ваш порфель еще пустой.')
        if choice == '4':
            cryptocurrency = input('Введите название криптовалюты: ').lower()
            sm(cryptocurrency)
        if choice == '5':
            print('Сеанс завершен.')
            break


main()

"""# Дополнительно: Задание 4

Задание 4: Проектное

Вам необходимо самостоятельно найти откртое API предоставляющее информацию в открытом доступе и реализовать собственный проект!


Критерии приемки результата:

- Проект включает в себя не менее 5 возможостей для пользователя
- Проект позволяет использовать все возможности проекта пользователю при помощи взаимодействия через коммандную строку
- Проект работает с открытым API (это значит что при проверке вашей работы преподавателем, преподавателю необходимо просто запустить ячейку с кодом вашего проекта и она будет работать без дополнительных манипуляции)
- Проект должен обязательно включать в себя ряд используемых конструкции:
    - Функции
    - Условные конструкции
    - Ввод/вывод
    - Словари/Списки
- Допускается использование библиотек:
    - requests
    - datetime
    - random

**Здесь добавьте описание вашего проекта**
"""

#  А здесь код