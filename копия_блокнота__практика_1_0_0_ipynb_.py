# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 1.0.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h_mZDXVjrdFgePjoo0Mwr8Cx_DYmzm3n

ФИО: Лобова Кристина Михайловна  зачет( 19 11 2024)

> Добавить блок с цитатой

# Задание (совместное с преподавателем)

Напишите систему для учёта отпусков с возможностью узнавать, сколько дней отпуска осталось у того или иного сотрудника.
Для этого создайте класс Employee со следующими методами:

- Метод consume_vacation должен отвечать за списание дней отпуска.

Единственный параметр этого метода (кроме self) — количество потраченных отпускных дней (целое число).

При вызове метода consume_vacation соответствующее количество дней должно вычитаться из общего числа доступных отпускных дней сотрудника.

Чтобы определить число доступных отпускных дней конкретного сотрудника, в классе опишите атрибут экземпляра |, который по умолчанию будет равен значению атрибута класса vacation_days, и используйте этот атрибут в работе метода.

- Метод get_vacation_details должен возвращать остаток отпускных дней сотрудника в формате: ```Остаток отпускных дней: <число>.```


Чтобы проверить работу программы:
1. Создайте экземпляр класса Employee.
2. Вызовите метод consume_vacation, указав подходящее значение аргумента, например 7.
3. Вызовите метод get_vacation_details.
"""

# Создание класса
class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender): # Конструктор класса
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days

    def consume_vacation(self, days): # Метод для вычитания отгулянных дней
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}'

employee1 = Employee('Иван', 'Иванович', 'м')
employee2 = Employee('Анна', 'Анновна', 'ж')

print(employee1.first_name, 'уехал в отпуск на 7 дней')
print(employee1.first_name, employee1.get_vacation_details())

employee1.consume_vacation(7)

print(employee1.first_name, employee1.get_vacation_details())

print(employee2.first_name, 'уехала в отпуск на 10 дней')
print(employee2.first_name, employee2.get_vacation_details())

employee2.consume_vacation(10)

print(employee2.first_name, employee2.get_vacation_details())

"""# Задание 1

Задание:

Создайте класс с именем Rectangle который имеет:
- Атрибуты ширины и высоты.
- Метод расчета площади.
- Метод расчета периметра.
- Метод отображения размеров прямоугольника.

Создайте экземпляр класса Rectangleи продемонстрируйте его функциональность.
"""

class Rectangle:

    def __init__(self, width, height): # Атрибуты ширины и высоты
        self.width = width
        self.height = height

    def get_square(self): # Метод расчета площади
        return self.width * self.height

    def get_perimeter(self): # Метод расчета периметра
        return 2 * self.width + 2 * self.height

    def get_rectangle_size(self): # Отображения размеров прямоугольника
        return f'ширина: {self.width}, высота: {self.height}'

rectangle = Rectangle(15, 10)

print(f'Площадь прямоугольника: {rectangle.get_square()}')
print(f'Периметр прямоугольника: {rectangle.get_perimeter()}')
print(f'Размеры прямоугольника: {rectangle.get_rectangle_size()}')

"""# Задание 2

Задание: Создайте мини версию банковской системы:


Инструкции:

1. Создайте класс BankAccountсо следующими атрибутами:
    - account_holder -  владелец счета
    - balance - баланс счета

2. Реализуйте следующие методы:
    - Метод для инициализации владельца счета: имя владельца счета и установите начальный баланс на 0.
    - deposit(amount): Добавьте указанную сумму к балансу.
    - withdraw(amount): Вычесть указанную сумму из баланса, если средств достаточно; в противном случае вывести предупреждение.
    - get_balance(): Возврат текущего баланса.


Создайте объект класса и продемонстрируйте его возможности
"""

class BankAccountсо:

    def __init__(self, account_holder): # Атрибут владельца счёта и баланса
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount): # Метод пополнения счёта
        self.balance += amount
        return f'Счёт пользователя {self.account_holder} \
был пополнен на {self.balance}'

    def withdraw(self, amount): # Метод снятия денег со счёта
        if self.balance >= amount:
            self.balance -= amount
            return f'Со счёта пользователя {self.account_holder} \
было снято {self.balance}'
        else:
            print('Недостаточно средств на счёте.')

    def get_balance(self): # Метод вывода баланса
        return f'Текущий баланс: {self.balance}'

account = BankAccountсо('Мария')
print(f'Владелец счета: {account.account_holder}')
print(f'Текущий баланс: {account.get_balance()}')

print(account.deposit(1000))
print(account.withdraw(500))

print(account.get_balance())

"""# Задание 3

