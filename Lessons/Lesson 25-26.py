#	Что такое функция?
'''
Функция - это область внутри программы(кода), в которую помещается некоторый код,
для дальнейшего его использования без повторного его написания
'''
#	Цели и задачи функции.
'''
Функции нужны для того, чтобы не повторять какую-то часть кода
по несколько раз, чтобы не заполнить ОЗУ и не делать ваш код сложно-читаемым
'''
#	Встроенные функции.
'''
max()
min()
len()
reversed()
sorted()
int() 
float()
str()
bool()
print()
len()
sum()
eval() - преобразовывает строчное выражение в математическое и выдает значение,
 которое является результатом какой-либо матем-ой операции
pow()
ord() - переводил в его десятичное представление по аски
oct() - 8
bin() - 2
hex() - 16
abs() - модуль
fabs() - int module
map()
filter()
zip()
reduce()
'''

#	Математические функции и случайные числа.
'''
import math
import random
'''

#Синтаксис объявления функций.
'''
def имя_функүии(параметры):
    инструция
 '''



#Аргументы и возвращаемые значения
'''
Виды функций:
1)ничего не принимает ничего не возвращает
2) при входе принимает но ничего не возвращает
3) ничего не принимает но возвращает
4)принимает и возвращает
'''
#1)ничего не принимает ничего не возвращает
'''def foo():
    print('Hello world')
foo()'''
#2)при входе принимает но ничего не возвращает
'''def Summ_el(num_1,num_2):
    summ = num_1+num_2
    print(summ)
Summ_el(4,125)
'''
#3) ничего не принимает но возвращает
'''def foo2():
    line = 'Hello world'
    return line
func = foo2()
print(func)'''

#4)принимает и возвращает
'''
def foo(a,b,c,d):
    list_el = []
    list_el.append(a)
    list_el.append(b)
    list_el.append(c)
    list_el.append(d)
    return list_el
func = foo(82,3.14,15,6344)
print(func)
print(foo(8,7,25,True))
'''
#___________________________________________________________________
#Practise
'''
1.Напишите функцию, которая принимает два числа в качестве параметра и отображает все нечетные числа между ними.
2.Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
 Функция принимает в качестве параметров: длину линии, направление, символ. 
3. Напишите функцию, которая возвращает максимальное из четырёх чисел. 
 Числа передаются в качестве параметров.  
4. Напишите функцию, которая возвращает сумму чисел в указанном диапазоне. Границы диапазона передаются в качестве параметров.
'''

'''def odd_numbers(num_1,num_2):
    for i in range(num_1,num_2):
        if i%2 !=0:
            print(i)
odd_numbers(10,20)
'''

'''def simbol_pos(length,navigation,symbol):
    if navigation == 1:
        print(symbol*length)
    if navigation ==2:
        for i in range(length):
            print(symbol)
length = int(input('Enter symbol length '))
symbol = input('Enter symbol:')
navigation = int(input('Choose:\n1.Horizontal\n2.Vertical\n'))
simbol_pos(length,navigation,symbol)
'''
#___________________________________________________________________

# Организация функций
'''
def main():
    say_hello()
    say_goodbye()
def say_hello():
    print("Hello")
def say_goodbye():
    print("Good Bye")
# Вызов функции main
main()
'''

#	Распаковка и упаковка аргументов.
'''
Распаковка 
Мы можем использовать * для распаковки списка, чтобы все его элементы можно было передавать как разные параметры.
def fun(a, b, c, d):
    print(a, b, c, d)
my_list = [1, 2, 3, 4]
# Unpacking list into four arguments
fun(*my_list)
Упаковка 
Когда мы не знаем, сколько аргументов нужно передать функции
def mySum(*args):
    return sum(args)
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))
'''

#	Аргументы по умолчанию, аргументы-ключи.
'''
def print_person(name, age = 18):
    print(f"Name: {name}  Age: {age}")
print_person("Rafael")
#Именнованные параметры
def print_person(name, age):
    print(f"Name: {name}  Age: {age}")
print_person(age = 21, name = "Rafael")
# * -  Все параметры, которые располагаются справа от символа *, получают значения только по имени:
def print_person(name, *,  age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")
print_person("Bob", age = 41, company ="Microsoft") 
'''

#	Область видимости, правило LEGB.
'''
ОБЛАСТЬ ВИДИМОСТИ
LEGB
Интерпретатор начинает поиски имени изнутри, последовательно переходя от локальной 
области видимости к объемлющей, затем к глобальной и в завершении к встроенной.
Local -> Enclosed -> Global -> Built-in
Local - inside fun-s. Удаляется, когда функция или блок кода завершают свое выполнение.
Global - free space
Enclosed - подобная область видимости относится к переменным которые созданы в функция, которые были созданы внутри других
функций lambda(частный пример)
Built-in - все встроенные по типу pi, punctuation, and etc.
'''

#	Локальные и глобальные переменные в функциях.
'''
global название переменной
n = 15
print(n)#15
def change_value():
    global n
    n+=15
    print(n)
change_value()
nonlocal 
Имена, перечисленные в инструкции nonlocal, в отличие от тех, что перечислены в инструкции global,
должны ссылаться на ранее существовавшие переменные в охватывающей области.
def football():
    x = 'Ronaldo'
    def argentina():
        nonlocal x
        x = 'Messi'
    return x
print(football())
'''

#	Функции как объекты первого класса.
'''
Это означает, что функции можно передавать и использовать в качестве аргументов, 
как и любой другой объект(string, int, float, list и т.Д.).
Особенности функций как объектов первого класса:
Функции можно присваивать переменным.
Функцию можно вернуть из функции.
У функций те же свойства и методы, что и у объектов(OOП).
Функцию можно передать в качестве аргумента при вызове другой функции.
def my_object(text):
    return text.upper()  
print(my_object("Вызов my_object"))    
upper = my_object  
print(upper("Вызов upper")) 
'''

#	Рекурсия.
''' 
#Рекурсивная функция - та функция, что вызывает саму же себя.
#Без рекурсии:
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
#С ней:
#С ней:
def factorial(n):
    if n == 1:
        return 1
    else: return n * factorial(n - 1)
'''

'''
Задание 5
Напишите функцию, которая отображает пустой или
заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой.
True
******
******
******
False
******
*    *
*    *
******
'''
'''length = int(input("insert length:"))
symbol = input("isnert simvol")
choice = input("insert your choice\n"
               "True/False:")
def square(length,symbol,choice):
    if choice=='True':
        for i in range(length):
            print(symbol*length)
    elif choice=='False':
        for i in range(length):
            for j in range(length):
                if i ==0 or j ==0 or i==length-1 or j==length-1:
                    print(symbol,end='')
                else:
                    print(" ",end='')
            print()
square(length,symbol,choice)'''

'''def Summ_el(num_1,num_2):
    summ = num_1+num_2
    print(summ)
Summ_el(4,125)
'''
'''
def summ_list(list_el):
    summ=0
    for i in list_el:
        summ+=i
    return summ
list_el =[]
list_el.append(6)
summ_list(list_el)
list_el.append(34)
summ_list(list_el)
list_el.append(70)
summ_list(list_el)
'''