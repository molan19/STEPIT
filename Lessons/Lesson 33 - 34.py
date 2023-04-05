# Tuple(кортеж)
'''
Кортеж (tuple) представляет последовательность элементов,
 которая во многом похожа на список за тем исключением,
 что кортеж является неизменяемым (immutable) типом.
Мы не можем добавлять или удалять элементы в кортеже, изменять его.
Кортеж очень часто используется для защиты хранимых данных приложения от незапланированных или непреднамеренных изменений.
Кортеж также требует выделения значительно меньшего количества памяти.
info = 'Raf',21
print(type(info))
info = ('Raf',21)
print(type(info))
'''

# Set(множество)
'''
Set(множество) представляют очередной вид набора элементов, который хранит только уникальные элементы.
names = {"Raf", "Ne Raf", "Raf", "Rafael"}
print(names)
print(type(names))
add() -	Добавляет элемент в набор
clear() -	Удаляет все элементы из набора
copy() - Возвращает копию набора
difference() -	Возвращает набор, содержащий разницу между двумя или более наборами
difference_update() -	Удаляет элементы в этом наборе, которые также входят в другой указанный набор
intersection() -	Возвращает набор, являющийся пересечением двух других наборов
intersection_update() -	Удаляет элементы в этом наборе, которых нет в других указанных наборах.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
z = x.difference_update(y)
print(z)
z = x.intersection(y)
print(z)
x.intersection_update(y)
print(x)
discard() -	Удалить указанный элемент
remove() -	Удалить указанный элемент
pop() - Удаляет и возвращает произвольный элемент набора.
isdisjoint() -	Возвращает, имеют ли два набора пересечение или нет
issubset() -	Возвращает, содержит ли другой набор этот набор или нет
issuperset() -	Возвращает, содержит ли этот набор другой набор или нет
union() -	Вернуть объединение наборов как новый набор.
update() -	Обновить набор с объединением себя и других
'''

# Frozen set
'''
Frozen set является видом множеств, которое не может быть изменено.
В такое множество мы не можем добавить новые элементы, как и удалить из него уже имеющиеся.
names = frozenset({"Rafael", "Tengiz", "Orhan"})
'''

# Dictionary(словарь)
'''
Словарь (dictionary) тип данных который хранит коллекцию элементов,
 где каждый элемент имеет уникальный ключ и некоторое значение,которое хранится за ключом.
#Синтаксис:
dictionary = { ключ1:значение1, ключ2:значение2, ....}
Ключом может быть int,str,float (не может быть дубликатов ключей)
Значением могут быть -  int,str,float,bool and other collections (могут быть дубликаты значений)
#Комлпексные словари
users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    }
}
#Преобразований списков/кортежей в словари и добавление элементов вручную:
users_tuple = (
    ("+994", "AZE"),
    ("+5", "USA"),
    ("+49", "Germany"),
)
users_dict = dict(users_tuple)
print(users_dict)
print(users_dict['+5'])
users_dict['+380']='Ukraine'
print(users_dict)
#Loops in Dictionaries
#Dictionary methods
clear()	Удаляет все элементы из словаря
copy()	Возвращает копию словаря
fromkeys() Возвращает словарь с указанными ключами и значением
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
get()	Возвращает значение указанного ключа
items()	Возвращает список, содержащий кортеж для каждой пары ключ-значение.
for key,value in dict.items():
    print(x,y)
keys()	Возвращает список, содержащий ключи словаря
values()	Возвращает список всех значений в словаре
pop()	Удаляет элемент с указанным ключом
popitem()	Удаляет последний элемент
setdefault()	Возвращает значение указанного ключа. Если ключ не существует: вставьте ключ с указанным значением
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
update()	Обновляет словарь указанными парами ключ-значение.
car.update({"color": "White"})
'''

# Practise
'''
Задание 1.
Пользователь вводит с клавиатуры название фрукта.
Необходимо вывести на экран количество раз, сколько
фрукт встречается в кортеже в качестве элемента.
Задание 2.
Добавьте к заданию 1 подсчет количества раз, когда
название фрукта является частью элемента. Например:
banana, apple, bananamango, mango, strawberry-banana.
В примере выше banana встречается три раза.
Задание 3.
Есть кортеж с названиями производителей автомобилей (название производителя может встречаться от 0
до N раз). Пользователь вводит с клавиатуры название
производителя и слово для замены. Необходимо заменить
в кортеже все элементы с этим названием на слово для
замены. Совпадение по названию должно быть полным.
Задание 4.
Есть множество, содержащее название стран. Необходимо предоставить пользователю возможности:
■ Добавление стран;
■ Удаления стран;
■ Поиска стран по введенным символам;
■ Проверки существует ли страна внутри множества
Задание 5.
Существует два множества, содержащие названия
городов. Необходимо создать третье множество: 
■  содержащее названия, которые есть в обоих множествах.
■  содержащее названия, которые есть в первом множестве, но
нет во втором.
■ содержащее названия, которые есть во втором множестве, но
нет в первом.
■ содержащее уникальные названия для каждого множества
Задание 6.
Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста и
его рост. Требуется реализовать возможность добавления,
удаления, поиска, замены данных. Используйте словарь
для хранения информации.
Задание 7.
Создайте программу «Фирма». Нужно хранить информацию о человеке: ФИО, телефон, рабочий email,
название должности, номер кабинета, skype. Требуется
реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для хранения
информации.
Задание 8.
Создайте программу «Книжная коллекция». Нужно
хранить информацию о книгах: автор, название книги,
жанр, год выпуска, количество страниц, издательство.
Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для
хранения информации.
'''

