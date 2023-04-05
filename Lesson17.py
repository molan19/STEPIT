'''dict_el = {'Rafael':21,'Amin':14}
for i in dict_el:
    print(dict_el[i])'''
'''x = ['key1','key2','key3']
y = 0
this_dic = dict.fromkeys(x,y)
print(this_dic)#(key1:0,key2:0,key3:0)
#Замена ключа
dict_el_1 = {'Rafael':21,'Amin':14}
dict_el_1 = ['Aziz'] = dict_el_1.pop('Rafael')


dict_el = {'Rafael':21,'Amin':14}
print(dict_el.get('Rafael')) #Выводит значение(21)

for key,value in dict_el.items():
    print(key,value) #Выводит ключ и значение(Рафаель 21)

print(dict_el.values()) #значение
print(dict_el.keys()) #ключи

car = {
    'brand':'Ford',
    'year':1964,

}
x = car.setdefault('model','Bronco')
print(x)
print(car)
car.update({'color':'White'})
print(car)'''

'''dict_el = {}
def add_dic():
    eng_word = input('Введите слово на английском')
    rus_word = input('Введите перевод слова')
    dict_el[eng_word]=rus_word
    print(f'{eng_word} was added to the dictionary with value = {dict_el[eng_word]}\n')

def delete_dic():
    eng_word = input('Введите слово на английском которое хотите удалить')
    del dict_el[eng_word]
    print(f' {eng_word} was deleted from dictionary')

def find_dic():
    eng_word = input('Введите ключ чтобы найти значение')
    if eng_word in dict_el:
        print(f' The value {dict_el[eng_word]} was found by key {eng_word}')
    else:
        print('Nothing was found')


def change_dic():
    eng_word = input('Введите слово на английском')
    rus_word = input('Введите перевод слова')
    if eng_word in dict_el:
        dict_el[eng_word] = rus_word
        print(f' word {eng_word} changed transaltion to {dict_el[eng_word]}')
    else:
        print('Word was not found')

def print_dic():
    for key,value in dict_el:
        print(key,value)

def main():
    while True:
        choise = int(input('Выбери опцию: \n1. Добавить элемент '
                           '\n2. Удалить элемент'
                           '\n3. Найти элемент'
                           '\n4. Изменить элемент'
                           '\n5. Вывод элементов'
                           '\n6. Выход '))
        if choise == 1:
            add_dic()
        elif choise == 2:
            delete_dic()
        elif choise == 3:
            find_dic()
        elif choise == 4:
            change_dic()
        elif choise == 5:
            print_dic()
        elif choise == 6:
            return -1

main()''''''
Задание 1.Пользователь вводит с клавиатуры название фрукта.Необходимо вывести на экран количество раз, 
сколькофрукт встречается в кортеже в качестве элемента.
Задание 2.Добавьте к заданию 1 подсчет количества раз, когданазвание фрукта является частью элемента. 
Например:banana, apple, bananamango, mango, strawberry-banana.В примере выше banana встречается три раза.
Задание 3.Есть кортеж с названиями производителей автомобилей (название производителя может встречаться от 0до N раз). 
Пользователь вводит с клавиатуры названиепроизводителя и слово для замены. 
Необходимо заменитьв кортеже все элементы с этим названием на слово длязамены. Совпадение по названию должно быть полным.
Задание 4.Есть множество, содержащее название стран. Необходимо предоставить пользователю возможности:
■ Добавление стран;■ Удаления стран;■ Поиска стран по введенным символам;
■ Проверки существует ли страна внутри множестваЗадание 
5.Существует два множества, содержащие названиягородов. Необходимо создать третье множество: 
■  содержащее названия, которые есть в обоих множествах.■  содержащее названия, которые есть в первом множестве,
нонет во втором.■ содержащее названия, которые есть во втором множестве, нонет в первом.
■ содержащее уникальные названия для каждого множестваЗадание 
6.Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста иего рост. 
Требуется реализовать возможность добавления,удаления, поиска, замены данных. 
Используйте словарьдля хранения информации.Задание 
7.Создайте программу «Фирма». Нужно хранить информацию о человеке: 
ФИО, телефон, рабочий email,название должности, номер кабинета, skype. 
Требуетсяреализовать возможность добавления, удаления, поиска, замены данных. 
Используйте словарь для храненияинформации.Задание 8.Создайте программу «Книжная коллекция». 
Нужнохранить информацию о книгах: автор, название книги,жанр, год выпуска, количество страниц, издательство.
Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь для'''
#Задание 1 и 2
'''def count(tuple,target,counter=0):
    for i in tuple:
        if target in i:
            counter+= 1
    return counter
dict_el_1 = ('apple','applebanana', 'apple')
print(count(dict_el_1,'apple'))'''