Возьмите код и задание (Рыцарь и дракон) из предыдущей практики и реализуйте его с применением классов
"""

import random

class Hero:
    def __init__(self, name):
        self.name = name.upper()
        self.coins = 5
        self.armor = None
        self.weapon = None
        self.defense = 0
        self.damage = 0
        self.health = random.choice([50, 70, 90, 100])

    def choose_armor(self):
        armor_choice = input('Выберите вид доспеха:\n',
                            '1) Кожаная: +5 к защите - 1 монета\n',
                            '2) Кольчужная: +7 к защите - 2 монеты\n',
                            '3) Железная броня: +10 к защите - 3 монеты\n')
        if armor_choice == '1':
            self.armor = 'кожаные'
            self.defense = 5
            self.coins -= 1
        elif armor_choice == '2':
            self.armor = 'кольчужные'
            self.defense = 7
            self.coins -= 2
        elif armor_choice == '3':
            self.armor = 'железные'
            self.defense = 10
            self.coins -= 3
        else:
            exit('Нет такой брони!')

    def choose_weapon(self):
        weapon_choice = input(f'Монет на счету: {self.coins}.\n\
Выберите вид оружия:\n\
1) Палка: +10 к атаке - 1 монета\n\
2) Рогатка: +20 к атаке - 2 монеты\n\
3) Меч: +30 к атаке - 3 монеты\n')
        if weapon_choice == '1':
            self.weapon = 'палка'
            self.damage = 10
            self.coins -= 1
        elif weapon_choice == '2':
            self.weapon = 'рогатка'
            self.damage = 20
            self.coins -= 2
        elif weapon_choice == '3':
            self.weapon = 'меч'
            self.damage = 30
            self.coins -= 3

        if self.coins < 0:
            exit('Вы превысили бюджет! Сборщики дани конфисковали ваших родных.')

    def display_player_info(self):
        print(f'Имя: {self.name}, доспехи: {self.armor}, оружие: {self.weapon},\
защита: {self.defense}, атака: {self.damage}, здоровье: {self.health}.')


class Dragon:
    def __init__(self):
        self.name = random.choice(['Фламберг', 'Загрей', 'Алый', 'Вихрь', 'Багровый'])
        self.health = random.choice([100, 150, 200])
        self.damage = random.choice([10, 12, 15])

    def display_dragon_info(self):
        print(f'Дракон: {self.name}, здоровье: {self.health}, урон: {self.damage}.')

class Fight:
    def __init__(self, hero, dragon):
        self.hero = hero
        self.dragon = dragon

    def start_fight(self):
        print(f'В средневековой деревне жили добрые и трудолюбивые люди, выращивавшие пшеницу и разводившие овец.\n\
Однажды на деревню напал дракон {self.dragon.name}, и люди в ужасе бежали.\n\
Вы, доблестный рыцарь {self.hero.name}, на коне бросились на помощь.')

        while self.hero.health > 0 and self.dragon.health > 0:
            choice = input('Что вы сделаете?\n\
1) Атаковать\n2) Увернуться\n')
            if choice in ['1', '2']:
                current_move = random.choice(['dragon_attack', 'hero_attack'])  # Рандомный выбор, кто ходит: дракон или игрок
                if current_move == 'dragon_attack' and choice == '1':  # Ход дракона, игрок атакует
                    print(f'Дракон прервал вашу атаку и нанес вам урон! Ваша защита не засчитана.\n\
Нанесенный дракона урон: {self.dragon.damage}, ваше здоровье: {self.hero.health - self.dragon.damage}, здоровье дракона: {self.dragon.health}')
                    self.hero.health -= self.dragon.damage
                elif current_move == 'dragon_attack' and choice == '2':  # Ход дракона, игрок защищается
                    damage_taken = max(0, self.dragon.damage - self.hero.defense)
                    print(f'Вы защитились от атаки дракона! Ваша защита засчитана.\n\
Нанесенный драконом урон: {damage_taken}, ваше здоровье: {self.hero.health - damage_taken}, здоровье дракона: {self.dragon.health}')
                    self.hero.health -= damage_taken
                elif current_move == 'hero_attack' and choice == '1':  # Ход игрока, игрок атакует
                    print(f'Вы нанесли урон дракону!\n\
Нанесенный вами урон: {self.hero.damage}, ваше здоровье: {self.hero.health}, здоровье дракона: {self.dragon.health - self.hero.damage}')
                    self.dragon.health -= self.hero.damage
                elif current_move == 'hero_attack' and choice == '2':  # Ход игрока, игрок защищается
                    print(f'Вы пропустили свою атаку! Урона не нанесено.\n\
Нанесенный урон: 0, ваше здоровье: {self.hero.health}, здоровье дракона: {self.dragon.health}')

        if self.hero.health <= 0:
            print(f'Победил дракон {self.dragon.name}!')
        elif self.dragon.health <= 0:
            print(f'Победил рыцарь {self.hero.name}!')

hero_name = input('Имя героя: ')
hero=Hero(hero_name)
hero.choose_armor()
hero.choose_weapon()
hero.display_player_info()

dragon = Dragon()
dragon.display_dragon_info()

fight = Fight(hero, dragon)
fight.start_fight()

"""# Дополнительное задание

Задача: Система управления библиотекой

**Цель**
Создайте простую систему управления библиотекой, которая позволит пользователям добавлять книги, брать книги, возвращать книги и просматривать список доступных книг.

**Требования**

1. **Определение класса**:
   – Создайте класс с именем «Book» со следующими атрибутами:
     - `title`
     - `автор`
     - `isbn`
     - `is_borrowed` (по умолчанию `False`)

2. **Класс библиотеки**:
   - Создайте класс с именем Library, который управляет коллекцией книг.
   - Класс должен иметь следующие методы:
     - `__init__(self)`: инициализирует пустой список книг.
     - `add_book(self, book: Book)`: добавляет новую книгу в библиотеку.
     - `borrow_book(self, isbn: str)`: помечает книгу как заимствованную. Если книга не найдена или уже взята, выведите соответствующее сообщение.
     - `return_book(self, isbn: str)`: помечает книгу как возвращенную. Если книга не найдена или не была взята взаймы, выведите соответствующее сообщение.
     - `list_available_books(self)`: печатает список всех доступных книг в библиотеке.
     - `find_book(self, isbn: str)`: возвращает объект книги, если он найден, в противном случае возвращает `None`.

3. **Взаимодействие с пользователем**:
   - Создайте простое текстовое меню, которое позволит пользователям:
     - Добавить книгу
     - Одолжить книгу
     - Вернуть книгу
     - Список доступных книг
     - Выйти из программы
"""



