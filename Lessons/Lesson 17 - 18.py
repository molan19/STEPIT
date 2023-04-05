# Форматирование строк
# f"stroka....{x} stroka...  {y} stroka..." - 1 sposob
# text = "Hello, {first_name}.".format(first_name="Tom") - 2 sposob (immenovanniy)
# info = "Name: {0}\t Age: {1}".format("Bob", 23) - takje vtoroy sposob(parametr po poziciyi)

# placeholders:
'''
s: для вставки строк
d: для вставки целых чисел
f: для вставки дробных чисел.
%: умножает значение на 100 и добавляет знак процента
e: выводит число в экспоненциальной записи

{переменная:placeholder}
{:[количество_символов][запятая][.число_знаков_в_дробной_части] плейсхолдер}


string = "Hello {:s}"
name = "Tom"
formatted_string = string.format(name)
print(formatted_welcome)

takje rabotayet:
source = "{:d} символов"
source = "{:,d} символов" - zapataya dlya ukazaniya razradov chisla
number_1 = 11.213124142
print("{:.3f}".format(number))
print(f"{number_1:%}")
print(f"{number_1:.0%}")
print(f"{number_1:.1%}")



bez metodov format:
info = "Имя: %s \t Возраст: %d" % ("Tom", 35)
print(info)
'''

# Sep,End

# String library
'''
#biblioteka string pomogayet ispolzovat ves alfavit i ascii table tak je yego simvoli
import string
print(string.ascii_uppercase) #zaglavniye bukvi
print(string.ascii_lowercase) #malenkiye bukvi
print(string.ascii_letters) #vse bolshiye i malenkiye bukvi
print(string.digits) # 0-9 vse cifri
print(string.punctuation) #punktuaciya
print(string.hexdigits) #16-ch sistema schisleniya
print(string.octdigits) #8-richnaya sistema schisleniya
#vsevozmojniye dla printa
'''

# print("--------password generator--------")
import string
import random

'''upperCase = string.ascii_uppercase
lowerCase = string.ascii_lowercase
numbers =string.digits
symbols = string.punctuation
allSymbol = upperCase + lowerCase + numbers + symbols
print(allSymbol)
'''
'''#method_2
allSymbol=string.printable
password = ''
length = int(input("Vvedite dlinu parola:"))#10
for i in range(length+1):
    password+=random.choice(allSymbol)
print(password)
'''

# Array and List. Stack and Heap
'''
Массив - структура объектов фиксированного размера 
Коллекция - структура объектов с динамически изменяющейся размерностью
массивы следует применять там, где будет строго фиксированное количество элементов;
 если предполагается изменение количества элементов, следует применять коллекции.

 две области в оперативной памяти — стек (stack) и кучу (heap).

Stack:
Стек используется для статичного выделения памяти.
Heap:
Куча используется для динамического выделения памяти

Если программа потребляет память не высвобождая её, то, в конечном итоге, она поглотит 
все доступные резервы и попытается выйти за пределы памяти.
 Тогда она просто упадет сама, или, что ещё драматичнее, обрушит операционную систему.

Сборка мусора — это процесс автоматического управления памятью в куче, 
который заключается в поиске неиспользующихся участков памяти, которые ранее были заняты 
под нужды программы.



'''

# List , Ссылочный тип данных list.
'''
Список (list) представляет тип данных, который хранит набор или последовательность элементов.
numbers1 = [1, 2, 3, 4, 5]
numbers2 = list([1, 2, 3, 4, 5])
string = ['Hello']
print(string)
letters = list("Hello")
print(letters) 
'''
# Обращение к элементам списка
# Разложение списка
'''
people = ["Tom", "Bob", "Sam"]
tom, bob, sam = people
'''
# Перебор элементов (for,while)
# Сравнение списков
'''
numbers1 = [1, 2, 3, 4, 5]
numbers2 = list([1, 2, 3, 4, 5])
if numbers1 == numbers2:
    print("numbers1 equal to numbers2")
else:
    print("numbers1 is not equal to numbers2")
'''

# Получение части списка
'''
list[:end]
list[start:end]
list[start:end:step]
'''
# List Comprehension - генератор списков
# ____________________________________________________________________


