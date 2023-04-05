#Задание 1.Пользователь вводит с клавиатуры название фрукта.Необходимо вывести на экран количество раз,
#сколькофрукт встречается в кортеже в качестве элемента.
#Задание 2.Добавьте к заданию 1 подсчет количества раз, когданазвание фрукта является частью элемента.
#Например:banana, apple, bananamango, mango, strawberry-banana.В примере выше banana встречается три раза.
'''def count(tuple,target,counter=0,counter_2=0):
    for i in tuple:
        if target == i:
            counter+= 1
        if target in i:
            counter_2+=1
    return counter,counter_2
dict_el_1 = ('apple','applebanana', 'apple')
print(count(dict_el_1,'apple'))'''
#Задание 3.Есть кортеж с названиями производителей автомобилей (название производителя может встречаться от 0до N раз).
#Пользователь вводит с клавиатуры названиепроизводителя и слово для замены.
#Необходимо заменитьв кортеже все элементы с этим названием на слово длязамены. Совпадение по названию должно быть полным.
'''avto = ('Porshe','BMW', 'Nissan','Ford', 'Mitsubisi')
def tuple_replace(tuple_input, old_word, new_word):
    return tuple([new_word if i == old_word else i for i in tuple_input])
print(tuple_replace(avto,'BMW','Mercedes'))'''
#Задание 4.Есть множество, содержащее название стран. Необходимо предоставить пользователю возможности:
#■ Добавление стран;■ Удаления стран;■ Поиска стран по введенным символам;
#■ Проверки существует ли страна внутри множества
'''country = {'Russia','Azerbaijan','Germany','Italy','Finland'}
def main():
    while True:
        choice = int(input('1 - add country\n'
                           '2 - delete country\n'
                           '3 - search country\n'
                           '4 - does exist country\n'
                           '5 - exit'))
        if choice == 1:
            add_country()
        elif choice == 2:
            delete_country()
        elif choice == 3:
            search_country()
        elif choice == 4:
            exist_country()
        elif choice == 5:
            return -1
def add_country():
    new_country = input()
    country.add(new_country)
    print(f'country {new_country} was added')
    print(country)

def delete_country():
    new_country = input()
    country.remove(new_country)
    print(f'country {new_country} was deleted')
    print(country)
def search_country():
    new_country = input()
    if new_country in country:
        print(f'country {new_country} was found')
    else:
        print('This country wasnt found')
    print(country)
def exist_country():
    new_country = input()
    if new_country in country:
        print(f'country {new_country} exists')
    else:
        print('This country doesnt exists')
print(country)
main()'''
#Задание 5.Существует два множества, содержащие названиягородов. Необходимо создать третье множество:
#■  содержащее названия, которые есть в обоих множествах.
#■  содержащее названия, которые есть в первом множестве,но нет во втором.
#■ содержащее названия, которые есть во втором множестве, но нет в первом.
#■ содержащее уникальные названия для каждого множества
'''goroda_1 = {'Baki','Fuzuli','Susa'}
goroda_2 = {'Moscow','St Peterburg','Krasnodar','Baki'}
tretye = {'Baki','Susa','Krasnodar','Texas'}'''
#Задание 6.Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста иего рост.
#ребуется реализовать возможность добавления,удаления, поиска, замены данных.
#Используйте словарьдля хранения информации.
'''basketball_players= {'Steph Curry':189,
                     'Lebron James:':206,
                     'Kevin Durant':208,
                     'Kyrie Irving':188}
def main():
    while True:
        choice = int(input('1 - add player\n'
                           '2 - delete player\n'
                           '3 - search player\n'
                           '4 - change info about player\n'
                           '5 - exit'))
        if choice == 1:
            add_player()
        elif choice == 2:
            delete_player()
        elif choice == 3:
            search_player()
        elif choice == 4:
            change_info()
        elif choice == 5:
            return -1

def add_player():
    name_player = input('Введите ФИО баскетболиста')
    height_player = input('Введите рост баскетболиста')
    basketball_players[name_player] = height_player
    print(f'Баскетболист {name_player} ростом {height_player} см был добавлен в словарь')
    print(basketball_players)

def delete_player():
    name_player = input('Введите ФИО басктеболиста')
    del basketball_players[name_player]
    print(f'Баскетболист {name_player} был удален из словаря')
    print(basketball_players)
def search_player():
    name_player = input('Введите ФИО басктеболиста')
    if name_player in basketball_players:
        print(f'Баскетболист {name_player} был найден')
    else:
        print(f'Этот басктболист не найден')
print(basketball_players)

def change_info():
    name_player = input('Введите ФИО баскетболиста')
    height = input('Введите рост баскетболиста')
    if name_player in basketball_players:
        basketball_players[name_player] = height
        print(f'Рост баскетболиста {name_player} был заменен на {basketball_players[name_player]} см')
    else:
        print('Игрок не найден')
print(basketball_players)
main()'''
#Задание 7.Создайте программу «Фирма». Нужно хранить информацию о человеке:
#ФИО, телефон, рабочий email,название должности, номер кабинета, skype.
#Требуетсяреализовать возможность добавления, удаления, поиска, замены данных.
#Используйте словарь для храненияинформации
'''firma = {
    'Смирнов Игорь Алексеевич': {
        "Телефон": "+971478745",
        "Почта": "smirnov12@gmail.com",
        'Должность': 'Управляющий',
        'Номер кабинета':15,
        'Скайп':'smirnov125'
    },
    'Рустамова Айнура Рафиг кызы': {
        "Телефон": "+9652999297",
        "Почта": "aynura1982@gmail.com",
        'Должность': 'Директор',
        'Номер кабинета':34,
        'Скайп':'aynura_rust82'
        },
    'Нуриманов Мамед Тофиг оглы': {
        "Телефон": "+314314531",
        "Почта": "nuriman421@gmail.com",
        'Должность': 'Бухгалтер',
        'Номер кабинета':19,
        'Скайп':'nurimamed4213'
        }
}
def main():
    while True:
        choice = int(input('1 - add\n'
                           '2 - delete\n'
                           '3 - search\n'
                           '4 - change\n'
                           '5 - exit'))
        if choice == 1:
            add_dict()
        elif choice == 2:
            delete_dict()
        elif choice == 3:
            search_dict()
        elif choice == 4:
            change_dict()
        elif choice == 5:
            return -1

def add_dict():
    name = input('Введите ФИО работника')
    number = input('Введите номер телефона работника')
    email = input('Введите почту работника')
    position = input('Введите должность работника')
    cabinet = input('Введите номер кабинета работника')
    skype = input('Введите скайп работника')
    firma[name] = {number,email,position,cabinet,skype}
    print(f'Работник {name} был(а) добавлен в фирму')
    print(firma)

def delete_dict():
    name = input('Введите ФИО работника')
    del firma[name]
    print(f'Работник{name} был(а) удален из фирмы')
    print(firma)

def search_dict():
    name = input('Введите ФИО работника')
    if name in firma:
        print(f'Работник {name} был(а) найден')
    else:
        print(f'Этот работник не найден')
print(firma)

def change_dict():
    name = input('Введите ФИО работника')
    number = input('Введите номер телефона работника')
    email = input('Введите почту работника')
    position = input('Введите должность работника')
    cabinet = input('Введите номер кабинета работника')
    skype = input('Введите скайп работника')
    if name in firma:
        firma[name] ={number,email,position,cabinet,skype}
        print(f'Данные работника {name} были изменены ')
        print(firma)
    else:
        print('Работник не найден')
main()
'''
# 8.Создайте программу «Книжная коллекция».
#Нужнохранить информацию о книгах: автор, название книги,жанр, год выпуска, количество страниц, издательство.
#Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для
'''spisok_knig = {
    '\"Мастер и Маргарита\"': {
        "Автор": "Михаил Булгаков",
        "Жанр": "Роман",
        'Год выпуска': 1967,
        'Количество страниц':416,
        'Издательство':'Азбука'
    },
    '\"Война и мир\"': {
        "Автор": "Лев Толстой",
        "Жанр": "Роман",
        'Год выпуска': 1867,
        'Количество страниц':1300,
        'Издательство':'Эксмо'
        },
    '\"Преступление и наказание\"': {
        "Автор": "Фёдор Достоевский",
        "Жанр": "Роман",
        'Год выпуска': 1866,
        'Количество страниц':672,
        'Издательство':'Азбука'
        }
}
def main():
    while True:
        choice = int(input('1 - add\n'
                           '2 - delete\n'
                           '3 - search\n'
                           '4 - change\n'
                           '5 - exit'))
        if choice == 1:
            add_dict()
        elif choice == 2:
            delete_dict()
        elif choice == 3:
            search_dict()
        elif choice == 4:
            change_dict()
        elif choice == 5:
            return -1

def add_dict():
    name = input('Введите название книги')
    author = input('Введите автора книги')
    genre = input('Введите жанр книги')
    year = input('Введите год выпуска книги')
    page = input('Введите количество страниц книги')
    publishing = input('Введите издательство книги')
    spisok_knig[name] = {author,genre,year,page,publishing}
    print(f'Книга {name} была добавлена в словарь')
    print(spisok_knig)

def delete_dict():
    name = input('Введите название книги')
    del spisok_knig[name]
    print(f'Книга {name} была удален из фирмы')
    print(spisok_knig)

def search_dict():
    name = input('Введите название книги')
    if name in spisok_knig:
        print(f'Книга {name} была найдена')
    else:
        print(f'Эта книга не найдена')
print(spisok_knig)

def change_dict():
    name = input('Введите название книги')
    author = input('Введите автора книги')
    genre = input('Введите жанр книги')
    year = input('Введите год выпуска книги')
    page = input('Введите количество страниц книги')
    publishing = input('Введите издательство книги')
    if name in spisok_knig:
        spisok_knig[name] ={author,genre,year,page,publishing}
        print(f'Данные книги {name} были изменены ')
        print(spisok_knig)
    else:
        print('Книга не найдена')
main()'''