'''
tuple_el = 1,1,2,232
tuple_el_2 = (1,2.3,'Hello',True)
print(tuple_el)
print(type(tuple_el))
print(tuple_el_2)
print(type(tuple_el_2))
for i in range(len(tuple_el)):
    print(tuple_el[i])
from functools import reduce
print(tuple(filter(lambda element:element%2==0,tuple_el)))
print(tuple_el)
print(list(tuple_el))
'''

'''set_el = {1,1.2,True, False, 'String', True,1,1.2}
set_el2 = {11,22,1.2,True, False,'Python the best', 'String', True,1,1.2}
set_el2.difference_update(set_el)
print(set_el2)'''

'''x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)
for i in x:
    print(x)'''

'''
dict_el = {'Rafael': {
                'Nationality':'AZE',
                'height': 187,
                'info': [21,'kariye']
                        },
    'Amin':14,'Rauf':16,'Leyla':21}
print(dict_el['Rafael']['info'])
'''

'''users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Angelo": {
        "phone": "+12312313",
        "email": "angelo.cool@gmail.com"
        }
}'''

'''users_tuple = (
    ("+994", "AZE"),
    ("+5", "USA"),
    ("+49", "Germany"),
)
users_dict = dict(users_tuple)
print(users_dict)
print(users_dict['+5'])
users_dict['+380']='Ukraine'
print(users_dict)
'''

'''dict_el = {'Rafael': 21,'Amin':14,'Rauf':16,'Leyla':21}
for i in dict_el:
    print(dict_el[i])
for i in dict_el.items():
    print(i)
x = ('key1', 'key2', 'key3')
y = [1,2,3]
thisdict = dict.fromkeys(x, y)
print(thisdict)
dict_el = {'Rafael': 21,'Amin':14,'Rauf':16,'Leyla':21}
#print(dict_el.get('Rafael'))
for key,value in dict_el.items():
    print(key,value)
    print(key)
    print(value)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)
del car["model"]
print(car)'''

# Example
'''
Создайте программу «Англо-Русский словарь».
Нужно хранить слово на английском языке и его перевод
на русском. Требуется реализовать возможность добавления,
удаления, поиска, замены данных в словаре. Используйте
словарь для хранения информации.
'''
'''
# Создаем пустой словарь
dictionary = {}
# Определяем функцию для добавления новых слов
def add_word():
    pass
# Определяем функцию для удаления слов
def remove_word():
    pass
# Определяем функцию для поиска слов
def search_word():
    pass
# Определяем функцию для замены перевода слова
def replace_word():
    pass
# Определяем функцию main c бесконечным циклом для взаимодействия с пользователем (menu)
def main():
    pass
'''

dict_el = {}


def main():
    while True:
        choice = int(input('Choose option:\n1.Add element'
                           '\n2.Delete element'
                           '\n3.Find element'
                           '\n4.Change element'
                           '\n5.Print all elements'
                           '\n6.Exit\n'))

        if choice == 1:
            add_dict()
        elif choice == 2:
            del_dict()
        elif choice == 3:
            find_dict()
        elif choice == 4:
            change_dict()
        elif choice == 5:
            print_dict()
        elif choice == 6:
            return -1


def add_dict():
    eng_word = input('Enter word in English')
    rus_word = input('Enter the traslation of the word')
    dict_el[eng_word] = rus_word
    print(f'{eng_word} was added to the dictionary with value = {dict_el[eng_word]}\n')


def del_dict():
    eng_word = input('Enter the word in English that you want to delete')
    del dict_el[eng_word]
    print(f'word {eng_word} was deleted from dictionary')


def find_dict():
    eng_word = input('Write the key to find value')
    if eng_word in dict_el:
        print(f'The value {dict_el[eng_word]} was found by key {eng_word}')
    else:
        print('Nothing was found')


def change_dict():
    eng_word = input('Enter word in English')
    rus_word = input('Enter the traslation of the word')
    if eng_word in dict_el:
        dict_el[eng_word] = rus_word
        print(f'Word {eng_word} changed translation to {dict_el[eng_word]}')
    else:
        print('Word was not found')


def print_dict():
    for key, value in dict_el.items():
        print(key, value)


main()