'''name = 'Osman'
age1 = 87
age2 = 312
print(f'{name} {age2+age1}')
'''  # text = "Hello, {first_name}.".format(first_name="Tom")#- 2 sposob (immenovanniy)
# print(text)
# info = "Name: {0}\t Age: {1} ----{2} ---- {3}---{1}".format("Bob", 23,2.1,56)# - takje vtoroy sposob(parametr po poziciyi)
# print(info)


'''
string = "Hello {:s}"
name = input()
formatted_string1 = string.format(name)
formatted_string2 = f'{string} {name:s}'
print(formatted_string1)
print(formatted_string2)
'''

# print('ChislO: {:,d}'.format(3425435345))#- zapataya dlya ukazaniya razradov chisla

'''
number_1 = 11.213124142
print("{:.3f}".format(number_1))#11.213
print(f"{number_1:%}")#1121.3124142%
print(f"{number_1:.0%}")
print(f"{number_1:.1%}")

info = "Имя: %s \t Возраст: %d" % ("Tom", 35)
print(info)
'''

# print('Hello', 'World', 'Dear', 'Person', sep= '-',end ='\t\t\t!')


'''import string
print(string.ascii_uppercase) #zaglavniye bukvi
print(string.ascii_lowercase) #malenkiye bukvi
print(string.ascii_letters) #vse bolshiye i malenkiye bukvi
print(string.digits) # 0-9 vse cifri
print(string.punctuation) #punktuaciya
print(string.hexdigits) #16-ch sistema schisleniya
print(string.octdigits) #8-richnaya sistema schisleniya'''

'''
import string
import random
upperCase = string.ascii_uppercase
lowerCase = string.ascii_lowercase
numbers =string.digits
symbols = string.punctuation
allSymbol = upperCase + lowerCase + numbers + symbols
print(allSymbol)
#method_2
allSymbol=string.printable
password = ''
length = int(input("Vvedite dlinu parola:"))#10
for i in range(length+1):
    password+=random.choice(allSymbol)
print(password)
'''
# ______________________________________________________
'''list_elements_1 = [5,9.3,True,'Tom', '___']
print(list_elements_1[3])
print(list_elements_1[-1])'''

'''string = ['Hello']
print(string)
letters = list("Hello world")
print(letters)
'''
'''string = ['Hello']*5
print(string)

list_elements_1 = [5,9.3,True,'Tom', '___']*2
print(list_elements_1[1])'''

'''people = ["Tom", True, 2]
tom, bob, sam = people
print(tom,bob,sam)'''

'''list_elements_1 = [5,9.3,True,'Tom', '___']


for i in range(0, len(list_elements_1)):
    print(list_elements_1[i], end= ' ')
i=0
while i<len(list_elements_1):
    print(f'\n{list_elements_1[i]}')
    i+=1'''

'''
list1 = [1,2,3]
list2 = list([1,2,3])

if list1==list2:
    print('Ravni')
else:
    print('ne ravni')


list1 = [1,2,3]
list2 = list([1,2,4])

if list1>list2:
    print('Bolshe')
else:
    print('menshe')


list3  = [[1,2,3], [5,7],['Hello'], random.randint()]'''

'''list1 = [1,2,3]
list2 = list([1,2,4])

list3 = list1+list2
print(list3)
list4 = list1[1]+ list2[2]
print(list4)'''

# В списке целых chisel, заполненном случайными числами
# вычислить: Сумму polojitelnix чисел;

'''from random import randint

list_random = [randint(-10,100),randint(-10,100),randint(-10,100)]
list_summ = 0
for i in range(0,len(list_random)):

    if list_random[i]>0:
        list_summ +=list_random[i]
        print(list_summ)'''

# В списке целых chisel, заполненном случайными числами
# вычислить: Сумму otricatelnix чисел;
# Сумму четных чисел;
# Сумму нечетных чисел;
# Произведение элементов с индексами кратными 3;
# Произведение элементов между минимальным и  максимальным элементом;


'''list = ['Tom', 'Khinkali', 'Pelmeshka', 'Borsh','Borsh','Borsh','Borsh','Borsh','Borsh']
print(list[1:7:2])'''